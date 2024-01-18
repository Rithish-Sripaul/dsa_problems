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
arr = [1, 1, 2 , 2, 2, 3]
# print(remove_duplicates(arr))


def remove_duplicates_2(arr):
  hash = {}
  l = 0
  k = 0 # Number of original items
  while l < len(arr):
    if arr[l] in hash:
      duplicate_ele = arr[l]
      while l < len(arr) and arr[l] == duplicate_ele:
        arr[l] = '_'
        l += 1
    else:
      hash[arr[l]] = 1
      arr[l], arr[k] = arr[k], arr[l]
      k += 1
      l += 1
  return k  
  # print(arr, k)

remove_duplicates_2(arr)





