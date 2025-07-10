N = int(input())
ans = []

for _ in range(N):
  M = int(input())
  if M == 0:
    ans.pop()
  else: ans.append(M)

print(sum(ans))