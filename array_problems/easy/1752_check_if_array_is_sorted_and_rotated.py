# Check if Array Is Sorted and Rotated

def solution(nums):
    n = len(nums)
    minElePos = 0
    minEle = nums[0]
    for i in range(n):
        if nums[i] < minEle:
            minEle = nums[i]
            minElePos = i
    prevEle = minElePos

    for i in range(n):
        currEle = (minElePos + i) % n
        if nums[currEle] < nums[prevEle]:
            return False
        prevEle = currEle
    return True

print(solution([3, 4, 5, 1, 2]))
print(solution([2, 1, 3, 4]))
print(solution([1, 2, 3]))
print(solution([6, 10, 6]))

    