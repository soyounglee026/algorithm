import sys

input = sys.stdin.readline

N = int(input())
s = []
stack = []

for _ in range(N):
  s = input().split()

  if len(s) == 2:
    stack.append(int(s[1]))
  elif s[0] == 'size':
    print(len(stack))
  elif len(stack) == 0:
    if s[0] == 'empty':
      print(1)
    else: print(-1)
  elif s[0] == 'pop':
    print(stack.pop())
  elif s[0] == 'top':
    print(stack[-1])
  elif s[0] == 'empty':
    print(0)