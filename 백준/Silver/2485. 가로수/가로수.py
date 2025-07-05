from math import gcd
from functools import reduce

N = int(input())
tree = [int(input()) for _ in range(N)]

diffs = [tree[i+1] - tree[i] for i in range(N-1)]

d = reduce(gcd, diffs)

print(((tree[-1] - tree[0]) // d + 1) - N)