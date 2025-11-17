T = int(input())

list = [[0] * 4 for i in range(T)]

for i in range(T):
  C = int(input())

  list[i][0] = C//25
  list[i][1] = (C%25)//10
  list[i][2] = ((C%25)%10)//5
  list[i][3] = (((C%25)%10)%5)//1

for i in range(T):
  for j in range(4):
    if j == 3:
      print(list[i][j])
    else: print(list[i][j], end=" ")