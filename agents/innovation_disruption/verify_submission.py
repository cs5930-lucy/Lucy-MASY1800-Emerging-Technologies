#!/usr/bin/env python3
"""Standard-library checks for the saved submission. Does not call a model."""
from pathlib import Path
import json, subprocess, sys, hashlib, tempfile
A=Path(__file__).resolve().parent
R=A.parents[1]
def check_schema(value,schema,path='$'):
 errors=[];typ=schema.get('type')
 kinds={'object':dict,'array':list,'string':str}
 if typ in kinds and not isinstance(value,kinds[typ]):return [f'{path}: expected {typ}']
 if typ=='object':
  props=schema.get('properties',{})
  for key in schema.get('required',[]):
   if key not in value:errors.append(f'{path}: missing {key}')
  if schema.get('additionalProperties') is False:
   for key in value.keys()-props.keys():errors.append(f'{path}: unexpected {key}')
  for key,s in props.items():
   if key in value:errors.extend(check_schema(value[key],s,path+'.'+key))
 if typ=='array':
  for i,v in enumerate(value):errors.extend(check_schema(v,schema.get('items',{}),f'{path}[{i}]'))
 return errors
errors=[]
p=subprocess.run([sys.executable,str(R/'tools/check_frozen_core.py')],capture_output=True,text=True)
print(p.stdout.strip());errors += [] if p.returncode==0 else [p.stdout+p.stderr]
for folder,schema_path in [('cases','input_schema.json'),('responses','output_schema.json')]:
 schema=json.loads((R/'core'/schema_path).read_text())
 for file in sorted((A/folder).glob('*.json')):
  e=check_schema(json.loads(file.read_text()),schema)
  print(('FAIL' if e else 'PASS')+' schema '+str(file.relative_to(A)));errors.extend(e)
  if folder=='responses':
   r=subprocess.run([sys.executable,str(R/'tools/validate_response.py'),str(file)],capture_output=True,text=True)
   if r.returncode:errors.append(r.stdout+r.stderr)
m=json.loads((A/'records/run_manifest.json').read_text())
for run in m['runs']:
 for kind in ['prompt','response']:
  if hashlib.sha256((A/run[kind]).read_bytes()).hexdigest()!=run[kind+'_sha256']:errors.append(f"Changed {kind}: {run['case']}")
 with tempfile.TemporaryDirectory() as temp:
  out=Path(temp)/'packet.txt'
  subprocess.run([sys.executable,str(R/'tools/build_prompt.py'),'--agent',str(A),'--case',str(A/f"cases/{run['case']}.json"),'--out',str(out)],check=True,capture_output=True)
  if out.read_bytes()!=(A/run['prompt']).read_bytes():errors.append('Prompt not reproducible: '+run['case'])
print('PASS prompt reproducibility and recorded hashes' if not errors else 'Inspect errors below')
cases=[json.loads((A/f'cases/{c}.json').read_text()) for c in ['primary','contrast_1','contrast_2']]
for key in ['emerging_technology','intended_application','time_horizon','adoption_posture']:
 if len({c[key] for c in cases})!=1:errors.append('Unexpected uncontrolled context change: '+key)
print('PASS controlled comparison inputs' if not errors else 'Input or other errors found')
for e in errors:print('ERROR',e)
print('Overall: '+('PASS' if not errors else 'FAIL'))
print('These checks verify structure, integrity and reproducibility, not factual truth or model reliability.')
sys.exit(bool(errors))
