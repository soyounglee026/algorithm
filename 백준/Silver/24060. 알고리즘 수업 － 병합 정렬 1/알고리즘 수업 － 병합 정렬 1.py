import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = [*map(int, input().split())]

cnt = 0
result = -1

def merge_sort(A, p, r):
  if p < r:
    q = (p+r)//2
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    merge(A, p, q, r)

def merge(A, p, q, r):
  global cnt, result
  tmp = []
  i = p
  j = q+1

  while i <= q and j <= r:
    if A[i] <= A[j]:
      tmp.append(A[i])
      i += 1
    else:
      tmp.append(A[j])
      j += 1

  while i <= q:
      tmp.append(A[i])
      i += 1
  while j <= r:
      tmp.append(A[j])
      j += 1

  t = 0
  i = p

  while i <= r:
    A[i] = tmp[t]
    cnt += 1
    if cnt == K:
      result = A[i]
    i += 1
    t += 1

merge_sort(A, 0, N-1)
print(result)