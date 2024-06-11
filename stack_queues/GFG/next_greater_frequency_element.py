def find(nums):
  hash, freq = {}, []
  freqInd = []
  for i in nums:
    hash[i] = hash.get(i, 0) + 1

  for i in nums:
    freq.append(hash[i])

  stack, stackEle = [], []
  result = []
  for i in range(len(nums) -1, -1, -1):
    while stack and stack[-1] <= freq[i]:
      stack.pop()
      stackEle.pop()
    
    if stack:
      result.insert(0, stackEle[-1])
    else:
      result.insert(0, -1)
    stack.append(freq[i])
    stackEle.append(nums[i])
  return result



nums = [1, 1, 2, 3, 4, 2, 1]
print(find(nums))
  