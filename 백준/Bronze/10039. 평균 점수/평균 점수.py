ans = []

for _ in range(5):
  score = int(input())

  if score <= 40:
    score = 40

  ans.append(score)

print(sum(ans)//5)