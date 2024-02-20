def first_approach(bloomDay, m, k):
    n = len(bloomDay)
    if n < m*k:
        return -1
    

    reqDays = 0
    low, high = 0, max(bloomDay)

    while low <= high:
        middle = (low + high) // 2

        temp_list = list(bloomDay)

        while True:
            for i in range(len(bloomDay)):
                if temp_list[i] < middle:
                    temp_list[i] = 0
                else:
                    temp_list[i] -= middle

            
            

nums = [7, 7, 7, 7, 12, 7, 7]
print(first_approach(nums, 2, 3))
            

            
