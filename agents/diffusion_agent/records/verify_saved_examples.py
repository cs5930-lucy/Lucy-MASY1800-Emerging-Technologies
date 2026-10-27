"""Validate saved artifacts, not model repeatability or application performance."""
from pathlib import Path
import json,subprocess,hashlib
r=Path(__file__).resolve().parents[3];a=r/'agents/diffusion_agent'
def validate(v,s,path='$'):
 types={'object':dict,'array':list,'string':str};t=s.get('type')
 if t:assert isinstance(v,types[t]),path+' type'
 if t=='object':
  assert set(s.get('required',[]))<=set(v),path+' required'
  props=s.get('properties',{})
  if s.get('additionalProperties') is False:assert set(v)<=set(props),path+' unexpected'
  for k,w in v.items():
   if k in props:validate(w,props[k],path+'.'+k)
 if t=='array':
  for i,w in enumerate(v):validate(w,s['items'],path+f'[{i}]')
report=[]
for f in sorted((a/'responses').glob('*.json')):
 subprocess.run(['python',str(r/'tools/validate_response.py'),str(f)],check=True,capture_output=True,text=True)
 validate(json.loads(f.read_text()),json.loads((r/'core/output_schema.json').read_text()))
 report.append(f.name+': supplied basic validator and all declared structural constraints passed')
for f in (a/'cases').glob('*.json'):validate(json.loads(f.read_text()),json.loads((r/'core/input_schema.json').read_text()))
get=lambda n:json.loads((a/f'cases/{n}.json').read_text())
p=get('primary')
for n,expected in [('contrast_1',{'adoption_posture'}),('contrast_2',{'adoption_posture'}),('denominator_hype',{'additional_context'}),('application_contrast',{'intended_application','risk_consequence_context'})]:
 c=get(n);actual={k for k in p if p[k]!=c[k]};assert actual==expected,(n,actual)
report.append('Input isolation passed for aggressive, conservative, application and hype contrasts.')
for f in sorted((a/'responses').glob('v0_2_*.json')):
 data=json.loads(f.read_text())
 for term in ['relative advantage','compatibility','complexity','trialability','observability']:assert term in data['application_finding'].lower(),(f.name,term)
report.append('All five factors are present in every revised response; semantic quality is manually assessed.')
for f in sorted((a/'records/prompts').glob('*.txt')):report.append(f.name+' SHA256 '+hashlib.sha256(f.read_bytes()).hexdigest())
z=subprocess.run(['python',str(r/'tools/check_frozen_core.py')],capture_output=True,text=True,check=True);report.append(z.stdout.strip())
report.append('Saved outputs are same-conversation analytical examples; no blind execution, repeated-run robustness, Canva integration or measured saving is claimed.')
(a/'records/validation.txt').write_text('\n'.join(report)+'\n');print('\n'.join(report))
