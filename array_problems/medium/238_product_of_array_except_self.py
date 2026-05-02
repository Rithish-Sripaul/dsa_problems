def solution_prefix_product(nums: list[int]) -> list[int]:
  n = len(nums)
  ans = [0] * n
  prefix = [1] * n
  suffix = [1] * n

  # Calculate Prefix
  product = 1
  for i in range(1, n):
    prefix[i] = prefix[i - 1] * nums[i - 1]
  
  # Calculate Suffix
  product = 1
  for j in range(n - 2, -1, -1):
    suffix[j] = suffix[j + 1] * nums[j + 1]
  
  for i in range(n):
    ans[i] = prefix[i] * suffix[i]

  return ans

def solution_order_n(nums: list[int]) -> list[int]:
  n = len(nums)
  ans = [1] * n

  for i in range(1, n):
    ans[i] = ans[i - 1] * nums[i - 1]
  right = 1
  for i in range(n - 1, -1, -1):
    ans[i] = ans[i] * right
    right = right * nums[i]
  return ans

nums = [1, 2, 3, 4]
print(solution_order_n(nums))
