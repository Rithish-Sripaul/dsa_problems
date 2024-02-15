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
                if i == 0 and j == 0:
                    col0 = 0
                    matrix[i][j] = 0
                else:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
    # print(matrix, col0)

    # Should replace the columns from 1 to n first
    # then replace the rows
    # and then replace the col0, if it is true
    for j in range(1, m):
        if matrix[0][j] == 0:
            for i in range(n):
                matrix[i][j] = 0

    for i in range(n):
        if matrix[i][0] == 0:
            matrix[i] = [0] * m

    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0
    
    
    
    print(matrix)
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
optimal_approach(matrix)
optimal_approach(matrix1)