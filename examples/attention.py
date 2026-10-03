import math
def attention(q, keys, values, visible):
    if not 0 < visible <= len(keys) or len(keys) != len(values):
        raise ValueError('invalid visible count or shapes')
    logits = [sum(a*b for a,b in zip(q,k))/math.sqrt(len(q)) for k in keys[:visible]]
    shifted = [math.exp(x-max(logits)) for x in logits]
    weights = [x/sum(shifted) for x in shifted]
    return weights, [sum(w*v[j] for w,v in zip(weights,values[:visible]))
                     for j in range(len(values[0]))]
if __name__ == '__main__':
    q = [1.0, 0.0]
    keys = [[1.0,0.0],[0.0,1.0]]
    values = [[2.0,0.0],[0.0,4.0]]
    print('First-position causal:', attention(q,keys,values,1))
    print('Both positions:', attention(q,keys,values,2))
