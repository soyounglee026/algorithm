import sys

input = sys.stdin.readline

N, M = map(int, input().split())

res = []

def backtracking():
  if len(res) == M:
    print(*res)
  
  for i in range(1, N+1):
    if len(res) != M:
      res.append(i)
      backtracking()
      res.pop()

backtracking()