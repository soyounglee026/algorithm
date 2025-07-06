import math

def segmented_sieve(N, M):
  size = M-N+1
  is_pn = [True] * size

  pn = [True] * (int(math.sqrt(M))+1)
  pn[0] = pn[1] = False

  for i in range(2, int(math.sqrt(M))+1):
    if pn[i]:
      for j in range(i*i, int(math.sqrt(M))+1, i):
        pn[j] = False
  
  for i in range(2, int(math.sqrt(M))+1):
    if pn[i]:
      start = max(i*i, ((N+i-1)//i) * i)
      for j in range(start, M+1, i):
        is_pn[j-N] = False

  for i in range(size):
    if is_pn[i] and (N+i>1):
      print(N+i)

N, M = map(int, input().split())
segmented_sieve(N, M)