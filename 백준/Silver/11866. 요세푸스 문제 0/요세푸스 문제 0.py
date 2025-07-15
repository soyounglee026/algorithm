N, K = map(int, input().split())

li = [i for i in range(1, N+1)]
ans = []

idx = K-1
while len(li) != 0:
  if idx >= len(li):
    idx -= len(li)
  else:
    ans.append(li.pop(idx))
    idx += K-1
    
print('<' + ', '.join(map(str, ans)) + '>')