def palindrome():
  if len(nums) <= 1:
     print('yes')
     return
  if nums.pop() != nums.pop(0):
    print('no')
    return
  palindrome()

while True:
  nums = list(input())
  for i in range(len(nums)):
    nums[i] = int(nums[i])
  if len(nums) == 1 and nums[0] == 0:
    break
  palindrome()