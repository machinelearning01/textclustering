import numpy as np
import bottleneck as bn
import pandas as pd
from numpy import unravel_index
import math
import time as t

uttrs = [
    'a weeker person cannot become a king because he can be killed anytime',
    'reset my password',
    'reset my machine',
    'king can be killed anytime so we need make him strong',
    'our prince is as strong as rock',
    'your prince was as weak as feather'] * 1000
n=1400
mtrx = np.random.random((n,n))

def asort(a,l):
    t1 = t.time()
    r = np.arange(l)
    mask = r[:,None] > r
    inds=list(zip(*np.where(mask)))
    print("masked inds in - ", (t.time() - t1))
    t2 = t.time()
    idx = a[mask].argsort()[::-1]
    # print(idx)
    print("sorted in - ", (t.time() - t2))
    return idx, inds

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

def loop_short(mtrx):
    # print(mtrx)
    l = mtrx.shape[0]
    print(l)
    s, inds = asort(mtrx, l)
    clus = form_clusts(s, inds)

def form_clusts(s, inds):
    t1 = t.time()
    clusts={}
    for i in s:
        per = truncate(mtrx[inds[i]], 1)
        if per > 0.0:
            idx = list(inds[i]) # 0.5
            done = False
            for key, values in clusts.items():
                if idx[0] in values:
                    done = True
                    if key.split('_')[0] == str(per) and idx[1] not in values:
                        clusts[key].append(idx[1])
                    else:
                        break
                elif idx[1] in values:
                    done = True
                    if key.split('_')[0] == str(per) and idx[0] not in values:
                        clusts[key].append(idx[0])
                    else:
                        break
            if done == False:
                if per in clusts.keys():
                    mtchs = any(key.startswith(per).split('_')[1] for key in clusts)
                    clusts[per+'_'+int(max(mtchs))+1] = idx
                else:
                    clusts[str(per)+'_1'] = idx
    print("clusterd in - ", (t.time() - t1))
    return clusts
    # dict={}
    # for i in range(len(inds[0])):
    #     dict[str(inds[0][i]) + "," + str(inds[1][i])] = mtrx[inds[0][i]][inds[1][i]]
    # sorted_dict = sorted(dict.items(), reverse=True, key=lambda x: x[1])
    # ad = mtrx[inds]

    # t3 = t.time()
    # m = np.array(ad)
    # print("make it np array ", (t.time() - t3))
    # print(m)
    # m=np.tril(mtrx, k=-1)
    # mtrx[il1] = 0   # fastest way to assign 0 to triangle
    # rows, cols = np.nonzero(m)
    # new_m = m[rows,cols]
    # start = t.time()
    # sorted = bottleneck_2(m, len(m) - 1)
    # print("--sort time--", t.time()-start)
    # print(sorted)
    # dict={}
    # for i in range(len(m)):
    #     a=1
        # dict[str(rows[i])+","+str(cols[i])]= round(m[rows[i]][cols[i]], 8)
    # res = unravel_index(max_i, mtrx.shape)
    # sorted_dict = sorted(dict.items(), reverse=True, key=lambda x: x[1])
    # print(l, len(sorted_dict))

def bottleneck_2(a, n):
    return bn.partition(a, a.size-n)

# start = t.time()
# loop_mtrx(mtrx)
# print("--in seconds--", t.time()-start)

start = t.time()
loop_short(mtrx)
print("--in seconds--", t.time()-start)



def argsort1(mtrx):
    t1 = t.time()
    inds = np.tril_indices(len(mtrx[0]), k=-1)
    vals = mtrx[inds]
    argsort = vals.argsort()[::-1]
    print("sorted - ", (t.time() - t1))
    return argsort