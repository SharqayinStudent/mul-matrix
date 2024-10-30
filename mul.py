def matrix_multiply(A, B):
    
    a_rows, a_cols = len(A), len(A[0])
    b_rows, b_cols = len(B), len(B[0])

    
    if a_cols != b_rows:
        print("Number of columns in A must be equal to number of rows in B")

    
    result = [[0] * b_cols for _ in range(a_rows)]

   
    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(a_cols):
                result[i][j] += A[i][k] * B[k][j]

    return result
