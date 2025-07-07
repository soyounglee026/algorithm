import sys

input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
  a = [*map(int, input().split())]

  if a[0] == 1:
    stack.append(a[1])
  elif a[0] == 3:
    print(len(stack))
  elif len(stack) == 0:
    if a[0] == 4:
      print(1)
    else: print(-1)
  elif a[0] == 4:
    print(0)
  elif a[0] == 5:
    print(stack[-1])
  else:
    print(stack.pop())