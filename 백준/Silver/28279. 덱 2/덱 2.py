from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
li = [[*map(int,input().split())] for i in range(N)]

deq = deque()
for i in range(N):
  l = li[i][0]
  if len(li[i]) == 2:
    if l == 1:
      deq.appendleft(li[i][1])
    else: deq.append(li[i][1])
  elif l == 5:
    print(len(deq))
  elif l == 6:
    if deq:
      print(0)
    else: print(1)
  elif len(deq) == 0:
    print(-1)
  elif l == 3 or l == 7:
    p = deq.popleft()
    print(p)
    if l == 7:
      deq.appendleft(p)
  elif l == 4 or l == 8:
    p = deq.pop()
    print(p)
    if l == 8:
      deq.append(p)