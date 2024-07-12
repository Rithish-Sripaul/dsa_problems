# Set matrix zeroes

def my_first_approach(matrix):
    arr = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                arr.append([i, j])

    for comb in arr:
        matrix[comb[0]] = [0] * len(matrix[0])
        for i in range(len(matrix)):
            matrix[i][comb[1]] = 0
    
# Space complexity: O(m + n)
def better_approach(matrix):
    n, m = len(matrix), len(matrix[0])

    row = [0] * n
    col = [0] * m

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0

# Space Complexity: O(1)
def optimal_approach(matrix):
    col0 = 1
    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # marking the row
                matrix[i][0] = 0

                # marking the col
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    # print(matrix, col0)

    # Mark with 0 from (1, 1) to (n - 1, m - 1)
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Mark with 0 for 1st col and 1st row
    # ROW
    if matrix[0][0] == 0:
        matrix[0] = [0] * m
    # COL
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0
    return matrix
    
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(optimal_approach(matrix))
optimal_approach(matrix1)