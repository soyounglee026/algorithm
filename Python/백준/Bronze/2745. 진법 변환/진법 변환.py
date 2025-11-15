N, B = input().split()
N = ''.join(reversed(N))
B = int(B)
sum = 0

for i in range(len(N)-1, -1, -1):
  if (ord(N[i])-55) < 9:
    sum = sum + int(N[i]) * B**i
  else:
    sum = sum + (ord(N[i])-55) * B**i

print(sum)