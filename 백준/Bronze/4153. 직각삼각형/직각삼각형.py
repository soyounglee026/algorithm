while True:
  a, b, c = map(int, input().split())

  if a == 0 and b == 0 and c == 0:
    break

  a = a**2
  b = b**2
  c = c**2

  if max(a, b, c)*2 == a+b+c:
    print("right")
  else: print("wrong")