import sys

input = sys.stdin.readline

N, M = map(int, input().split())
check = [False] * (M-N+1)

i = 2
while i*i <= M:
  square = i*i
  start = ((N-1)//square+1) * square
  for j in range(start, M+1, square):
    check[j-N] = True
  i += 1

print(check.count(False))