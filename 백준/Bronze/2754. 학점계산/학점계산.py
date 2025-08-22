grade = input()
ans = []

if grade == 'F':
  print(0.0)
else:
  if grade[0] == 'A':
    ans.append('4')
  elif grade[0] == 'B':
    ans.append('3')
  elif grade[0] == 'C':
    ans.append('2')
  else: ans.append('1')

  if grade[1] == '+':
    ans.append('.3')
  elif grade[1] == '0':
    ans.append('.0')
  else:
    ans.append(int(ans.pop())-0.3)

  print(*ans, sep="")