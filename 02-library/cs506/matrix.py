

def get_determinant(matrix):
    """
    input: matrix
    output: determinant of matrix
    this function will be handled recursively
    """
    total = 0
    #base case is 2x2 matrix
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    #need to check if matrix is square
    elif len(matrix) == len(matrix[0]):
        for col_n in range(len(matrix)):
            #remove the top row of the matrix
            sub_matrix = matrix[1:]
            for i in range(len(sub_matrix)):
                #remove the column in which the element we are multiplying with resides
                sub_matrix[i] = sub_matrix[i][0:col_n] + sub_matrix[i][col_n+1:]
            
        #get determinant of sub matrix
        sub_determinant = get_determinant(sub_matrix)

        #the total of each call will be the element from the top row multiplied by the determinant of the sub matrix
        #we then need to decide if we are adding it or subtracting it depending on whether it is an odd or even column number
        sign = (-1) ** col_n
        total += sign * matrix[0][col_n] * sub_determinant

        return total

    #if matrix is not square; raise input errer
    else:
        raise ValueError("Input matrices must be square")
