import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

ABC =str(A*B*C)
ans = [0] *10

for i in range(len(ABC)):
  n = ABC[i]
  ans[int(n)] += 1

print(*ans, sep='\n')