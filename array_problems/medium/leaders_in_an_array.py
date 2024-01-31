#Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.


def find_leaders_optimal(nums):
  n = len(nums)
  ans = []

  maxEle = nums[n - 1]
  ans.append(maxEle)

  for i in range(n - 2, -1, -1):
    if nums[i] > maxEle:
      ans.append(nums[i])
      maxEle = nums[i]
  print(ans)

def find_leaders(nums):

  leaders = {}

  for i in range(len(nums)):
    leaders[nums[i]] = [i, 0]

    for leader in leaders:
      if nums[i] > leader and leaders[leader][0] < i:
        leaders[leader][1] += 1

  print([leader for leader in leaders if leaders[leader][1] == 0])
  # print(leaders)


nums = [4, 7, 1, 0]
nums = [10, 22, 12, 3, 0, 6]
find_leaders_optimal(nums)

