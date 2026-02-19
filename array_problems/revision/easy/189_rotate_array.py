# optimal approach



# not optimal
def rotate_right_by_k(nums, k):

  for count in range(k % len(nums)):
    last = nums[-1]

    for i in range(len(nums) - 1, 0, -1):
      nums[i] = nums[i - 1]
    
    nums[0] = last

# Approach using mod
def approach_2(nums, k):
  res = [0] * len(nums)

  for i in range(len(nums)):
    res[(i + k) % len(nums)] = nums[i]
  
  return res

# Approach using reverse
def approach_3(nums, k):
  print(nums)
  print(list(reversed(nums[len(nums) - k:])))
  res = nums[len(nums) - k::-1].append(nums[:len(nums) - k - 1])
  return res

nums = [1, 2, 3, 4, 5]

print(approach_3(nums, 2))
  