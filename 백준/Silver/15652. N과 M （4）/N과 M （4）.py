import sys

input = sys.stdin.readline

N, M = map(int, input().split())

res = []

def backtracking(start):
  if len(res) == M:
    print(*res)
    return

  for i in range(start, N+1):
    res.append(i)
    backtracking(i)
    res.pop()

backtracking(1)