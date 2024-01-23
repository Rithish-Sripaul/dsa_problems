# WORKED ANSWER

def move_zeroes(arr):
  l = 0
  while l < len(arr):
    if arr[l] == 0:
      for r in range(l, len(arr)):
        if arr[r] != 0:
          arr[l], arr[r] = arr[r], arr[l]
          break
    l += 1
  return arr

def move_zeroes_2(arr):
  l, r = 0, 0
  while l < len(arr):
    if r > len(arr):
        return arr  
    if arr[l] == 0:
      
      if arr[r] != 0:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r = l
      else:
        r += 1
    else:
      l += 1
      r = l

  return arr

arr = [0, 1, 0, 3, 12]
print(move_zeroes(arr))
print(move_zeroes_2(arr))
    
      