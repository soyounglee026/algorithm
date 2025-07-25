def fibonacci(n):
  f = [0] * (n+1)
  f[1] = f[2] = 1

  cnt = 0

  for i in range(3, n+1):
    f[i] = f[i-1] + f[i-2]
    cnt += 1
  return f[n], cnt

print(*fibonacci(int(input())))