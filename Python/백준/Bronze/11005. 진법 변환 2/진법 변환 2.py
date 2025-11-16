a, b = input().split()

a = int(a)
b = int(b)

list = []

while True:

  if a < b:
    list.append(a)
    break
  
  list.append(a%b)

  a//=b

i = len(list)

answer = []

while i != 0:

  if list[i-1] >= 10:
    answer.append(chr(55+list[i-1]))
  else: answer.append(str(list[i-1]))
  i -= 1

ans = ''.join(answer)
print(ans)