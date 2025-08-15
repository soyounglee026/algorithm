T = int(input())

for _ in range(T):
  H, W, N = map(int, input().split())

  floor = N%H
  
  if floor == 0:
    floor = H
    num = N//H
  else: num = N//H + 1
  print(100*floor + num)