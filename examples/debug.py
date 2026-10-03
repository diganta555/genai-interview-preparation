from examples.trace import span
import time
if __name__ == '__main__':
    with span('synthetic-incident','request'):
        with span('synthetic-incident','queue'):
            time.sleep(0.03)
        with span('synthetic-incident','model-fixture'):
            time.sleep(0.005)
