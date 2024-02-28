def majority_element(nums):
    count = 0
    max_ele = nums[0]

    for num in nums:
        if max_ele != num:
            if count < 0:
                count = 0
                max_ele = num
            else:
                count -= 1
    
    return max_ele

nums = [2, 2, 1, 1, 1, 2, 2]

print(majority_element(nums))