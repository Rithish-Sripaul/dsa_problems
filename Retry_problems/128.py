def first_approach(nums):
    hash = {}
    maxTillNow = 0
    for i in nums:
        hash[i] = hash.get(i, 0) + 1
    
    for i in range(len(nums)):
        if nums[i] - 1 not in hash:
            crnt = 0
            start = nums[i]
            while start in hash:
                crnt += 1
                start += 1
            maxTillNow = max(maxTillNow, crnt)

    return maxTillNow


def with_set(nums):
    nums = set(nums)
    maxTillNow = 0

    for x in nums:
        if x - 1 not in nums:
            crnt = 0
            start = x
            while start in nums:
                crnt += 1
                start += 1
            maxTillNow = max(maxTillNow, crnt)
    return maxTillNow

nums = [100, 4, 200, 1, 3, 2]
print(with_set(nums))