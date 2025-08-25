s = input()
ans = []

for i in s:
  if ord(i) > 90:
    ans.append(chr(ord(i)-32))
  else: ans.append(chr(ord(i)+32))

print(*ans, sep="")