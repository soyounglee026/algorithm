n = int(input())

x, y = 0, 1
for i in range(n-1):
  if i%2 == 0:
    y = x+y
  else: x = x+y

if n == 0:
  print(0)
else: print(x+y)