# to be continued...
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def rotate_path(matrix, visited, direction):
    
    global directions
    rows = len(matrix)
    columns = len(matrix[1])
    
    next_cell = get_next(visited, direction)

    if next_cell[0] > rows - 1 or next_cell[1] > columns - 1:
        direction = (direction + 1) % 4
        return rotate_path(matrix, visited, direction)

    if next_cell in visited:
        direction = (direction + 1) % 4
        if get_next(visited, direction) in visited:
            return visited
        return rotate_path(matrix, visited, direction)

    visited.append(next_cell)
    return rotate_path(matrix, visited, direction)


def get_next(visited, direction):

    global directions
    new_cell_row = visited[-1][0] + directions[direction][0]
    new_cell_col = visited[-1][1] + directions[direction][1]

    return new_cell_row, new_cell_col

print rotate_path([[1, 2], [1, 23]], [(0, 0)], 0)


