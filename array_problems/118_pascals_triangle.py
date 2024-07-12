def pascals_triangle(numRows):
  ans = []
  for i in range(1, numRows + 1):
    if i == 1:
      ans.append([1])
    elif i == 2:
      ans.append([1, 1])
    else:
      subAns = [1]
      for j in range(1, i - 1):
        subAns.append(ans[-1][j - 1] + ans[-1][j])
      subAns.append(1)
      ans.append(subAns)
  return ans

print(pascals_triangle(5))
print(pascals_triangle(1))