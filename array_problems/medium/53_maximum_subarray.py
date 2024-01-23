# def maximum_subarray(nums):
#   curr_max, maxTillNow = 0, -9999999

#   for num in nums:
#     curr_max = max(curr_max, curr_max + num)
#     maxTillNow = max(curr_max, maxTillNow)
  
#   return maxTillNow


# Optimal solution
# Will allow the user to take the maximum subarray too
def maximum_subarray_with_array(nums):
  # Start and end of the maxim_ subarray
  start, end = 0, 0
  result = nums[0]
  s = 0 # Temp start of the array
  Sum = 0

  for i in range(len(nums)):
    Sum += nums[i]

    if Sum > result:
      result = Sum
      start = s
      end = i
    
    if Sum < 0:
      Sum = 0
      start = i + 1
  
  return result
nums = [-2,1,-3,4,-1,2,1,-5,4]


print(maximum_subarray_with_array(nums))