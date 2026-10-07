from pathlib import Path
import hashlib,json,zipfile,shutil
R=Path(__file__).resolve().parent
OUT=Path('/mnt/data/fresh_planar_bell_scout_2026-10-07.zip')
NOTE=Path('/mnt/data/fresh_planar_bell_scout_2026-10-07.md')
if OUT.exists()or NOTE.exists():raise FileExistsError('Refuse to overwrite delivered evidence.')
sha=lambda data:hashlib.sha256(data).hexdigest()
record=json.loads((R/'RUN_RECORD.json').read_text())
for name,meta in record['context_inputs'].items():
 p=Path('/mnt/data/merlin_arthur_after_pmc_2026-10-07')/name
 assert sha(p.read_bytes())==meta['sha256']and p.stat().st_size==meta['bytes']
assert (R/'evidence/first.json').read_bytes()==(R/'evidence/repeat.json').read_bytes()
assert sha((R/'check_planar_bell.py').read_bytes())==record['script_sha256']
files={p.relative_to(R).as_posix():p.read_bytes()for p in sorted(R.rglob('*'))if p.is_file()and '__pycache__'not in p.parts}
assert all(Path(n).suffix.lower()not in {'.pdf','.ttf','.otf','.woff','.woff2','.pyc'}for n in files)
manifest={n:{'sha256':sha(b),'bytes':len(b)}for n,b in files.items()}
with zipfile.ZipFile(OUT,'x',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
 for n,b in files.items():z.writestr(n,b)
 z.writestr('MANIFEST.json',json.dumps(manifest,indent=2,sort_keys=True)+'\n')
with zipfile.ZipFile(OUT)as z:
 assert z.testzip()is None and len(z.namelist())==len(set(z.namelist()))
 for n,m in manifest.items():
  b=z.read(n);assert len(b)==m['bytes']and sha(b)==m['sha256']
shutil.copyfile(R/'SCOUT.md',NOTE)
print(json.dumps({'archive':str(OUT),'note':str(NOTE),'archive_sha256':sha(OUT.read_bytes()),'members':len(files)+1,'bytes':OUT.stat().st_size,'all_hashes_verified':True},indent=2))
