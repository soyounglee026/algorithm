import sys
import collections

input = sys.stdin.readline

N = int(input())

queue = collections.deque()
s = [input().split() for _ in range(N)]

for i in range(N):
  cmd = s[i][0]
  if cmd == 'push':
    queue.append(int(s[i][1]))
  elif cmd == 'size':
    print(len(queue))
  elif not queue:
    if cmd == 'empty':
      print(1)
    else:
      print(-1)
  elif cmd == 'empty':
    print(0)
  elif cmd == 'front':
    print(queue[0])
  elif cmd == 'back':
    print(queue[-1])
  else:
    print(queue.popleft())