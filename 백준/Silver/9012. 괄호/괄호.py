N = int(input())

for _ in range(N):
  s = input()
  stack = []
  is_vps = True
  
  for i in s:
    if i == '(':
      stack.append(i)
    elif not stack:
      is_vps = False
      break
    else: stack.pop()
  
  if is_vps and not stack:
    print("YES")
  else: print("NO")