from collections import deque

N = int(input())
balloon = deque(enumerate(map(int, input().split())))

ans = []
while balloon:
  num = balloon.popleft()
  ans.append(num[0]+1)
  if num[1] > 0:
    balloon.rotate(-(num[1]-1))
  else: balloon.rotate(-num[1])
print(*ans)