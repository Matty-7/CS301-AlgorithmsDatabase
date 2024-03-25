def fmt_num(n): return '%3s' % str(n)
import collections
import tabulate
class Stats:
    Dict = collections.defaultdict(int)
    @staticmethod
    def Reset():
        Dict = collections.defaultdict(lambda i: 0)
        pass

    @staticmethod
    def Inc(key, val=1):
        Stats.Dict[key] = Stats.Dict[key]  +val
        pass
    pass

def PrintStats():
    print()
    hx = ['Run stats' ,'Count']
    tx = [ [i,j] for i,j in sorted(Stats.Dict.items())]
    print(tabulate.tabulate(tx,hx, tablefmt = 'presto'))
    print()
    pass


def printArray(A):
    print(' '.join(map(fmt_num,A)))
    pass

