
import sys
import HT_Chaining_v2


N = sys.stdin.read().split()[0]

T = HT_Chaining_v2.HashTable(int(N))

HT_Chaining_v2.main(T)