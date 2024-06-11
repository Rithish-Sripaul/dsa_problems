def nge(nums1, nums2):
  stack = []
  hash = {}

  for i in range(len(nums2) -1, -1, -1):
    while stack and stack[-1] <= nums2[i]:
      stack.pop()
    
    if stack:
      hash[nums2[i]] = stack[-1]
    else:
      hash[nums2[i]] = -1
    stack.append(nums2[i])

  ans = []
  for i in nums1:
    ans.append(hash.get(i, -1))
  return ans

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nge(nums1, nums2))
    
  
    

    

