N = int(input())
mycard = [*map(int, input().split())]
M = int(input())
card = [*map(int, input().split())]

idx = [0 for _ in range(20000000)]

for i in mycard:
  idx[i+10000000] = 1

ans = [idx[i+10000000] for i in card]
print(*ans)