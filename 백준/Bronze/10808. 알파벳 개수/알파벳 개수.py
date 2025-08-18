s = input()

a = [0 for _ in range(26)]

for i in s:
  idx = ord(i)-97
  a[idx] += 1

print(*a)