import math

T = int(input())

b = [[*map(int, input().split())] for _ in range(T)]

for i in range(T):
  if b[i][0] >= b[i][1]:
    print(math.comb(b[i][0], b[i][1]))
  else: print(math.comb(b[i][1], b[i][0]))