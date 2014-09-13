def zero_cr(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row_with_zeros = [False for x in range(m)]
    col_with_zeros = [False for x in range(n)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row_with_zeros[i] = True
                col_with_zeros[j] = True

    for i in range(m):
        for j in range(n):
            if row_with_zeros[i] or col_with_zeros[j]:
                matrix[i][j] = 0
