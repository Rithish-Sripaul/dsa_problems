def solution(arr):
  if arr[0] > arr[1]:
    largest, second_largest = arr[0], arr[1]
    smallest, second_smallest = arr[1], arr[0]
  else:
    largest, second_largest = arr[1], arr[0]
    smallest, second_smallest = arr[0], arr[1]

  for i in range(2, len(arr)):
    if arr[i] > largest:
      second_largest = largest
      largest = arr[i]
    elif arr[i] < largest and arr[i] > second_largest:
      second_largest = arr[i] 

    if arr[i] < smallest:
      second_smallest = smallest
      smallest = arr[i]
    elif arr[i] < second_smallest  and arr[i] > smallest:
      second_smallest = arr[i]
  
  return [second_largest, second_smallest]

print(solution([10, 20, 30, 40]))
print(solution([10, 20, 40, 40]))
print(solution([20, 30, 10, 500]))