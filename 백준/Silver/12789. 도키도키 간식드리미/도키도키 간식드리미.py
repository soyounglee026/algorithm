N = int(input())

line = [*map(int, input().split())]

num = 1
space = []
ox = True

a = line.pop(0)
for _ in range(N):
  if not line:
    break
  if a == num:
    num += 1
    a = line.pop(0)
  elif not space or space[-1] > a:
    space.append(a)
    a = line.pop(0)
  elif space[-1] == num:
    space.pop()
    num += 1
  else:
    ox = False
    break

if ox:
  print("Nice")
else: print("Sad")