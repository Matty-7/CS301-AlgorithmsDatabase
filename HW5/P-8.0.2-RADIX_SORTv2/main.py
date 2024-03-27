#
# Created by Jiang Long 
#
# DKU CS301 FALL 2021 SESSION 02
#

import sys,os, importlib
import rIO
import RADIX_SORTv2


                          
ax = sys.stdin.read().split()

A = list(map(int, ax))

RADIX_SORTv2.main(A,4,3)

print()
print()
RADIX_SORTv2.main(A,2,6)


