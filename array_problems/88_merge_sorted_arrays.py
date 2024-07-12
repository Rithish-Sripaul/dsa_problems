def mergeSortedArrays(nums1, m, nums2, n):

  n1, n2 = m - 1, n - 1
  A = n + m - 1

  while n2 >= 0 and n1 >= 0:
    if nums1[n1] < nums2[n2]:
      nums1[A] = nums2[n2]
      A -= 1
      n2 -= 1
    else:
      nums1[A] = nums1[n1]
      A -= 1
      n1 -= 1
  return nums1
    

print(mergeSortedArrays([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
