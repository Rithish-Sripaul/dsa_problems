import math
def koko_eating(piles, h):
  low, high = 1, max(piles)
  ans = 0
  while low <= high:
    middle = (low + high) // 2

    count = 0
    for i in piles:
      count += math.ceil(i / middle)

    if count <= h:
      ans = middle
      high = middle - 1
    else:
      low = middle + 1
  return ans

piles = [3, 6, 7, 11]
print(koko_eating(piles, 8))
print(koko_eating([30, 11, 23, 4, 20], 6))