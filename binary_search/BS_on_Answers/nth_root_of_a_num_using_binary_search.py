def first_approach(n, m):
    low, high = 1, m

    while low <= high: 
        middle = (low + high) // 2

        x = middle ** n
        if x == m:
            return middle
        elif x < m:
            low = middle + 1
        else:
            high = middle - 1
    
    return -1

print(first_approach(3, 27))
print("Hello