import sys

input = sys.stdin.readline

N = int(input())

if N < 100:
  print(N)

else:
  cnt = 99
  for i in range(111, N+1):
    s = str(i)
    for j in range(-4, 5):
      if int(s[0])+j == int(s[1]) and int(s[1])+j == int(s[2]):
        cnt += 1

  print(cnt)