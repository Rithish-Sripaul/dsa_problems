def subsetSums(n, arr):

  def find(arr, sum, index):
    if index == len(arr):
      ans.append(sum)
      return    
    # Element is picked
    find(arr, sum + arr[index], index + 1)
    # Element is not picked
    find(arr, sum, index + 1)

  ans = []
  find(arr, 0, 0)
  print(ans)

subsetSums(2, [2, 3])


