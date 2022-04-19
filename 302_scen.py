#find maximal value in matrix `matrix`


def find_max(matrix): 
    max = matrix[0][0] 
    for i in range(len(matrix)): 
        for j in range(len(matrix[0])): 
            if matrix[i][j] > max: 
                max = matrix[i][j] 
    return max