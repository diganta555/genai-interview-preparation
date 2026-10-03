from examples.core import cache_key, Identity
ROUTES={'classification':'small-model-config','complex-synthesis':'large-model-config'}
def route(task):
    if task not in ROUTES:
        raise ValueError('unsupported task')
    return ROUTES[task]
if __name__ == '__main__':
    print(route('classification'))
    print(cache_key(Identity('demo','reader'),'refund','index-v1','prompt-v1',route('classification'),'acl-v1'))
    print('Static route demo. No real model quality or savings measured.')
