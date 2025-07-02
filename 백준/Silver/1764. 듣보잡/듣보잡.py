N, M = map(int, input().split())

h = [input() for _ in range(N)]
h = set(h)

ans = []

for _ in range(M):
  s = input()
  if s in h:
    ans.append(s)

ans.sort()
print(len(ans))
print(*ans, sep="\n")