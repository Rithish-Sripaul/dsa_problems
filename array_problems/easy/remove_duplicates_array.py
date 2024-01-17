# METHOD 1 - TIME LIMITED EXCEEDED
def remove_duplicates(nums):
  hash = {}
  k = 0
  for i in range(len(nums)):
    if nums[i] in hash:
      k += 1
      nums[i] = "_"
    else:
      hash[nums[i]] = 1
  print(nums)
  l = 0
  while l != len(nums):
    if nums[l] == "_":
      r = l
      while r < len(nums):
        if nums[r] != "_":
          nums[l], nums[r] = nums[r], nums[l]
          break
        r += 1
    l += 1
  print(nums)
  return k, nums

    # [1, _, 2, _, _, 3]

# arr = [1, 1, 2, 2, 3, 3, 3, 3, 3, 4]
arr = [1, 1, 2  ]
print(remove_duplicates(arr))


def remove_duplicates_2(arr):
  hash = {}
  for i in range(len(nums)):
    if nums[i] in hash:
      if i != len(arr) - 1:
        l = i + 1
        while nums[l] == nums[i]:
          nums[l] == "_"
          l += 1
          





