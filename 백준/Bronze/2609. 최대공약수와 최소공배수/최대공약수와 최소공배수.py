import math
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
print(math.gcd(N, M))
print(math.lcm(N, M))