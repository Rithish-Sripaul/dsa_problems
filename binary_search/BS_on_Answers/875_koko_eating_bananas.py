import math
def first_approach(piles, h):
    
    sum_ = sum(piles)

    maxN = max(piles)

    low, high = 1, maxN
    ans = low
    while low <= high:
        middle = (low + high) // 2

        temp_pile = list(piles)
        i = 0
        count = 0
        while i < len(temp_pile):

            if temp_pile[i] <= middle:
                temp_pile[i] = 0
                i += 1
                count += 1
            else:
                temp_pile[i] -= middle    
                count += 1
        
        if count <= h:
            ans = middle
            high = middle - 1
        else:
            low = middle + 1
    return int(ans)

def optimal_approach(piles, h):
    low, high = 1, max(piles)
    ans = low
    while low <= high:
        middle = (low + high) // 2
        count = 0
        for i in piles:
            count += math.ceil(i/middle)
        if count <= h:
            ans = middle
            high = middle - 1
        else:
            low = middle + 1
    return ans


nums = [3, 6, 7, 11]
nums1 = [30, 11, 23, 4, 10]
print(first_approach(nums, 8))
print(first_approach(nums1, 5))

print(optimal_approach(nums, 8))