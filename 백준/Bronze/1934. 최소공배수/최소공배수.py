from math import gcd

N = int(input())
li = [[*map(int, input().split())] for _ in range(N)]
for i in range(N):
  a, b = li[i][0], li[i][1]
  print((a*b)//gcd(a, b))