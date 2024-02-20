import math
def first_approach(weights, days):

    low = max(weights)
    high = math.ceil(len(weights) / days) * max(weights)
 
    ans = 0

    while low <= high: 
        middle = (low + high) // 2
        capacity = middle
        count_days = 1
        for weight in weights:
            if weight > capacity:
                if count_days > days:
                    break
                capacity = middle
                count_days += 1
            capacity -= weight
        if count_days <= days:
            ans = middle
            high = middle - 1
        else:
            low = middle + 1
        
    return ans

weights = [1,2,3,4,5,6,7,8,9,10]
weights1 = [3, 2, 2, 4, 1, 4]
weights2 = [1,2,3,1,1]
print(first_approach(weights, 1))
print(first_approach(weights1, 3))
print(first_approach(weights2, 4))