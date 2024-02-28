def first_approach(nums):
    ans = []
    pos, neg = 0, 0
    i = 0
    while i < len(nums):
        if i == 0:
            if nums[pos] > 0:
                ans.append(nums[pos])
                i += 1
            pos += 1
        else:
            if i % 2 == 1:
                if nums[neg] < 0:
                    ans.append(nums[neg])
                    i += 1
                neg += 1
            else:
                if nums[pos] > 0:
                    ans.append(nums[pos])
                    i += 1
                pos += 1
                
    return ans

nums = [3, 1, -2, -5, 2, -4]
print(first_approach(nums))