"""Validate local links, required modules, bank counts, and mock prompt structure."""
import json
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
def main():
    errors=[]
    for path in ROOT.rglob('*.md'):
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',path.read_text()):
            if target.startswith(('http:','https:','#','mailto:')): continue
            local=target.split('#',1)[0]
            if local and not (path.parent/local).exists():
                errors.append(f'{path.relative_to(ROOT)}: {target}')
    modules=[p for p in ROOT.iterdir() if p.is_dir() and re.match(r'\d\d-',p.name) and p.name!='00-roadmap']
    if len(modules)!=30: errors.append(f'Module count: {len(modules)}')
    counts={p.name:len(re.findall(r'^## Question ',p.read_text(),re.M)) for p in (ROOT/'interview-questions').glob('top-*.md')}
    if sum(counts.values())!=530: errors.append(f'Question count: {counts}')
    mocks=json.loads((ROOT/'data/mock_interviews.json').read_text())
    if len(mocks)!=10 or any(len(r['questions'])!=20 for r in mocks): errors.append('Invalid mock structure')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('OK: 30 modules; 530 bank entries; 200 mock questions; all local Markdown links resolve.')
if __name__=='__main__': main()
