def single_number(nums):
  xor = 0
  for num in nums:
    xor ^= num
    print(xor)
  return xor

nums = [4, 1, 2, 2, 1]
print(single_number(nums))
