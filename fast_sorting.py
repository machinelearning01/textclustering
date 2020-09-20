import time
import numpy as np
import bottleneck as bn
import pandas as pd
import heapq

def bottleneck_1(a, n):
    return -bn.partition(-a, n)[:n]

def bottleneck_2(a, n):
    return bn.partition(a, a.size-n)[-n:]

def numpy(a, n):
    return a[a.argsort()[-n:]]

def numpy_2(a, n):
    M = a.shape[0]
    perc = (np.arange(M-n,M)+1.0)/M*100
    return np.percentile(a,perc)

def pandas(a, n):
    return pd.Series(a).nlargest(n)

def hpq(a, n):
    return heapq.nlargest(n, a)

def do_nothing(a, n):
    return a[:n]

def benchmark(func, a, ntimes=1):
    print("->", len(a))
    topn = len(a)
    t1 = time.time()
    # for n in range(ntimes):
    res = func(a, topn)
    print(res)
    t2 = time.time()
    ms_per_loop = (t2 - t1)
    return ms_per_loop

a = np.random.rand(10000)
print(a)
t0 = benchmark(do_nothing, a)
print("did nothing--------")
# t1 = benchmark(bottleneck_1, a)
# print("bottleneck 1: {:05.2f} ms per loop".format(t1 - t0))
# t2 = benchmark(bottleneck_2, a)
# print("bottleneck 2: {:05.2f} ms per loop".format(t2 - t0))
t3 = benchmark(pandas, a)
print("pandas      : {:05.2f} ms per loop".format(t3 - t0))
# t4 = benchmark(hpq, a)
# print("heapq       : {:05.2f} ms per loop".format(t4 - t0))
t5 = benchmark(numpy, a)
print("numpy       : {:05.2f} ms per loop".format(t5 - t0))
# t6 = benchmark(numpy_2, a)
# print("numpy 2     : {:05.2f} ms per loop".format(t6 - t0))