s = input()

for i in range(10, len(s)+1, 10):
  print(s[i-10:i])

print(s[len(s)-len(s)%10:])