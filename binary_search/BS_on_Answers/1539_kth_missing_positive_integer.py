def first_approach(arr, k):
    low, high = 0 , len(arr) - 1

    count = arr[0] - 1
    middle = (low + high) // 2
    while low <= high:
        middle = (low + high) // 2
        
        if count > k:
            return arr[middle] - (count - k)


        if count + 1 + middle == arr[middle]:
            low = middle + 1
        elif count + 1 + middle < arr[middle]:
            count += arr[middle] - (count + 1 + middle)
            low = middle + 1
        else:
            high = middle - 1
    print("Count: ", count)
    if count <= 0:
        return arr[-1] + (k - count)
    return arr[middle] - (count - k + 1)

nums = [2, 3, 4, 7, 11]
nums1 = [1, 2, 3, 4]
print(first_approach(nums, 1))

