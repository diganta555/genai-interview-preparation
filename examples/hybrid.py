from examples.core import rrf
if __name__ == '__main__':
    lexical = ['exact-invoice','policy','overview']
    dense_fixture = ['policy','overview','exact-invoice']
    print('Fusion of two fixture rankings:',rrf([lexical,dense_fixture]))
