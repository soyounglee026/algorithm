N = int(input())

li = [input().split() for _ in range(N)]

dance = ['ChongChong']

for i in range(N):
  if li[i][0] in dance:
    dance.append(li[i][1])
  elif li[i][1] in dance:
    dance.append(li[i][0])

print(len(set(dance)))