def fmt_num(n): return '%3s' % str(n)
import collections
import tabulate
class Stats:
    Dict = collections.defaultdict(int)
    @staticmethod
    def Reset():
        Dict = collections.defaultdict(lambda i: 0)
        pass
    def Inc(key, val=1):
        Stats.Dict[key] = Stats.Dict[key]  +val
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

    def PrintArrayRange(A, p, r, labels=[], itemWidth=4, symbol = '#'):
        '''
        p = 10 
        q = 19
        labels = [10 11]
        symbol = '#'
        This would print the sub-array A[10:19] with a  '#' after item 10 and 11
        '''
        f = lambda i: '%3s ' % str(i[1])  if (i[0]+p) not in labels else ( '%3s' % (str(i[1])) + symbol)
        
        s = [' ' *itemWidth ] * p + list(map(f, enumerate(A[p:r]))) + [' '*itemWidth]* (len(A) -r)

        #s = [' ' *itemWidth ] * p + list(map(f, range(p,r))) + [' '*itemWidth]* (len(A) -r)

        return ' '.join(s)
    pass
