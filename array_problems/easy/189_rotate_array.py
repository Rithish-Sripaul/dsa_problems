# METHOD 1: ROTATE ONE BY ONE - to the left
def rotate_array_left(arr, k):
  p = 0
  while p <= k:
    last = arr[0]
    for i in range(len(arr) - 1):
      arr[i] = arr[i + 1]
    arr[len(arr) - 1] = last
    p += 1
  return arr


# CORRECT METHOD: ROTATE ARRAY TO THE RIGHT
# RESULT: Time Limit Exceeded
def rotate_array_right(arr, k):
  p = 0
  n = len(arr)
  while p < k:
    first = arr[n - 1]
    for i in range(n - 1, 0, -1):
      arr[i] = arr[i - 1]
    arr[0] = first
    p += 1
  return arr

# METHOD 3: Slicing, Not in place
def rotate_array_right_slicing(arr, k):
  n = len(arr)
  arr = arr[n - k:] + arr[:n - k]
  # print(arr[n - k:] + arr[:n-k])
  return arr

# METHOD 4: Using Mod, Not in place
def rotate_array_right_mod(arr, k):
  res = [0] * len(arr)
  for i in range(len(arr)):
    res[(i + k) % len(arr)] = arr[i]
  return res

# METHOD 5: Reversing arr, IN PLACE
def rotate_array_right_reverse(arr, k):
  arr = arr[::-1]
  arr[:k] = list(reversed(arr[:k]))
  arr[k:] = list(reversed(arr[k:]))
  # print(arr)
  # print(list(reversed(arr[:k])))
  # arr[:k] = arr[:k:-1]
  # print(arr)
  # arr[k:] = arr[k::-1]
  # print(arr)
  return arr
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
# print(rotate_array_right(arr, k))
# print(rotate_array_right_slicing(arr, k))
# print(rotate_array_right_mod(arr, k))
print(rotate_array_right_reverse(arr, k))
# for k in range(5, 1, -1):
  # print(k)