N, M = map(int, input().split())

name2idx = {}
idx2name = {}

for i in range(1, N+1):
  name = input()
  name2idx[name] = i
  idx2name[i] = name

q = [input() for _ in range(M)]
for i in q:
  if i in name2idx:
    print(name2idx[i])
  else: print(idx2name[int(i)])