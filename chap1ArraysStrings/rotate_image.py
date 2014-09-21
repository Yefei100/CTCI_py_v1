"""
Page 73

Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

ans: pg 179
"""

# layer by layer

def matrix_rotate(matrix, N):
    """
    assume that the matrix is rotated to the right
    """

    for layer in range(N/2):
        last_col = N - 1 - layer
        for col_idx in range(layer, last_col):
	    # copy the top value
	    top = matrix[layer][col_idx]

	    # rotate the left to the top
            matrix[layer][col_idx] = matrix[N-1-col_idx][layer]

	    # rotate the bottom to the left
	    matrix[N-1-col_idx][layer] = matrix[N-1-layer][N-1-col_idx]

	    # rotate the right to the bottom
	    matrix[N-1-layer][N-1-col_idx] = matrix[col_idx][N-1-layer]

	    # rotate the top to the right
	    matrix[col_idx][N-1-layer] = top

    return matrix

print matrix_rotate([[1, 2], [3, 4]], 2)
print matrix_rotate([[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]], 4)
