def find_smallest(nums, threshold):
  low, high = 1, max(nums)

  ans = max(nums)
  while low <= high:
    middle = (low + high) // 2

    temp = 0.
    for i in nums:
      temp += math.ceil(i, middle)

    if temp <= threshold:
      return ans
      high = middle - 1
    else:
      low = middle + 1
  return ans
print(find_smallest([1, 2, 5, 9], 6))
print(find_smallest([44,22,33,11,1], 5))