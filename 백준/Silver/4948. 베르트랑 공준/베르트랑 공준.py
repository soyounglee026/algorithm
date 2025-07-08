import math

def segmented_sieve(N):
  size = N+1
  is_pn = [True] * size

  pn = [True] * (int(math.sqrt(2*N))+1)
  pn[0] = pn[1] = False

  for i in range(2, int(math.sqrt(2*N))+1):
    if pn[i]:
      for j in range(i*i, int(math.sqrt(2*N))+1, i):
        pn[j] = False
  
  for i in range(2, int(math.sqrt(2*N))+1):
    if pn[i]:
      start = max(i*i, ((N+i-1)//i) * i)
      for j in range(start, 2*N+1, i):
        is_pn[j-N] = False
  if is_pn[0]:
    print(is_pn.count(True)-1)
  else: print(is_pn.count(True))
    
while True:
  N = int(input())
  if N == 0:
    break
  segmented_sieve(N)