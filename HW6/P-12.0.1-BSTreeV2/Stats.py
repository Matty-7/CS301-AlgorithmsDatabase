# Created by Jiang Long 
# 
# DKU CS301 FALL 2021 SESSION 01
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
    t = '' if tag is None else '%s: '% tag
    print(t + ' '.join(map(fmt_num,A)))
    pass


def PrintMatrix(A, title = None, row_tag = None):
    t = '' if title is None else '%s: '% title
    if row_tag == None:row_tag = 'row'
    if not title is None: print (t)
    #print(t + ' '.join(map(fmt_num,A)))
    for j, i in enumerate(A):
        PrintArray(i, '  %s %d'% (row_tag, j))
        pass
    pass

