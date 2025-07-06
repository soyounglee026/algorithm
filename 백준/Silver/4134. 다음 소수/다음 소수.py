import math

def find_pn(num):
  if num <= 1:
    return 2
  while True:
    pn = True
    for i in range(2, int(math.sqrt(num))+1):
      if num%i == 0:
        pn = False
        break
    if pn:
      return num
    else: num += 1
        
N = int(input())
for _ in range(N):
  print(find_pn(int(input())))