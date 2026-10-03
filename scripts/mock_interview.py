"""Offline one-question-at-a-time mock practice with HUMAN self-scoring."""
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--round',type=int,default=1,choices=range(1,11))
    parser.add_argument('--start',type=int,default=1,choices=range(1,21))
    args=parser.parse_args()
    rounds=json.loads((ROOT/'data/mock_interviews.json').read_text())
    selected=rounds[args.round-1]
    print('Round:',selected['title'],'— answers remain hidden until you respond.')
    for case in selected['questions'][args.start-1:]:
        print('\n'+case['id']+': '+case['question'])
        try:
            response=input('Your answer (or /quit): ').strip()
        except (EOFError,KeyboardInterrupt):
            print('\nSession ended.')
            break
        if response=='/quit':
            break
        if not response:
            print('Skipped; answer not revealed.')
            continue
        print('\nExpected points:',case['answer'])
        print('Deep technical detail:',case['technical'])
        print('Follow-up:',case['followup'])
        print('Self-review each point from 0 to 4; no automatic semantic score is claimed:')
        for point in case['rubric']:
            print(' -',point)
        print('Read:',case['chapter'])
if __name__=='__main__':
    main()
