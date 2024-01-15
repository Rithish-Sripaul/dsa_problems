def topKElements(nums, k):
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    print(count)
topKElements([2, 2, 1,1 , 1, 1, 1, 2, 2, 3], 2)

