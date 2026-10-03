import json, time, uuid
from contextlib import contextmanager
@contextmanager
def span(request_id,stage):
    start=time.perf_counter()
    status='ok'
    try:
        yield
    except Exception:
        status='error'
        raise
    finally:
        print(json.dumps({'request_id':request_id,'stage':stage,'status':status,
                          'duration_ms':(time.perf_counter()-start)*1000}))
if __name__ == '__main__':
    request_id=str(uuid.uuid4())
    with span(request_id,'request'):
        with span(request_id,'retrieval'):
            time.sleep(0.005)
        with span(request_id,'model-fixture'):
            time.sleep(0.01)
