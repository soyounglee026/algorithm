A, B, C = map(int, input().split())

if C-B == 0:
  ans = -1
else: ans = A//(C-B)+1

if ans < 0:
  print(-1)
else: print(A//(C-B)+1)