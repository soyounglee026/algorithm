from math import gcd

li = [[*map(int, input().split())] for _ in range(2)]

n = (li[0][0] * li[1][1]) + (li[0][1] * li[1][0])
d = li[0][1] * li[1][1]

print(n//gcd(n, d), d//gcd(n, d))