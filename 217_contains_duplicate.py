def containsDuplicates(nums):
  hash = {}

  for num in nums:
    if hash.get(num, False):
      return False
    else:
      hash[num] = 1
  return True


