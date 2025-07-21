import sys
import collections

input = sys.stdin.readline

N = int(input())

num = [int(input()) for _ in range(N)]

# 산술평균
avg = sum(num)/N
# avg가 양수일 때
if (avg-(sum(num)//N)) >= 0.5:
 print(sum(num)//N+1)
# avg가 음수일 때
elif (avg-(sum(num)//N+1)) <= -0.5:
  print(sum(num)//N)
else: print(round(avg))
    
# 중앙값
num.sort()
print(num[N//2])

# 최빈값
import collections
ans = collections.Counter(num).most_common(2)

if len(ans) == 1 or ans[0][1] != ans[1][1]:
  print(ans[0][0])
else:
  ans.sort()
  print(ans[1][0])
    
# 범위
print(num[-1]-num[0])