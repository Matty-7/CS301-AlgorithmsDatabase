#
# Created by Jiang Long 
#
# DKU CS301 FALL 2021 SESSION 02
#

def fmt_num(n): return '%3s' % str(n)
import collections
import tabulate
class Stats:
    Dict = collections.defaultdict(int)
    pass


def Reset():
    Stats.Dict = collections.defaultdict(int)
    pass

def Inc(key, val=1):
    Stats.Dict[key] = Stats.Dict[key]  +val
    pass
def Set(key, val):
    Stats.Dict[key] =val
    pass

def PrintStats():
    print()
    hx = ['Run stats' ,'Count']
    tx = [ [i,j] for i,j in sorted(Stats.Dict.items())]
    print(tabulate.tabulate(tx,hx, tablefmt = 'presto'))
    print()
    pass


def PrintArray(A, tag = None):
    t = '' if tag is None else '%22s: '% tag
    print(t + ' '.join(map(fmt_num,A)))
    pass

