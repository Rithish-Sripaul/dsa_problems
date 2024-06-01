def rotate_image(matrix):
  
  # Simple, Transpose a matrix and reverse it
  # Transposing a matrix

  n, m = len(matrix), len(matrix[0])

  # Transposing a matrix 
  for i in range(n):
    for j in range(i, m):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  
  # Reversing every row
  for i in range(n):
    matrix[i] = matrix[i][::-1]

  return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_image(matrix))