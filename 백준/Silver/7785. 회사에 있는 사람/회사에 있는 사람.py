N = int(input())

record = {name: state for _ in range(N) for name, state in [input().split()]}

li = []
for name in record:
  if record[name] == 'enter':
    li.append(name)
li.sort(reverse=True)
print(*li, sep="\n")