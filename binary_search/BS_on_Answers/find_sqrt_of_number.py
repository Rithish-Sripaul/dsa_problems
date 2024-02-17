def first_approach(num):
    low, high = 0, num

    while low <= high: 
        
        middle = (low + high) // 2
        sqr = middle ** 2
        if sqr == num:
            return middle
        elif  sqr < num:
            low = middle + 1
        else:
            high = middle - 1
    
    return int(middle)

print(first_approach(256))