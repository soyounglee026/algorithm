s = input()
cnt = 1
x, y = 0, 0

if len(s) == 1:
  x = 0
  y = int(s[0])
else:
  x = int(s[0])
  y = int(s[1])

z = x+y
x = y
y = z%10
z = x+y

while (x*10+y) != int(s):
  x = y
  y = z%10
  z = x+y
  cnt += 1

print(cnt)