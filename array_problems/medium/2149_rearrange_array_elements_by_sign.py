# 2149 - Rearrange array elements by sign
# It is not possible to solve this question using constant space

def optimal_approach(nums):
  pos, neg, count = 0, 0, 0

  ans = [0] * len(nums)
  while count < len(nums):
    if count % 2 == 0:
      # Positive Number in ans[]
      if nums[pos] > 0:
        ans.append(nums[pos])
        count += 1
      pos += 1
    else:
      # Negative number in ans[]
      if nums[neg] < 0:
        ans.append(nums[neg])
        count += 1
      neg += 1
  return ans

nums = [3,1,-2,-5,2,-4]
nums = [-1, 1]
nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
print(optimal_approach(nums))
print([28,-41,22,-8,46,-37,35,-9,18,-6,19,-26,15,-37,14,-10,31,-9])
      
