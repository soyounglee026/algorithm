import sys

input = sys.stdin.readline

s = input().split('-')

ans = 0

if '+' not in s[0]:
  ans += int(s[0])
else:
  sum_nums = map(int, s[0].split('+'))
  ans += sum(sum_nums)

for i in range(1, len(s)):
  if '+' in s[i]:
    sum_nums = map(int, s[i].split('+'))
    ans -= sum(sum_nums)
  else:
    ans -= int(s[i])

print(ans)