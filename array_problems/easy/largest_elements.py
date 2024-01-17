def largest_ele(arr):
  largest = arr[0]
  for i in range(len(arr)):
    largest = max(arr[i], largest)
  
  return largest

arr = [1, 2, 45, 234, 12, 1, -1]
print(largest_ele(arr))