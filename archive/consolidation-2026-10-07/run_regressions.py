"""Rerun the three unchanged planar-GHZ suites, preserving all old outputs."""
from pathlib import Path
import hashlib,json,os,subprocess,sys,time
R=Path(__file__).resolve().parent
jobs=[('source_dictionary','prior/check_source_dictionary.py','prior/evidence/repeat.json',3),
      ('audit_rate','prior/prior/check_audit_and_rate.py','prior/prior/evidence/repeat.json',5),
      ('initial_scout','prior/prior/prior/check_planar_bell.py','prior/prior/prior/evidence/repeat.json',5)]
env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','PYTHONDONTWRITEBYTECODE':'1','TERM':'dumb'}
record=[]
for name,script,reference,count in jobs:
    out=R/'evidence'/f'{name}_rerun.json';log=R/'evidence'/f'{name}_rerun.log'
    assert not out.exists() and not log.exists()
    t=time.monotonic()
    with log.open('x')as f:
        p=subprocess.run([sys.executable,str(R/script),'--output',str(out)],env=env,cwd=R,stdout=f,stderr=subprocess.STDOUT,timeout=40)
    d=json.loads(out.read_text())
    assert p.returncode==0 and d['status']=='PASS'and d['tests_run']==count
    same=out.read_bytes()==(R/reference).read_bytes()
    record.append(dict(suite=name,groups=count,report=str(out.relative_to(R)),reference=reference,
                       byte_identical_to_reference=same,elapsed_seconds=time.monotonic()-t,
                       sha256=hashlib.sha256(out.read_bytes()).hexdigest()))
(R/'evidence/REGRESSIONS.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
