N = int(input())
cards = [0, 1, 2, 2, 4]

i = 5
while len(cards) <= N:
  n = cards[i-1]+2
  if n > i:
    n = 2
    cards.append(n)
  else:
    cards.append(n)
  i += 1
print(cards[N])