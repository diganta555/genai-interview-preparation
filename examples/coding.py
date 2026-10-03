from examples.core import chunks, cosine, retrieval_metrics
if __name__ == '__main__':
    print(chunks('abcdefghij',size=4,overlap=1))
    print(cosine([1,1],[1,0]))
    print(retrieval_metrics(['D2','D1'],{'D1'},2))
