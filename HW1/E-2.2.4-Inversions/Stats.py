#
# Created by : Jiang Long (jiang.long@dukekunshan.edu.cn)
#
# For COMPSCI 301 FALL S02 2021
#
import collections
import tabulate

# format string with width 3, a hack
def fmt_num(n): return '%3s' % str(n)

''''
# Design doc

    We consider run-time statistics to be of the form key:value pairs,
    where the key is a string and value can be int, float, list etc.

    Default values for all value based statistics is 0.

# Common used API implemented
  
   Reset 
   Inc
   Set
   PrintArray
   PrintStats

See code for there definitions, no more documentation is provided.

'''
class Stats:
    Dict = collections.defaultdict(lambda: 0)
    pass


# Reset all values
def Reset():
    Stats.Dict = collections.defaultdict(int)
    pass

# Increment the value by 'val', default is 1
def Inc(key, val=1):
    Stats.Dict[key] = Stats.Dict[key]  +val
    pass

# Hard set a value
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

