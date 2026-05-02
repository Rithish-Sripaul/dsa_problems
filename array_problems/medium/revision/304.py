class NumMatrix:

  def __init__(self, matrix: list[list[int]]):
    self.matrix = matrix
    self.prefixSum = self.calculatePrefixSum(matrix)
  
  def calculatePrefixSum(self, matrix):
    n = len(matrix)
    m = len(matrix[0])

    prefixSum = [[0] * m for _ in range(n)]

    for i in range(n):
      for j in range(m):
        prefixSum[i][j] = matrix[i][j]

        if i > 0:
          prefixSum[i][j] += prefixSum[i - 1][j]
        
        if j > 0:
          prefixSum[i][j] += prefixSum[i][j - 1]
        
        if i > 0 and j > 0:
          prefixSum[i][j] -= prefixSum[i - 1][j - 1]

    return prefixSum
    
  def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    answer = self.prefixSum[row2][col2]
    n, m = len(self.prefixSum), len(self.prefixSum[0])
    if col1 > 0:
      answer -= self.prefixSum[row2][col1 - 1]
    if row1 > 0:
      answer -= self.prefixSum[row1 - 1][col2]
    if col1 > 0 and row1 > 0:
      answer += self.prefixSum[row1 - 1][col1 - 1]

    return answer

nums = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
matrix = NumMatrix(nums)
print(matrix.sumRegion(2, 1, 4, 3))
print(matrix.sumRegion(1, 1, 2, 2))
print(matrix.sumRegion(1, 2, 2, 4))


for i in range(len(nums)):
  print(nums[i])
print()

for i in range(len(nums)):
  print(matrix.prefixSum[i])
      
  