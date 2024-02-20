import math
def first_approach(nums, threshold):

    low, high = 1, max(nums)
    ans = 0
    while low <= high:
        middle = (low + high) // 2
        sum_divisor = 0
        for i in nums:
            sum_divisor += math.ceil(i / middle)
        if sum_divisor <= threshold:
            ans = middle
            high = middle - 1
        else:
            low = middle + 1
    return ans
nums = [1, 2, 5, 9]
nums1 = [44, 22, 33, 11, 1]
nums2 = [21212, 10101, 12121]
print(first_approach(nums, 6))
print(first_approach(nums1, 5))
print(first_approach(nums2, 1000000))

        