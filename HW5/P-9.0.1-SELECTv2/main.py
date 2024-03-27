import sys,os, importlib, random
import rIO

import SELECTv2

                          
ax = sys.stdin.read().split()

A, ax = rIO.readArray(ax)


random.seed(len(A))
B = list(sorted(A))
for i in range(len(A)):
    # do a random order stats
    k = i # random.randint(0, len(A))
    r = SELECTv2.main(A, k)

    assert r == B[k]
    pass

