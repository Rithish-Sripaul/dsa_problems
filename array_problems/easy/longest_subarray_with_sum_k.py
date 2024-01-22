def longest_subarray(nums, k):
  ans = 0
  slow, fast = 0, 0
  Sum = 0
  while fast < len(nums):
    while slow <= fast and Sum > k:
      Sum -= nums[slow]
      slow += 1
    
    if Sum == k:
      ans = max(ans, fast - slow)
    
    if fast < len(nums): Sum += nums[fast]
    fast += 1
  
  return ans


nums = [2, 3, 5, 1, 9]
k = 10
print(longest_subarray(nums, k))

      
    