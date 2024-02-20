def first_approach(matrix):
    n, m = len(matrix), len(matrix[0])
    i, j = 0, 0
    while True:
        if i < n - 1 and j < m - 1:
            print(matrix[i][j])
            j += 1
        elif j == m - 1 and i < n - 1:
            print(matrix[i][j])
            i += 1
        elif j == m - 1 and i == n - 1:
            print
            
        
    

matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_approach(matrix)