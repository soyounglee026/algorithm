import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

A = [*map(int, input().split())]
B = [*map(int, input().split())]
M = int(input())
C = [*map(int, input().split())]

dq = deque(C)

for i in range(len(A)):
  if A[i] == 0:
    dq.appendleft(B[i])

print(*[dq[i] for i in range(M)])