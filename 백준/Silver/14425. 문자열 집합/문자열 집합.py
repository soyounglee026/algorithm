N, M = map(int, input().split())

s = [input() for _ in range(N)]
target = [input() for _ in range(M)]

sum = 0

for i in range(M):
  if target[i] in s:
    target[i] = -1
    sum += 1

print(sum)