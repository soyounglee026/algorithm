def recursion(s, i):
  if i >= (len(s)//2):
    print(1, i+1)
    return i
  elif s[i] == s[-(i+1)]:
    i += 1
    recursion(s, i)
  else:
    print(0, i+1)

T = int(input())
for _ in range(T):
  recursion(input(), 0)