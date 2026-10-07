#!/usr/bin/env python3
"""Run unchanged planar-GHZ scientific suites and preserve exact-revision evidence."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
JOBS = (
    ('consolidation', 'check_consolidation.py', 'evidence/repeat.json', 5),
    ('source_dictionary', 'prior/check_source_dictionary.py', 'prior/evidence/repeat.json', 3),
    ('audit_rate', 'prior/prior/check_audit_and_rate.py', 'prior/prior/evidence/repeat.json', 5),
    ('initial_scout', 'prior/prior/prior/check_planar_bell.py', 'prior/prior/prior/evidence/repeat.json', 5),
)
ATOL, RTOL = 1e-13, 1e-12


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect_archive(root: Path = ROOT) -> dict:
    info = json.loads((root / 'provenance/IMPORT.json').read_text())
    archive = root / info['snapshot_directory']
    manifest_path = archive / 'MANIFEST.json'
    if digest(manifest_path) != info['manifest_sha256']:
        raise ValueError('Protected import manifest changed')
    manifest = json.loads(manifest_path.read_text())
    expected = set(manifest) | {'MANIFEST.json'}
    actual = {p.relative_to(archive).as_posix() for p in archive.rglob('*') if p.is_file()}
    if actual != expected or len(actual) != info['snapshot_members']:
        raise ValueError('Protected snapshot member set changed')
    for name, meta in manifest.items():
        relative = Path(name)
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('Unsafe imported path')
        p = archive / relative
        if p.is_symlink() or p.stat().st_size != meta['bytes'] or digest(p) != meta['sha256']:
            raise ValueError(f'Protected source changed: {name}')
    if digest(root / 'LICENSE') != info['license_sha256']:
        raise ValueError('Owner license changed')
    for name, meta in info['active_derivations'].items():
        if digest(root / name) != meta['sha256']:
            raise ValueError(f'Active account differs from declared import: {name}')
    return {'snapshot_members': len(actual), 'manifest_sha256': info['manifest_sha256'],
            'source_archive_sha256': info['source_archive_sha256'], 'all_hashes_match': True}


def compare(actual, reference, path='$') -> list[dict]:
    """Exact discrete comparison; report every permitted finite floating difference."""
    if type(actual) is not type(reference):
        raise ValueError(f'Type changed at {path}')
    if isinstance(reference, dict):
        if actual.keys() != reference.keys():
            raise ValueError(f'Keys changed at {path}')
        return [item for key in reference for item in compare(actual[key], reference[key], f'{path}.{key}')]
    if isinstance(reference, list):
        if len(actual) != len(reference):
            raise ValueError(f'Length changed at {path}')
        return [item for i, value in enumerate(reference) for item in compare(actual[i], value, f'{path}[{i}]')]
    if isinstance(reference, float):
        if not math.isfinite(actual) or not math.isfinite(reference):
            raise ValueError(f'Nonfinite value at {path}')
        delta = abs(actual - reference)
        if delta > ATOL + RTOL * abs(reference):
            raise ValueError(f'Numerical drift outside policy at {path}: {actual} vs {reference}')
        return [] if actual == reference else [dict(path=path, actual=actual, reference=reference, absolute_difference=delta)]
    if actual != reference:
        raise ValueError(f'Exact value changed at {path}')
    return []


def check_links(root: Path = ROOT) -> int:
    count = 0
    paths = list(root.glob('*.md')) + list((root / 'research').glob('*.md'))
    paths += list((root / 'literature').glob('*.md')) + list((root / 'work_orders').glob('*.md'))
    paths += list((root / 'docs').rglob('*.md'))
    paths += [root / 'archive/README.md', root / 'llms.txt']
    for path in paths:
        text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if re.match(r'[a-z]+:', link) or link.startswith('#'):
                continue
            target = (path.parent / link.split('#', 1)[0]).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                raise ValueError(f'Broken local link: {path.name}: {link}')
            count += 1
    return count


def fresh_output(path: Path, root: Path = ROOT) -> Path:
    path = path.resolve()
    archive = (root / 'archive').resolve()
    if path.is_relative_to(archive) or path == root.resolve() or path.exists():
        raise ValueError('Use a new output directory outside the protected archive')
    return path


def tracked_sources(root: Path = ROOT) -> dict:
    p = subprocess.run(['git', 'ls-files', '-z'], cwd=root, capture_output=True)
    if p.returncode == 0 and p.stdout:
        names = p.stdout.decode().strip('\0').split('\0')
    else:
        names = [p.relative_to(root).as_posix() for p in root.rglob('*')
                 if p.is_file() and not any(x in {'.git', '.artifacts', '__pycache__', '.venv'} for x in p.relative_to(root).parts)]
    return {name: {'sha256': digest(root/name), 'bytes': (root/name).stat().st_size} for name in sorted(names)}


def write_json(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False) + '\n')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    try:
        out = fresh_output(args.output)
    except ValueError as e:
        parser.error(str(e))
    out.mkdir(parents=True, exist_ok=False)
    summary = {'status': 'FAIL', 'scientific_groups': 0, 'suites': [],
               'comparison_policy': {'absolute': ATOL, 'relative': RTOL},
               'git_commit': subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.strip() or None}
    try:
        import numpy
        import scipy
        write_json(out/'environment.json', dict(python=sys.version, platform=platform.platform(),
                   numpy=numpy.__version__, scipy=scipy.__version__, blas_threads=1))
        write_json(out/'SOURCE_HASHES.json', tracked_sources())
        summary['preservation'] = inspect_archive()
        summary['active_local_links'] = check_links()
        archive = ROOT/'archive/consolidation-2026-10-07'
        env = {**os.environ, 'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1',
               'PYTHONDONTWRITEBYTECODE': '1', 'TERM': 'dumb'}
        for name, script, reference, groups in JOBS:
            report, log = out/(name+'.json'), out/(name+'.log')
            start = time.monotonic()
            with log.open('x') as handle:
                run = subprocess.run([sys.executable, str(archive/script), '--output', str(report)],
                    cwd=archive, env=env, stdout=handle, stderr=subprocess.STDOUT, timeout=180)
            data = json.loads(report.read_text())
            if run.returncode != 0 or data.get('status') != 'PASS' or data.get('tests_run') != groups:
                raise ValueError(f'Original scientific suite failed: {name}; inspect {log.name}')
            differences = compare(data, json.loads((archive/reference).read_text()))
            write_json(out/(name+'-differences.json'), differences)
            entry = dict(name=name, groups=groups, status='PASS', returncode=run.returncode,
                byte_identical=report.read_bytes() == (archive/reference).read_bytes(),
                changed_fields=len(differences), report_sha256=digest(report),
                seconds=time.monotonic()-start)
            summary['suites'].append(entry)
            summary['scientific_groups'] += groups
            print(json.dumps(entry), flush=True)
        inspect_archive()
        summary['status'] = 'PASS'
    except Exception as e:
        summary['error'] = str(e)
        print(str(e), file=sys.stderr, flush=True)
    write_json(out/'SUMMARY.json', summary)
    lines = ['# Planar GHZ verification', '', f"Status: **{summary['status']}**", '',
             f"Revision: `{summary['git_commit']}`", '', f"Scientific groups: {summary['scientific_groups']}", '',
             '| Suite | Groups | Reference byte-identical | Changed float fields |', '|---|---:|---|---:|']
    for row in summary['suites']:
        lines.append(f"| {row['name']} | {row['groups']} | {row['byte_identical']} | {row['changed_fields']} |")
    if 'error' in summary:
        lines.extend(['', 'Error: '+summary['error']])
    lines.extend(['', 'Finite checks and source preservation are not independent proof review or a priority certificate.', ''])
    (out/'SUMMARY.md').write_text('\n'.join(lines))
    return 0 if summary['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
