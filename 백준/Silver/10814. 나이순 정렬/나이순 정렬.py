N = int(input())
li = []

for i in range(N):
  age, name = input().split()
  li.append([int(age), i, name])

li.sort()

for i in range(N):
  print(li[i][0], li[i][2])