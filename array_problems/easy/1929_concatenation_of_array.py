def concatenation(nums):
  ans = [0] * 2 * len(nums)

  for i in range(len(nums)):
    ans[i] = nums[i]
    ans[i + len(nums)] = nums[i]

  return ans

print(concatenation([1, 2, 1]))
print(concatenation([1, 3, 2, 1]))