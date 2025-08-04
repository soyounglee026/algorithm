import sys

input = sys.stdin.readline

C = int(input())
li = [[*map(int, input().split())] for _ in range(C)]

for i in range(C):
  p = 0
  avg = sum(li[i][1:])/li[i][0]
  for j in range(1, li[i][0]+1):
    if avg < li[i][j]:
      p += 1
  print(f'{p/li[i][0]*100:.3f}%')