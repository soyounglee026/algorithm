N = int(input())

li = [input() for i in range(N)]

count = 0
cnt = []
for i in range(N):
  if li[i] == 'ENTER':
    count += len(set(cnt))
    cnt = []
  else:
    cnt.append(li[i])
count += len(set(cnt))

print(count)