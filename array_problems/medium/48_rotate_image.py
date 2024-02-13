def first_approach(image):
    layer = 0
    
    # Transposing a matrix and reversing it

    # Transposing a matrix
    n, m = len(image), len(image[0])
    for i in range(n):
        for j in range(i, m):
            image[i][j], image[j][i] = image[j][i] ,image[i][j]

    # Reversing the rows of the matrix
    for i in range(n):
        image[i] = image[i][::-1]
    print(image)


image =[[1,2,3],[4,5,6],[7,8,9]]
first_approach(image)        