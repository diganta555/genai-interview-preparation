def estimate(qps, service_seconds, docs, chunks_per_doc, dimensions):
    if min(qps,service_seconds,docs,chunks_per_doc,dimensions)<0:
        raise ValueError('negative workload')
    return {'in_flight_mean':qps*service_seconds,
            'vectors':docs*chunks_per_doc,
            'raw_float32_GB':docs*chunks_per_doc*dimensions*4/1e9}
if __name__ == '__main__':
    print(estimate(100,5,500000,20,768))
    print('Exclude replicas, metadata, index overhead, headroom, and cache from this lower bound.')
