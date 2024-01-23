def majority_element(nums):
  hash = {}
  for num in nums:
    hash[num] = hash.get(num, 0) + 1
    if hash[num] > len(nums) / 2:
      return num

# Time: O(n)
# Space: O(1)
# Moore algorithm
# Only works if the count of majority element is > n/2
# So even if the count variable is reset to 0, the majority element will still take the lead in the end
def majority_element_optimal(nums):
  count, candidate = 0, 0

  for num in nums:
    if count == 0:
      candidate = num

    if num == candidate:
      count += 1
    else:
       count -= 1
  
  return candidate  

nums = [2,2,1,1,1,2,2, 3, 3, 3,3 ,3, 3, 3, 33, 3, 33, 3, 3, 3, 3]
print(majority_element_optimal(nums))
