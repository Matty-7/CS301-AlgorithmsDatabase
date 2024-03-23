def fmt_num(n): return '%3s' % str(n)
import collections
import tabulate
class Stats:
    Dict = collections.defaultdict(lambda: 0)
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


def PrintArray(A):
    print(' '.join(map(fmt_num,A)))
    pass

