import math

def segmented_sieve(N):
  size = N
  is_pn = [True] * (size+1)
  
  pn = [True] * (int(math.sqrt(N))+1)
  pn[0] = pn[1] = False

  for i in range(2, int(math.sqrt(N))+1):
    if pn[i]:
      for j in range(i*i, int(math.sqrt(N)+1), i):
        pn[j] = False

  for i in range(2, int(math.sqrt(N))+1):
    if pn[i]:
      for j in range(i*i, N+1, i):
        is_pn[j] = False

  is_pn[0] = is_pn[1] = False
  
  return is_pn

N = int(input())

num = [int(input()) for _ in range(N)]

pn = segmented_sieve(max(num))

for i in range(N):

  count = 0

  for j in range(num[i]//2+1):
    if pn[j]:
      if pn[num[i]-j]:
        count += 1
  print(count)