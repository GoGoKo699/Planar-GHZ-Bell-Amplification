#!/usr/bin/env python3
"""Generate and check the portable reading view of the protected theorem."""
from __future__ import annotations
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MATH = re.compile(r'^```math\n(.*?)^```\s*$|^\$\$\s*\n(.*?)^\$\$\s*$', re.M | re.S)


def theorem_view(root: Path = ROOT) -> str:
    text = (root/'research/THEOREM.md').read_text()
    text = text.replace(r'\operatorname{', r'\mathrm{')
    opened = False
    lines = []
    for line in text.splitlines():
        if line == '$$':
            lines.append('```' if opened else '```math')
            opened = not opened
        else:
            lines.append(line)
    if opened:
        raise ValueError('Unclosed display math in protected source')
    return '\n'.join(lines).rstrip() + '\n\n' + (
        'The preserved [scientific source](../research/THEOREM.md) defines this theorem.\n')


def check(root: Path = ROOT) -> dict:
    if (root/'docs/THEOREM.md').read_text() != theorem_view(root):
        raise ValueError('The theorem reading view is stale; run python tools/render_docs.py')
    paths = list(root.glob('*.md')) + list((root/'research').glob('*.md'))
    paths += list((root/'literature').glob('*.md')) + list((root/'docs').rglob('*.md'))
    protected = {root/'research/THEOREM.md', root/'research/ASSESSMENT.md'}
    blocks = 0
    for path in paths:
        if path in protected:
            continue
        for match in MATH.finditer(path.read_text()):
            blocks += 1
            if r'\operatorname' in match.group():
                raise ValueError(f'Unsupported math macro in {path.relative_to(root)}')
    return {'theorem_view_matches_source': True, 'math_blocks_checked': blocks}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check without rewriting files')
    args = parser.parse_args()
    if not args.check:
        (ROOT/'docs/THEOREM.md').write_text(theorem_view())
    print(check())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
