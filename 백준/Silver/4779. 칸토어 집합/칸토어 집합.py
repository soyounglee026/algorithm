def cantor(A, p, r):
  n = (r-p)//3

  if n == 0:
    return

  for i in range(p+n, r-n):
    if A[i] == '-':
      A[i] = ' '

  cantor(A, p, p+n)
  cantor(A, r-n, r)

while True:
  try:
    N = int(input())
    A = ['-'] * (3**N)
    cantor(A, 0, len(A))
    print(*A, sep='')
  
  except EOFError:
    break