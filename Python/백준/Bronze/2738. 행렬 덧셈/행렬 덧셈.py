n, m = map(int, input().split())

A = []
for _ in range(n):
  A.append(input().split())

B = []
for _ in range(n):
  B.append(input().split())

for j in range(n):
  for i in range(m):
    print(int(A[j][i])+int(B[j][i]), end=" ")
  print()