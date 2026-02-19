# OPTIMAL METHOD - 0MS, (Feb 18, 2026)
"""
Docstring for array_problems.easy.26_remove_duplicates_from_sorted_array

Simply iterate through the array, maintain value of the current element.
and also maintain the count of number of unique elements
if the new element is different from the current element, replace the position of nums[curent_pos_of_unique_elements] with the new elmenet
return curent_pos_of_unique_elements
"""

def optimal_solution(nums):
  if len(nums) == 1:
    return 1
  current_ele, current_pos = nums[0], 1
  count = 1
  for i in range(1, len(nums)):
    if nums[i] != current_ele:
      nums[current_pos] = nums[i]
      current_ele = nums[i]
      current_pos += 1
      
  
  return current_pos


# ------------------------------------

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


def remove_duplicates_arr(nums):
  k = 0 # Number of unique elements
  l = 0
  currEle = nums[0]
  while l < len(nums):
    # In case the element is repeating
    if nums[k] == nums[l]:
      l += 1
    else:
      k += 1
      nums[k], nums[l] = nums[l], nums[k]
      l += 1
      # currEle = nums[l]

  return nums

print(remove_duplicates_arr([1, 1, 2]))
print(remove_duplicates_arr([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))



