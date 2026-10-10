# -- Create the board for the snake game
def create_board(rows, cols):
    board = []

    for row in range(rows):
        new_row = []

        for col in range(cols):
            new_row.append(0)

        board.append(new_row)

    return board

# -- Create the starting snake on the board
def create_starting_snake(board, start_row, start_col, snake_size, direction):
    for i in range(snake_size):
        value = snake_size - i

        row = start_row
        col = start_col

        if direction == "east":
            col -= i

        elif direction == "west":
            col += i

        elif direction == "north":
            row += i

        elif direction == "south":
            row -= i

        board[row][col] = value

# -- Check if the snake donrt run into itself or the walls
def is_legal_move(pos, board):
    row, col = pos

    if row < 0 or row >= len(board):
        return False

    if col < 0 or col >= len(board[0]):
        return False

    if board[row][col] > 0:
        return False

    return True

# -- Get the next head position based on the current direction
def get_next_head_position(head_pos, direction):
    row, col = head_pos

    if direction == "east":
        col += 1

    elif direction == "west":
        col -= 1

    elif direction == "north":
        row -= 1

    elif direction == "south":
        row += 1

    return (row, col)

# -- Snake movement function
def subtract_one_from_all_positives(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 0:
                grid[row][col] -= 1

# -- Makeing sure the snake can't turn back on itself
def can_change_direction(current_direction, new_direction):
    opposite = {
        "north": "south",
        "south": "north",
        "east": "west",
        "west": "east"
    }

    return new_direction != opposite[current_direction]