# to find the next greater element for each element

def printNge(arr):
  stack = []

  for i in range(len(arr)):

    if not stack:
      stack.append(arr[i])
      continue

    while stack and stack[-1] < arr[i]:
      print(stack.pop(), "-->", arr[i])
    
    stack.append(arr[i])

  while stack:
    print(stack.pop(), "-->", -1  )

def monotonicDecreasing(nums):
  stack = []
  result = []

  for num in nums:
    while stack and stack[-1] < num:
      stack.pop()
    
    if stack:
      result.append(stack[-1])
    else:
      result.append(-1)
    stack.append(num)
  return result

def monotonicIncreasing(nums):
  stack = []
  result = []

  for num in nums:
    while stack and stack[-1] > num:
      stack.pop()
    
    if stack:
      result.append(stack[-1])
    else:
      result.append(-1)
    stack.append(num)
  return result

def nextGreaterElement(nums):
  stack = []
  result = []
  
  for i in range(len(nums) - 1, -1, -1):
    while stack and stack[-1] <= nums[i]:
      stack.pop()

    if stack:
      result.insert(0, stack[-1])
    else:
      result.insert(0, -1)
    stack.append(nums[i])
  
  return result

printNge([11, 13, 21, 3])
print(monotonicDecreasing([3, 1, 4, 1, 5, 9, 2, 6]))
print(monotonicIncreasing([3, 1, 4, 1, 5, 9, 2, 6]))
print(nextGreaterElement([2, 1, 2, 4, 3]))