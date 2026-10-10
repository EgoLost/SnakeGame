from snake_game import (
    create_board,
    create_starting_snake,
    subtract_one_from_all_positives
)

from snake_food import (
    add_apple_at_random_location
)

# -- Start the arcade mode
def start_arcade(app):
    app.game_mode = "arcade"

    # -- Check if the player has the extra life upgrade
    app.extra_life_available = (
        app.upgrades["extra_life"]["bought"])

    # -- Reset the arcade stage and game settings to the starting values
    app.arcade_stage = 1
    app.rows = app.arcade_start_size
    app.cols = app.arcade_start_size
    app.goal = 12
    app.score = 0
    app.snake_size = 2
    app.arcade_stage_start_snake_size = app.snake_size
    app.direction = "east"
    app.next_direction = "east"
    app.arcade_speed = 220
    start_row = app.rows // 2
    start_col = app.cols // 2
    app.head_pos = (start_row, start_col)

    # -- Set the timer delay and speed mode to normal
    app.base_timer_delay = app.arcade_speed
    app.timer_delay = app.base_timer_delay
    app.speed_up_held = False
    app.slow_down_held = False

    # -- Create the board and place an apple
    app.board = create_board(app.rows, app.cols)
    app.board[start_row][start_col] = 2
    add_apple_at_random_location(app.board)

    app.state = "active"

# -- Restart the current arcade stage
def restart_current_arcade_stage(app):
    app.score = 0

    app.snake_size = app.arcade_stage_start_snake_size

    app.direction = "east"
    app.next_direction = "east"

    app.speed_up_held = False
    app.slow_down_held = False

    app.timer_delay = app.base_timer_delay

    start_row = app.rows // 2
    start_col = app.cols // 2

    app.head_pos = (start_row, start_col)

    app.board = create_board(
        app.rows,
        app.cols
    )

    create_starting_snake(
        app.board,
        start_row,
        start_col,
        app.snake_size,
        app.direction
    )

    add_apple_at_random_location(app.board)

    app.state = "active"

# -- Start the next arcade stage
def start_next_arcade_stage(app):
    app.arcade_stage += 1

    if app.rows < 12:
        app.rows += 1
        app.cols += 1

    else:
        if app.arcade_speed > 80:
            app.arcade_speed -= 10

    app.base_timer_delay = app.arcade_speed
    app.timer_delay = app.base_timer_delay

    app.speed_up_held = False
    app.slow_down_held = False

    app.score = 0
    app.goal += 3

    app.snake_size = 2
    app.arcade_stage_start_snake_size = app.snake_size

    app.direction = "east"
    app.next_direction = "east"

    start_row = app.rows // 2
    start_col = app.cols // 2

    app.head_pos = (start_row, start_col)
    app.board = create_board(app.rows,app.cols)
    app.board[start_row][start_col] = 2

    add_apple_at_random_location(app.board)

    app.state = "active"

# -- Shrink the snake by one unit
def shrink_snake(app):
    subtract_one_from_all_positives(app.board)

    app.snake_size -= 1

    if app.snake_size <= 1:
        start_next_arcade_stage(app)