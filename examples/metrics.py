from examples.core import classification_metrics
if __name__ == '__main__':
    print('Always benign:', classification_metrics(0, 0, 10, 990))
    print('Attack detector:', classification_metrics(8, 12, 2, 978))
