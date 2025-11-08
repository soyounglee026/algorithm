n = int(input())
x = 0
y = 0
for _ in range(n):
  s = input()
  for j in range(len(s)):
    for k in range(j+2, len(s)):
      if s[j] != s[j+1] and s[j] == s[k]:
        y = 1
        break
  if y != 1:
    x = x+1
  y = 0
print(x)