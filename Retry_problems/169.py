def majority_element(nums):
  count = 0
  max_ele = -1
  
  for i in nums:
    if i == max_ele:
      count += 1
    else:
      count -= 1
      if count < 0:
        count = 0
        max_ele = i
  return max_ele

nums = [3, 2, 3]
nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))
