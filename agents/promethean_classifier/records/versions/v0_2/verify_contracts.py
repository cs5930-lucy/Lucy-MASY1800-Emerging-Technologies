"""Check every declared structural constraint used by these simple frozen schemas."""
from pathlib import Path
import json,subprocess
root=Path(__file__).resolve().parents[3];a=root/'agents/promethean_classifier'
def check(v,s,path='$'):
 t=s.get('type');types={'object':dict,'array':list,'string':str}
 if t: assert isinstance(v,types[t]),path
 if t=='object':
  assert all(k in v for k in s.get('required',[])),path+' required fields'
  props=s.get('properties',{})
  if s.get('additionalProperties') is False: assert set(v)<=set(props),path+' extra fields'
  for k,w in v.items():
   if k in props:check(w,props[k],path+'.'+k)
 if t=='array':
  for i,w in enumerate(v):check(w,s['items'],path+f'[{i}]')
report=[]
for f in sorted((a/'responses').glob('*.json')):
 result=subprocess.run(['python',str(root/'tools/validate_response.py'),str(f)],capture_output=True,text=True,check=True)
 check(json.loads(f.read_text()),json.loads((root/'core/output_schema.json').read_text()))
 report.append(f.name+': '+result.stdout.strip()+'; declared schema constraints passed')
for f in (a/'cases').glob('*.json'):check(json.loads(f.read_text()),json.loads((root/'core/input_schema.json').read_text()))
r=[json.loads((a/f'responses/v0_2_{n}.json').read_text()) for n in ['primary','contrast_1','contrast_2']]
assert len({x['general_et_finding'] for x in r})==1
assert 'Defer' in r[1]['recommendation_management_implication']
assert 'Reject' in r[2]['recommendation_management_implication']
assert 'Abstain' in json.loads((a/'responses/v0_2_insufficient_evidence.json').read_text())['general_et_finding']
report+=['Four input cases pass declared schema constraints.','Broad finding stable across three same-technology cases.','Safety deferral, hype refusal and evidence abstention checks passed.']
r=subprocess.run(['python',str(root/'tools/check_frozen_core.py')],capture_output=True,text=True,check=True);report.append(r.stdout.strip())
report.append('Checks inspect saved representative responses, not statistical repeatability or application effectiveness.')
(a/'records/validation.txt').write_text('\n'.join(report)+'\n');print('\n'.join(report))
