N = int(input())

li = [0 for _ in range(20000001)]

card = [*map(int, input().split())]

for i in card:
  li[i+10000000] += 1

M = int(input())
card2 = [*map(int, input().split())]

ans = []
for i in card2:
  ans.append(li[i+10000000])
print(*ans)