N = int(input())
stars = [['*'] * N for _ in range(N)]

def star(n, x, y):
  if n == 1:
    return

  size = n // 3

  for i in range(x + size, x + (size*2)):
    for j in range(y + size, y + (size*2)):
      stars[i][j] = ' '

  for dx in range(0, n, size):
    for dy in range(0, n, size):
      if dx == size and dy == size:
        continue
      star(size, x+dx, y+dy)


star(N, 0, 0)

for i in range(N):
  print(''.join(stars[i]))