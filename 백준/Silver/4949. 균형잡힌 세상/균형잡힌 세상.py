while True:
  s = input()

  if s == '.':
    break

  stack = []
  yesorno = True

  for i in s:
    if i == '[' or i == '(':
      stack.append(i)
    elif len(stack) == 0 and (i == ']' or i == ')'):
      yesorno = False
      break
    elif i == ']':
      if stack[-1] == '[':
        stack.pop()
      else:
        yesorno = False
        break
    elif i == ')':
      if stack[-1] == '(':
        stack.pop()
      else:
        yesorno = False
        break
  
  if len(stack) > 0:
    yesorno = False

  if yesorno:
    print('yes')
  else: print('no')