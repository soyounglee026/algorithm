N = int(input())

T = []
B = []

for _ in range(N):
  i, j = map(int, input().split())
  T.append(i)
  B.append(j)

TxB = (max(T) * min(B))

print((TxB%7)+1)