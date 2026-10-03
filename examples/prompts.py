TASKS = {
    'support': 'Answer from the supplied policy. Cite source IDs. Escalate unsupported requests.',
    'document': 'Extract requested facts with source spans. Use null for missing values.',
    'sql': 'Return an allowed typed query plan. Do not execute or claim execution.',
    'coding': 'Propose code and meaningful tests. State assumptions and dependencies.',
    'summary': 'Summarize supported facts, preserving dates, units, negations, and uncertainty.',
    'classification': 'Choose exactly one allowed label; return unknown if no label applies.',
    'extraction': 'Return fields in the declared schema. Never invent absent values.',
}
def prompt(task, question, evidence):
    import json
    return {'version': 'v1', 'system': TASKS[task],
            'user': json.dumps({'question':question, 'untrusted_evidence':evidence})}
if __name__ == '__main__':
    print(prompt('support','Can I get a refund?',
                 [{'id':'P1','text':'Refunds within 14 days with receipt.'}]))
