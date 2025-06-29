N = int(input())
c = [*map(int, input().split())]

sorted_c = sorted(set(c))
order=[]

order = {j: i for i, j in enumerate(sorted_c)}

ans = [order[i] for i in c]
print(*ans)