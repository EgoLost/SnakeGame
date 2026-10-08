import random
from snake_view import (draw_board, draw_game_info, draw_game_background, get_board_box)
from snake_menu import (
    draw_menu,
    menu_mouse_pressed,
    menu_mouse_moved,
    menu_key_pressed,
    draw_levels,
    levels_mouse_pressed,
    levels_mouse_moved,
    draw_store,
    store_mouse_pressed,
    draw_settings,
    settings_mouse_pressed,
    draw_gameover,
    gameover_mouse_pressed,
    draw_pause,
    pause_mouse_pressed,
    gameover_mouse_moved,
    gameover_key_pressed,
    store_mouse_moved,
    settings_mouse_moved,
    pause_mouse_moved,
)
from load_save import (
    load_config,
    save_config,
    load_default_config,
    reset_settings,
    load_levels,
    load_progress,
    save_progress,
    load_coins,
    save_coins
)

def assign_key(config, action, index, new_key):
    controls = config["controls"]

    for control_action in controls:
        for key_index in range(len(controls[control_action])):
            if controls[control_action][key_index] == new_key:
                controls[control_action][key_index] = ""

    controls[action][index] = new_key

def app_started(app):
    # Config
    app.config = load_config()
    app.changing_control = None
    app.menu_index = 0

    # Game
    app.state = "menu"

    # Gameover
    app.gameover_index = 0

    # Arcade
    app.game_mode = None
    app.arcade_stage = 1
    app.arcade_start_size = 7

    # Level
    app.levels = load_levels()
    app.level_index = 0

    progress = load_progress()
    app.unlocked_level = progress["unlocked_level"]
    app.completed_levels = progress["completed_levels"]

    # Store
    coins_data = load_coins()
    app.coin = coins_data["coins"]

    app._root.state("zoomed")

def reset_game(app):
    load_level(app)

def create_board(rows, cols):
    board = []

    for row in range(rows):
        new_row = []

        for col in range(cols):
            new_row.append(0)

        board.append(new_row)

    return board

def start_arcade(app):
    app.game_mode = "arcade"

    app.arcade_stage = 1

    app.rows = app.arcade_start_size
    app.cols = app.arcade_start_size

    app.goal = 12
    app.score = 0

    app.snake_size = 1

    app.direction = "east"
    app.next_direction = "east"

    app.arcade_speed = 220
    app.timer_delay = app.arcade_speed

    start_row = app.rows // 2
    start_col = app.cols // 2

    app.head_pos = (start_row, start_col)

    app.board = create_board(app.rows, app.cols)

    app.board[start_row][start_col] = 1

    add_apple_at_random_location(app.board)

    app.state = "active"

def load_level(app):
    level = app.levels["levels"][app.level_index]

    app.level = level["level"]
    app.goal = level["goal"]
    app.timer_delay = level["speed"]

    app.rows = level["rows"]
    app.cols = level["cols"]

    app.score = 0
    app.snake_size = level["snake_size"]

    app.direction = level["start_direction"]
    app.next_direction = level["start_direction"]

    start_row = level["start_row"]
    start_col = level["start_col"]

    app.head_pos = (start_row, start_col)
    app.board = create_board(app.rows, app.cols)

    create_starting_snake(app.board, start_row, start_col, app.snake_size, app.direction)

    add_apple_at_random_location(app.board)

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

def start_level(app):
    app.game_mode = "level"
    reset_game(app)
    app.state = "active"

def timer_fired(app):
    if app.state == "active":
        move_snake(app)

    elif app.state == "shrinking":
        shrink_snake(app)

def normalize_key(key):
    if key in ["Enter", "Return"]:
        return "Enter"

    if len(key) == 1:
        return key.lower()

    return key

def key_pressed(app, event):
    key = normalize_key(event.key)

    # Change controls
    if app.changing_control is not None:
        action, index = app.changing_control

        assign_key(app.config, action, index, key)

        save_config(app.config)

        app.changing_control = None

        return

    if app.state == "menu":
        action = menu_key_pressed(app, key)

        if action == "active":
            start_arcade(app)

        elif action == "levels":
            app.state = "levels"

        elif action == "store":
            app.state = "store"

        elif action == "settings":
            app.state = "settings"

        elif action == "exit":
            app._root.destroy()

        return

    if app.state in ["levels", "store", "settings"]:
        if key in ["Escape", "BackSpace"]:
            app.state = "menu"

        return
    
    if app.state == "gameover":
        action = gameover_key_pressed(app, key)

        if action == "restart":
            if app.game_mode == "arcade":
                start_arcade(app)
            else:
                start_level(app)

        elif action == "menu":
            app.state = "menu"

        return

    if app.state == "paused":
        if key in ["Escape", "BackSpace"]:
            app.state = "active"

        return


    if key in app.config["controls"]["restart"]:
        if app.game_mode == "arcade":
            start_arcade(app)
        else:
            start_level(app)

        return

    new_direction = None

    if app.state == "shrinking":
        return

    if key in app.config["controls"]["up"]:
        new_direction = "north"

    elif key in app.config["controls"]["down"]:
        new_direction = "south"

    elif key in app.config["controls"]["left"]:
        new_direction = "west"

    elif key in app.config["controls"]["right"]:
        new_direction = "east"

    if new_direction is not None:
        if can_change_direction(
            app.direction,
            new_direction
        ):
            app.next_direction = new_direction

    elif key in ["Escape", "BackSpace"]:
        app.state = "paused"

def add_coin_at_random_location(grid):
    free_positions = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                free_positions.append((row, col))

    if len(free_positions) > 0:
        row, col = random.choice(free_positions)
        grid[row][col] = -2

def finish_level(app):
    current_level = app.level_index + 1

    if current_level not in app.completed_levels:
        app.completed_levels.append(current_level)

    if current_level == app.unlocked_level:
        if app.unlocked_level < len(app.levels["levels"]):
            app.unlocked_level += 1

    save_progress(app)

    app.state = "levels"

def reset_progress(app):
    app.unlocked_level = 1
    app.completed_levels = []

    save_progress(app)

def mouse_moved(app, event):
    pointer = False

    if app.state == "menu":
        pointer = menu_mouse_moved(app, event)

    elif app.state == "levels":
        pointer = levels_mouse_moved(app, event)

    elif app.state == "store":
        pointer = store_mouse_moved(app, event)

    elif app.state == "settings":
        pointer = settings_mouse_moved(app, event)

    elif app.state == "paused":
        pointer = pause_mouse_moved(app, event)

    elif app.state == "gameover":
        pointer = gameover_mouse_moved(app, event)

    if pointer:
        app._root.config(cursor="hand2")
    else:
        app._root.config(cursor="")

def mouse_pressed(app, event):

    if app.state == "menu":
        action = menu_mouse_pressed(app, event)

        if action == "active":
            start_arcade(app)

        elif action == "levels":
            app.state = "levels"

        elif action == "store":
            app.state = "store"

        elif action == "settings":
            app.state = "settings"

        elif action == "exit":
            app._root.destroy()

        return


    elif app.state == "levels":
        action = levels_mouse_pressed(app, event)

        if action == "back":
            app.state = "menu"

        elif action == "start_level":
            start_level(app)

        elif action == "reset":
            reset_progress(app)

        return


    elif app.state == "store":
        action = store_mouse_pressed(app, event)

        if action == "back":
            app.state = "menu"

        return


    elif app.state == "settings":
        action = settings_mouse_pressed(app, event)

        if action == "reset":
            reset_settings(app)

        elif action == "back":
            app.state = "menu"

        return


    elif app.state == "paused":
        action = pause_mouse_pressed(app, event)

        if action == "continue":
            app.state = "active"

        elif action == "menu":
            app.state = "menu"

        return

    elif app.state == "gameover":
        action = gameover_mouse_pressed(app, event)

        if action == "restart":
            if app.game_mode == "arcade":
                start_arcade(app)
            else:
                start_level(app)

        elif action == "menu":
            app.state = "menu"

        return

def is_legal_move(pos, board):
    row, col = pos

    if row < 0 or row >= len(board):
        return False

    if col < 0 or col >= len(board[0]):
        return False

    if board[row][col] > 0:
        return False

    return True

def add_apple_at_random_location(grid):
    free_positions = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                free_positions.append((row, col))

    if len(free_positions) > 0:
        row, col = random.choice(free_positions)

        grid[row][col] = -1

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

def subtract_one_from_all_positives(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 0:
                grid[row][col] -= 1

def can_change_direction(current_direction, new_direction):
    opposite = {
        "north": "south",
        "south": "north",
        "east": "west",
        "west": "east"
    }

    return new_direction != opposite[current_direction]

def move_snake(app):
    app.direction = app.next_direction

    next_pos = get_next_head_position(app.head_pos, app.direction)

    if not is_legal_move(next_pos, app.board):
        app.gameover_index = 0
        app.state = "gameover"
        return

    app.head_pos = next_pos
    row, col = app.head_pos

    if app.board[row][col] == -1:
        app.snake_size += 1
        app.score += 1

        app.board[row][col] = app.snake_size

        if app.score >= app.goal:
            if app.game_mode == "arcade":
                app.timer_delay = 100
                app.state = "shrinking"
                return
            else:
                finish_level(app)
                return

        add_apple_at_random_location(app.board)

        if random.randint(1, 100) <= 20:
            add_coin_at_random_location(app.board)

    elif app.board[row][col] == -2:
        app.coin += 1
        save_coins(app.coin)

        subtract_one_from_all_positives(app.board)
        app.board[row][col] = app.snake_size

    else:
        subtract_one_from_all_positives(app.board)
        app.board[row][col] = app.snake_size

def start_next_arcade_stage(app):
    app.arcade_stage += 1

    if app.rows < 14:
        app.rows += 1
        app.cols += 1

    else:
        if app.arcade_speed > 80:
            app.arcade_speed -= 10

    app.timer_delay = app.arcade_speed

    app.score = 0
    app.goal += 3

    app.snake_size = 1

    app.direction = "east"
    app.next_direction = "east"

    start_row = app.rows // 2
    start_col = app.cols // 2

    app.head_pos = (start_row, start_col)
    app.board = create_board(app.rows,app.cols)
    app.board[start_row][start_col] = 1

    add_apple_at_random_location(app.board)

    app.state = "active"

def shrink_snake(app):
    subtract_one_from_all_positives(app.board)

    app.snake_size -= 1

    if app.snake_size <= 1:
        start_next_arcade_stage(app)

def redraw_all(app, canvas):

    if app.state == "menu":
        draw_menu(app, canvas)
        return

    if app.state == "levels":
        draw_levels(app, canvas)
        return

    if app.state == "store":
        draw_store(app, canvas)
        return

    if app.state == "settings":
        draw_settings(app, canvas)
        return

    if app.state == "gameover":
        draw_gameover(app, canvas)
        return

    if app.state == "paused":
        draw_game_background(app, canvas)

        x1, y1, x2, y2 = get_board_box(app)

        draw_board(
            canvas,
            x1,
            y1,
            x2,
            y2,
            app.board,
            app.direction
        )

        draw_game_info(canvas, app)
        draw_pause(app, canvas)

        return

    if app.state == "active" or app.state == "shrinking":
        draw_game_background(app, canvas)

        x1, y1, x2, y2 = get_board_box(app)

        draw_board(
            canvas,
            x1,
            y1,
            x2,
            y2,
            app.board,
            app.direction
        )

        draw_game_info(canvas, app)

    

if __name__ == "__main__":
    from uib_inf100_graphics.event_app import run_app

    run_app(width=1200, height=800, title="Snake game")