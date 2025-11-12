arr = []
for _ in range(9):
  arr.append(input().split())

max = 0
x = 0
y = 0
for i in range(9):
  for j in range(9):
    if int(arr[i][j]) > max:
      max = int(arr[i][j])
      x = i
      y = j

print(max)
print(x+1, y+1)