"""
Page 73

write an algorithm such that if an element in an MxN matrix is 0, its entire row and column and set to 0

ans: pg 180
"""

def set_zero(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0])

    rows_to_zero = []
    cols_to_zero = []

    for i in range(rows):
        for j in range(cols):
	    if matrix[i][j] == 0:
	        rows_to_zero.append(i)
		cols_to_zero.append(j)

    for row in rows_to_zero:
        for col in range(cols):
	    matrix[row][col] = 0

    for col in cols_to_zero:
        for row in range(rows):
	    matrix[row][col] = 0

    return matrix

print set_zero([[1,2,0], [2,1,1], [3,1,0]])
    
