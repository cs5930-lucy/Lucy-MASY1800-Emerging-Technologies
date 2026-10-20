"""Validate saved examples; does not execute an AI model or prove repeatability."""
from pathlib import Path
import json,subprocess,hashlib
root=Path(__file__).resolve().parents[3];a=root/'agents/promethean_classifier'
def check(v,s,path='$'):
 t=s.get('type');types={'object':dict,'array':list,'string':str}
 if t:assert isinstance(v,types[t]),path
 if t=='object':
  assert all(k in v for k in s.get('required',[])),path+' missing required'
  props=s.get('properties',{})
  if s.get('additionalProperties') is False:assert set(v)<=set(props),path+' unexpected fields'
  for k,w in v.items():
   if k in props:check(w,props[k],path+'.'+k)
 if t=='array':
  for i,w in enumerate(v):check(w,s['items'],path+f'[{i}]')
report=[]
for f in sorted((a/'responses').glob('*.json')):
 subprocess.run(['python',str(root/'tools/validate_response.py'),str(f)],capture_output=True,text=True,check=True)
 check(json.loads(f.read_text()),json.loads((root/'core/output_schema.json').read_text()))
 report.append(f.name+': basic and declared-schema constraints passed')
for f in (a/'cases').rglob('*.json'):check(json.loads(f.read_text()),json.loads((root/'core/input_schema.json').read_text()))
case=lambda n:json.loads((a/f'cases/v0_3/{n}.json').read_text())
primary=case('primary')
for n,want in [('posture_only',{'adoption_posture'}),('hype_only',{'additional_context'})]:
 other=case(n);assert {k for k in primary if primary[k]!=other[k]}==want
report.append('Input isolation passed: posture-only changes one field; hype-only changes one field.')
# Expected labels evaluate saved samples after generation. They are not supplied to the model packets.
for n in ['primary','safety','posture_only','hype_only']:
 response=json.loads((a/f'responses/v0_3_{n}.json').read_text())
 assert 'potentially promethean' in response['general_et_finding'].lower()
for n,label in [('unknown','abstain'),('incremental_control','incremental')]:
 assert label in json.loads((a/f'responses/v0_3_{n}.json').read_text())['general_et_finding'].lower()
report.append('Saved sample label checks passed; exact wording equality is not required.')
for n in ['primary','safety','posture_only','hype_only','unknown','incremental_control']:
 packet=a/f'records/prompts/v0_3_{n}.txt'
 report.append(n+' packet SHA256 '+hashlib.sha256(packet.read_bytes()).hexdigest())
r=subprocess.run(['python',str(root/'tools/check_frozen_core.py')],capture_output=True,text=True,check=True);report.append(r.stdout.strip())
report.append('Manual semantic findings and provenance are in revision_and_tests.md. No statistical robustness or application performance is claimed.')
(a/'records/validation.txt').write_text('\n'.join(report)+'\n');print('\n'.join(report))
