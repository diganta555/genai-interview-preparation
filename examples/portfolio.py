from examples.evaluate import run
if __name__ == '__main__':
    results=run()
    print('Measured on synthetic offline cases:',len(results))
    print('Abstention expectation passes:',sum(x['abstention_pass'] for x in results))
    print('No live-model semantic or production-readiness claim is made.')
