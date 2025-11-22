N = int(input())
list = []
n = 0
i = 1

while True:
  if N == 2:
    print(2)
    break
  elif N <= (n*6)+1:
    print(i)
    break
  n += i
  i += 1