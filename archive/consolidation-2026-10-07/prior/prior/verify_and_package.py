"""Verify actual records and package this bounded follow-up without overwrites."""
from pathlib import Path
import hashlib,json,os,subprocess,sys,zipfile,shutil
R=Path(__file__).resolve().parent
OUT=Path('/mnt/data/planar_ghz_bell_audit_2026-10-07.zip')
NOTE=Path('/mnt/data/planar_ghz_bell_audit_2026-10-07.md')
if OUT.exists() or NOTE.exists():raise FileExistsError('Refusing to overwrite delivered evidence')
sha=lambda data:hashlib.sha256(data).hexdigest()
original=Path('/mnt/data/fresh_planar_bell_scout_2026-10-07.zip')
assert sha(original.read_bytes())=='d475669e842683b811187053a06be68cb93f0a5845f9c0a711b85943e6451abc'
with zipfile.ZipFile(original) as z:
    assert z.testzip() is None
    members=[i for i in z.infolist() if not i.is_dir()]
    assert len(members)==12
    for item in members:
        assert (R/'prior'/item.filename).read_bytes()==z.read(item.filename),item.filename
manifest=json.loads((R/'prior/MANIFEST.json').read_text());assert len(manifest)==11
for name,metadata in manifest.items():
    data=(R/'prior'/name).read_bytes()
    assert sha(data)==metadata['sha256'] and len(data)==metadata['bytes'],name
assert (R/'prior/SCOUT.md').read_bytes()==Path('/mnt/data/fresh_planar_bell_scout_2026-10-07.md').read_bytes()
for name in ('final','repeat'):
    report=json.loads((R/'evidence'/f'{name}.json').read_text())
    assert report['status']=='PASS' and report['tests_run']==5
assert (R/'evidence/final.json').read_bytes()==(R/'evidence/repeat.json').read_bytes()
old=json.loads((R/'evidence/prior-rerun.json').read_text())
assert old['status']=='PASS' and old['tests_run']==5
assert (R/'evidence/prior-rerun.json').read_bytes()==(R/'prior/evidence/repeat.json').read_bytes()
failed=json.loads((R/'evidence/first.json').read_text())
assert failed['status']=='FAIL' and failed['tests_run']==5
out=R/'evidence/repeat.json';before=sha(out.read_bytes())
proc=subprocess.run([sys.executable,str(R/'check_audit_and_rate.py'),'--output',str(out)],capture_output=True,text=True,
 env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','TERM':'dumb'})
assert proc.returncode==2 and sha(out.read_bytes())==before
(R/'evidence/output_refusal.log').write_text(proc.stdout+proc.stderr)
record={'date':'2026-10-07','task':'Planar GHZ proof/prior-art audit with exact asymptotic full-correlation amplification law',
 'decision':'Retain the unified bounded result; resolve the missing latest source comparison before repository or manuscript promotion.',
 'prior_archive_sha256':sha(original.read_bytes()),'prior_archive_members_preserved':12,'prior_manifest_entries_verified':11,
 'prior_standalone_note_matches':True,'new_groups':5,'new_complete_final_runs':2,
 'new_reports_byte_identical':True,'new_final_report_sha256':sha((R/'evidence/final.json').read_bytes()),
 'old_groups_rerun':5,'old_report_byte_identical':True,
 'prior_rerun_sha256':sha((R/'evidence/prior-rerun.json').read_bytes()),
 'first_run':'Four groups passed, one failed on SLSQP success status under squared-norm constraints.',
 'repair':'Equivalent norm constraints and analytic Jacobian; remove exactly duplicate opposite signs; unchanged acceptance thresholds and full original squared-feasibility audit.',
 'optimizer_ftol':1e-12,'optimizer_maxiter':500,'objective_threshold':2e-8,'full_squared_feasibility_threshold':-2e-8,
 'optimizer_success_required':True,'tolerance_relaxed':False,'original_checker_changed':False,'prior_reports_refreshed':False,
 'output_refusal':{'returncode':2,'bytes_preserved':True},'largest_dense_quantum_dimension':32,
 'high_party_certification':'Exact rational scalar powers for N13,N16,N25; not a many-qubit numerical statevector.',
 'new_analytical_results':['All-state full-correlation upper bound nu^N with the prescribed planar family at every site.',
 'GHZ lower bound nu^N/2 matches the exact Nth-root rate nu.',
 'The constructed phase-adjusted GHZ is an exact maximal eigenstate of its own Bell operator.',
 'Necessary and sufficient party-count bounds have the same inverse-incompatibility-gap scaling for a fixed violation factor.',
 'Exact fixed-family margin and local-shrinkage controls.'],
 'not_claimed':['Smallest party count for any violation','All Bell expressions including marginals','New compatibility perimeter criterion',
 'Efficient experimental sampling','General biased/noncoplanar extension','Genuine N-party nonlocality','Exhaustive priority','Independent scientific review'],
 'source_access_gap':'Full text of Yoshino et al. arXiv2609.38836 remains unavailable; primary indexed abstract read.',
 'repositories_accessed_or_modified':False,'protected_project_material_used':False,'new_manuscript_or_contact':False}
(R/'RUN_RECORD.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
files={}
for p in sorted(R.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    name=p.relative_to(R).as_posix()
    assert p.suffix.lower() not in {'.pdf','.ttf','.otf','.woff','.woff2','.pyc'},name
    files[name]=p.read_bytes()
entries={name:{'sha256':sha(data),'bytes':len(data)}for name,data in files.items()}
with zipfile.ZipFile(OUT,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name,data in files.items():z.writestr(name,data)
    z.writestr('MANIFEST.json',json.dumps(entries,indent=2,sort_keys=True)+'\n')
with zipfile.ZipFile(OUT) as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))
    for name,meta in entries.items():
        data=z.read(name);assert sha(data)==meta['sha256'] and len(data)==meta['bytes'],name
shutil.copyfile(R/'AUDIT_AND_RATE.md',NOTE)
print(json.dumps({'archive':str(OUT),'note':str(NOTE),'archive_bytes':OUT.stat().st_size,
 'archive_sha256':sha(OUT.read_bytes()),'members':len(files)+1,'member_hashes_verified':True,
 'new_groups_passed_twice':5,'prior_groups_reproduced':5,'prior_members_unchanged':12},indent=2))
