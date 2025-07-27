import sys

input = sys.stdin.readline

N = int(input())
li = [input() for _ in range(N)]

ans = [True] * len(li[0])

for i in range(len(li[0])):
  for j in range(N):
    if j == 0:
      tmp = li[0][i]
    elif tmp != li[j][i]:
      ans[i] = False

for i in range(len(ans)):
  if ans[i]:
    ans[i] = li[0][i]
  else: ans[i] = '?'

print(*ans, sep="")