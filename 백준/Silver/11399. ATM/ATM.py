N = int(input())
li = [*map(int, input().split())]
ans = 0
li.sort()

for i in range(N):
  ans += li[i] * (N-i)

print(ans)