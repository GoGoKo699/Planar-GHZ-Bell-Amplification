"""Verify preservation/repeated reports and create a new, exclusive checkpoint."""
from pathlib import Path
import hashlib,json,os,platform,subprocess,sys,zipfile
import numpy,scipy
R=Path(__file__).resolve().parent
BASE=R.parent
previous=BASE/'planar_ghz_source_comparison_2026-10-07.zip'
pdf=BASE/'2609.38836v1.pdf'
out=BASE/'planar_ghz_consolidation_2026-10-07.zip'
sha=lambda b:hashlib.sha256(b).hexdigest()
assert not out.exists()
assert sha(previous.read_bytes())=='47d2bd25137347aec2b5d0446d1cc705e8e5671c2e825274c833c5bff3acfd07'
assert sha(pdf.read_bytes())=='1181693ddd202f90eff59ebfc13f556e00bf472037e401ae9de2fd5f1c67eb88'
with zipfile.ZipFile(previous)as z:
    assert z.testzip()is None
    members=[i for i in z.infolist()if not i.is_dir()]
    assert len(members)==54
    for i in members:assert (R/'prior'/i.filename).read_bytes()==z.read(i.filename),i.filename
m=json.loads((R/'prior/MANIFEST.json').read_text())
for name,rec in m.items():
    b=(R/'prior'/name).read_bytes();assert len(b)==rec['bytes']and sha(b)==rec['sha256'],name
assert (R/'prior/SOURCE_COMPARISON.md').read_bytes()==(BASE/'planar_ghz_source_comparison_2026-10-07.md').read_bytes()
assert (R/'prior/CONTRIBUTION_BRIEF.md').read_bytes()==(BASE/'planar_ghz_source_comparison_2026-10-07/CONTRIBUTION_BRIEF.md').read_bytes()
final=R/'evidence/final.json';repeat=R/'evidence/repeat.json'
assert final.read_bytes()==repeat.read_bytes()
d=json.loads(final.read_text());assert d['status']=='PASS'and d['tests_run']==5
reg=json.loads((R/'evidence/REGRESSIONS.json').read_text());assert sum(x['groups']for x in reg)==13
for row in reg:
    assert (R/row['report']).read_bytes()==(R/row['reference']).read_bytes()
# Refusal must leave the existing report unchanged and not pretend to run tests.
before=sha(repeat.read_bytes())
p=subprocess.run([sys.executable,str(R/'check_consolidation.py'),'--output',str(repeat)],capture_output=True,text=True,
                 env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','PYTHONDONTWRITEBYTECODE':'1','TERM':'dumb'})
assert p.returncode==2 and sha(repeat.read_bytes())==before
(R/'evidence/output_refusal.log').write_text(p.stdout+p.stderr)
# No unclosed math environments or stale duplicate variable from the earlier note.
text=(R/'THEOREM.md').read_text()
assert text.count('$$')%2==0 and 'u=u='not in text
assert r'u=\sum_xc_x\bar z_x=\frac12\sum_i\|k_i\|=\nu' in text
sources={
 'reading_date':'2026-10-07',
 'uploaded_primary':{'title':'Joint measurability of coplanar POVMs','version':'arXiv:2609.38836v1',
                    'sha256':sha(pdf.read_bytes()),
                    'used':'Fully supplied parsed content, main theorem and explicit X/Y certificate; earlier complete visual/dictionary audit retained, not recounted as a new visual audit.'},
 'primary_reads':[
  {'id':'PGQ25','url':'https://arxiv.org/pdf/2403.10564v4',
   'passages':'Theorem3; p2 all-but-one compatibility locality; Corollary6; Discussion pp4-5; AppendixB construction and AppendixD conclusion.',
   'use':'General existence and noise-threshold convergence are inherited; the stated GHZ/party-count question and resource scope are checked. Standard all-but-one compatibility justifies the refined bound.',
   'limits':'Not an independent reproduction of every cone-map theorem cited by the source.'},
  {'id':'WW01','url':'https://arxiv.org/pdf/quant-ph/0102024',
   'passages':'SectionVD GHZ-extreme-correlation construction and SectionVII two-setting restriction.',
   'use':'Distinguish standard GHZ/equatorial algebra from the arbitrary fixed-family constructive implication.',
   'limits':'Not a claim that the source solves the many-setting theorem or that our finite-N beta is globally optimal.'},
  {'id':'LN22','url':'https://arxiv.org/pdf/2205.12668',
   'passages':'Theorems8.1-8.2, pp24-25, and their fixed-Alice bipartite scope.',
   'use':'Attribution for compatibility-norm upper-bound method.',
   'limits':'No graph/table data used.'},
  {'id':'DVP24','url':'https://arxiv.org/pdf/2310.20677',
   'passages':'Equations6-8, regular-polygon observables and GHZ full-correlation tensor; scope discussion.',
   'use':'Strong symmetric-case predecessor; no claimed numerical superiority.',
   'limits':'No unviewed numerical table/plot value used.'}
 ],
 'search_limits':'Several broad keyword/domain searches returned largely irrelevant results. No absence-of-hits priority argument is made; unrelated results and secondary generated summaries are not technical evidence.',
 'failed_visual_requests':['PGQ25 page2 cache miss','PGQ25 page5 cache miss','WW01 page8 cache miss'],
 'visual_claims':'No newly rendered primary-paper figure or table was successfully inspected in this pass; the current arguments use parsed mathematical text.',
 'new_derivations':'N-1 parent converse refinement; exact finite-margin exclusion from the refined bound; explicit CHSH canonical-GHZ scope control and full-behavior parity-twirl check. These are applications/clarifications, not claimed independent discoveries.',
 'independent_review':False,'exhaustive_priority':False,'protected_projects_accessed':False,
 'unrelated_electronic_decoherence_pdf_used':False
}
(R/'SOURCES.json').write_text(json.dumps(sources,indent=2)+'\n')
(R/'environment.json').write_text(json.dumps(dict(python=sys.version,platform=platform.platform(),numpy=numpy.__version__,scipy=scipy.__version__,blas_threads=1),indent=2)+'\n')
record={
 'stage':'Consolidate one planar-GHZ Bell theorem, sharpen finite-party upper bound, and freeze scope for author review.',
 'main_theorem':'nu^N/2 <= R_N_GHZ <= R_N <= r*nu^(N-1) <= nu^N; Nth-root limits equal nu.',
 'prior_exponent_changed':False,'prior_geometric_attribution_preserved':True,
 'new_final_groups':5,'new_complete_runs':2,'new_reports_byte_identical':True,
 'new_report_sha256':sha(final.read_bytes()),'largest_new_quantum_matrix_dimension':16,
 'previous_suites':reg,'previous_groups_rerun':13,
 'previous_archive_members_unchanged':54,'previous_manifest_entries_verified':len(m),
 'uploaded_pdf_unchanged':True,'source_pdf_redistributed':False,
 'initial_execution':'Timed out at45s during an expensive Python-loop deterministic local-bound calculation; no scientific assertion failure or complete report. Initial script and partial log preserved.',
 'repair':'Identical absolute maximum evaluated by vectorized sign contractions; smaller full-enumeration controls verify equivalence. Measurement families, objective, assertions and tolerances retained.',
 'overwritten_reports':False,'refusal_exit_status':p.returncode,
 'decision':'Retain bounded theoretical project; recommend a separate versioned repository only after owner destination/authorization; no further model expansion required for current contribution review.',
 'repository_created_or_accessed':False,'external_contact':False,'manuscript_submission':False,
 'not_claimed':['Optimal finite N','Optimal beta at each N','Arbitrary marginal-containing Bell bounds','General biased or noncoplanar measurements','Genuine multipartite nonlocality','Efficient experimental statistics','Exhaustive priority','Independent review']
}
(R/'RUN_RECORD.json').write_text(json.dumps(record,indent=2)+'\n')
(R/'evidence/PRESERVATION.txt').write_text('PASS:54 prior archive members and53 manifest entries unchanged; supplied PDF hash unchanged;5 final groups repeated exactly; previous3+5+5 reports reproduced exactly; output refusal leaves evidence unchanged.\n')
files={}
for path in sorted(R.rglob('*')):
    if not path.is_file()or'__pycache__'in path.parts:continue
    rel=path.relative_to(R).as_posix()
    assert path.suffix.lower() not in {'.pdf','.ttf','.otf','.woff','.woff2','.pyc'}
    files[rel]=path.read_bytes()
manifest={name:dict(bytes=len(b),sha256=sha(b))for name,b in files.items()}
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
    for name,b in files.items():z.writestr(name,b)
    z.writestr('MANIFEST.json',json.dumps(manifest,indent=2,sort_keys=True)+'\n')
with zipfile.ZipFile(out)as z:
    assert z.testzip()is None and len(z.namelist())==len(set(z.namelist()))
    for name,rec in manifest.items():
        b=z.read(name);assert len(b)==rec['bytes']and sha(b)==rec['sha256']
summary=dict(archive=str(out),archive_sha256=sha(out.read_bytes()),bytes=out.stat().st_size,members=len(files)+1,
             theorem=str(R/'THEOREM.md'),assessment=str(R/'ASSESSMENT.md'),all_archive_hashes_verified=True)
(R/'PACKAGE_VERIFICATION.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
