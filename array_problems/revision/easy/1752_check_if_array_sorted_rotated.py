"""
Docstring for array_problems.revision.easy.1752_check_if_array_sorted_rotated
We need to find how many times the ascending order is broken.
if count > 0; then check nums[-1] > nums[0]; if True, then return False
If count <= 1; then it is True
else; False
"""


def optimal_solution(nums):
  count = 0
  if len(nums) == 1:
    return True
  
  for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
      count += 1
    
  if count > 0 and nums[i - 1] > nums[0]:
    return False
  
  return count <= 1

def solution(nums):
  if len(nums) == 1:
    return True
  
  list_started = False
  for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
      if list_started: return False
      
      if nums[-1] > nums[0]:
        return False
      list_started = True
      continue
    if list_started and nums[i] > nums[0]:
      return False
  return True
    
nums = [3, 4, 5, 1, 2, 6, 7, 8]
print(solution(nums))
print(optimal_solution(nums))
