N, M = map(int, input().split())

A = [*map(int, input().split())]
B = [*map(int, input().split())]

AB = set(A+B)

A = set(A)
B = set(B)
AB -= A&B

print(len(AB))