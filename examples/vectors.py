from examples.core import cosine
if __name__ == '__main__':
    for other in ([1.0,0.0],[0.0,1.0],[-1.0,0.0]):
        print(other, cosine([1.0,0.0],other))
