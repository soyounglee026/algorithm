import collections
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
li = []

for _ in range(N):
  s = input().strip()
  if len(s) >= M:
    li.append(s)

f = collections.Counter(li).most_common()

tmp = f[0][1]

ans = []
for i in range(len(f)):
  if tmp == f[i][1]:
    ans.append(f[i][0])
  else:
    ans.sort()
    ans.sort(key=len, reverse=True)
    print(*ans, sep="\n")
    ans = []
    tmp = f[i][1]
    ans.append(f[i][0])
ans.sort()
ans.sort(key=len, reverse=True)
print(*ans, sep="\n")