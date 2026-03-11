# Input = [0, 1, 0, 3, 12]
# Output = [1, 3, 12, 0, 0]

def move_zeroes(nums):
  if len(nums) > 1:
    
    i, j = 0, 0
    while i < len(nums) and nums[i] != 0:
      i += 1
    
    while j < len(nums):
      if nums[j] == 0:
        j += 1
      else:
        if j > i:
          nums[i], nums[j] = nums[j], nums[i]
        
          while nums[i] != 0:
            i += 1
        j += 1
    
        

          

nums = [0, 1, 0, 3, 12]
nums = [1, 2]
print(move_zeroes(nums))
print(nums)


    


    