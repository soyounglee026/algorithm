import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = [*map(int, input().split())]

s = [0] * N
s[0] = nums[0]
for i in range(1, N):
  s[i] = nums[i] + s[i-1]

for _ in range(M):
  i, j = map(int, input().split())
  if i == 1:
    print(s[j-1])
  else: print(s[j-1]-s[i-2])