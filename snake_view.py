from uib_inf100_graphics.helpers import load_image, image_in_box

snake_head_up = load_image("source/img/Snake_head.png")
snake_head_down = load_image("source/img/Snake_head_down.png")
snake_head_left = load_image("source/img/Snake_head_left.png")
snake_head_right = load_image("source/img/Snake_head_right.png")

snake_body_vertical = load_image("source/img/Snake_body.png")
snake_body_horizontal = load_image("source/img/Snake_body_horizontal.png")

snake_tail_up = load_image("source/img/Snake_tail.png")
snake_tail_down = load_image("source/img/Snake_tail_down.png")
snake_tail_left = load_image("source/img/Snake_tail_left.png")
snake_tail_right = load_image("source/img/Snake_tail_right.png")

snake_turn_top_right = load_image("source/img/Snake_turn.png")
snake_turn_right_down = load_image("source/img/Snake_turn_right_down.png")
snake_turn_down_left = load_image("source/img/Snake_turn_down_left.png")
snake_turn_left_top = load_image("source/img/Snake_turn_left_top.png")

apple = load_image("source/img/apple.png")
coin = load_image("source/img/coin.png")
floor = load_image("source/img/floor.png")
game_fon = load_image("source/img/fon_game.png")

def draw_game_background(app, canvas):
    image_in_box(
        canvas,
        0,
        0,
        app.width,
        app.height,
        game_fon,
        fit_mode="stretch"
    )

def get_board_box(app):
    x1 = app.width * 0.048
    y1 = app.height * 0.078

    x2 = app.width * 0.567
    y2 = app.height * 0.896

    return x1, y1, x2, y2

def draw_board(canvas, x1, y1, x2, y2, board, direction):
    lines_amount = len(board)
    columns_amount = len(board[0])

    cell_width = (x2 - x1) / columns_amount
    cell_height = (y2 - y1) / lines_amount

    biggest = get_biggest_value(board)

    for row in range(lines_amount):
        y_one = y1 + cell_height * row
        y_two = y_one + cell_height

        for col in range(columns_amount):
            x_one = x1 + cell_width * col
            x_two = x_one + cell_width

            value = board[row][col]
            image_in_box(
                canvas,
                x_one,
                y_one,
                x_two,
                y_two,
                floor,
                fit_mode="stretch"
            )

            if value == -1:
                image_in_box(
                    canvas,
                    x_one,
                    y_one,
                    x_two,
                    y_two,
                    apple
                )

            elif value == -2:
                image_in_box(
                    canvas,
                    x_one,
                    y_one,
                    x_two,
                    y_two,
                    coin
                )
            else:
                image = get_snake_image(board, row, col, biggest, direction)

                if image is not None:
                    image_in_box(canvas, x_one, y_one, x_two, y_two, image, fit_mode="stretch")


def draw_game_info(canvas, app):
    scale = min(
        app.width / 1200,
        app.height / 800
    )

    if app.game_mode == "arcade":
        title = "STAGE"
        number = app.arcade_stage
    else:
        title = "LEVEL"
        number = app.level

    info_x = 1220 * scale

    title_font = (
        "Georgia",
        int(30 * scale),
        "bold"
    )

    number_font = (
        "Georgia",
        int(25 * scale),
        "bold"
    )

    main_color = "#4a2a12"
    shadow_color = "#d5a84c"

    canvas.create_text(
        info_x + 2 * scale,
        151 * scale + 2 * scale,
        text=title,
        font=title_font,
        fill=shadow_color
    )

    canvas.create_text(
        info_x,
        151 * scale,
        text=title,
        font=title_font,
        fill=main_color
    )

    canvas.create_text(
        info_x,
        190 * scale,
        text=str(number),
        font=number_font,
        fill=main_color
    )

    canvas.create_text(
        info_x + 2 * scale,
        250 * scale + 2 * scale,
        text="GOAL",
        font=title_font,
        fill=shadow_color
    )

    canvas.create_text(
        info_x,
        250 * scale,
        text="GOAL",
        font=title_font,
        fill=main_color
    )

    canvas.create_text(
        info_x,
        295 * scale,
        text=f"{app.score} / {app.goal}",
        font=number_font,
        fill=main_color
    )

    coin_y = 598 * scale
    coin_size = 55 * scale

    coin_x1 = 1180 * scale
    coin_y1 = coin_y - coin_size / 2

    coin_x2 = coin_x1 + coin_size
    coin_y2 = coin_y + coin_size / 2

    image_in_box(
        canvas,
        coin_x1,
        coin_y1,
        coin_x2,
        coin_y2,
        coin,
        fit_mode="stretch"
    )

    canvas.create_text(
        coin_x2 + 15 * scale,
        coin_y,
        text=str(app.coin),
        font=("Georgia", int(25 * scale), "bold"),
        fill=main_color,
        anchor="w"
    )


def get_biggest_value(board):
    biggest = 0

    for row in board:
        for value in row:
            if value > biggest:
                biggest = value

    return biggest


def find_neighbor(board, row, col, value):
    if row > 0 and board[row - 1][col] == value:
        return row - 1, col

    if row < len(board) - 1 and board[row + 1][col] == value:
        return row + 1, col

    if col > 0 and board[row][col - 1] == value:
        return row, col - 1

    if col < len(board[0]) - 1 and board[row][col + 1] == value:
        return row, col + 1

    return None


def get_direction(row, col, other_row, other_col):
    if other_row < row:
        return "north"

    if other_row > row:
        return "south"

    if other_col < col:
        return "west"

    if other_col > col:
        return "east"


def get_snake_image(board, row, col, biggest, direction):
    value = board[row][col]

    if value <= 0:
        return None

    if value == biggest:
        return get_head_image(board, row, col, biggest, direction)

    if value == 1:
        return get_tail_image(board, row, col)

    return get_body_image(board, row, col)


def get_head_image(board, row, col, biggest, snake_direction):

    if biggest == 1:
        if snake_direction == "north":
            return snake_head_up

        if snake_direction == "south":
            return snake_head_down

        if snake_direction == "west":
            return snake_head_left

        if snake_direction == "east":
            return snake_head_right

    neck = find_neighbor(board, row, col, biggest - 1)

    if neck is None:
        return snake_head_right

    neck_row, neck_col = neck

    direction = get_direction(row, col, neck_row, neck_col)

    if direction == "south":
        return snake_head_up

    if direction == "north":
        return snake_head_down

    if direction == "west":
        return snake_head_right

    if direction == "east":
        return snake_head_left


def get_tail_image(board, row, col):
    body = find_neighbor(board, row, col, 2)

    if body is None:
        return snake_tail_up

    body_row, body_col = body
    direction = get_direction(row, col, body_row, body_col)

    if direction == "south":
        return snake_tail_up

    if direction == "north":
        return snake_tail_down

    if direction == "west":
        return snake_tail_right

    if direction == "east":
        return snake_tail_left


def get_body_image(board, row, col):
    value = board[row][col]

    previous_part = find_neighbor(board, row, col, value - 1)
    next_part = find_neighbor(board, row, col, value + 1)

    if previous_part is None or next_part is None:
        return snake_body_vertical

    previous_row, previous_col = previous_part
    next_row, next_col = next_part

    direction_one = get_direction(row, col, previous_row, previous_col)
    direction_two = get_direction(row, col, next_row, next_col)

    if (direction_one == "north" and direction_two == "south"):
        return snake_body_vertical

    if (direction_one == "south" and direction_two == "north"):
        return snake_body_vertical

    if (direction_one == "east" and direction_two == "west"):
        return snake_body_horizontal

    if (direction_one == "west" and direction_two == "east"):
        return snake_body_horizontal

    return get_turn_image(direction_one, direction_two) 

def get_turn_image(direction_one, direction_two):
    if (direction_one == "north" 
        and direction_two == "east") or (direction_one == "east" 
                                         and direction_two == "north"):
        return snake_turn_top_right

    if (direction_one == "east" 
        and direction_two == "south") or (direction_one == "south" 
                                          and direction_two == "east"
    ):
        return snake_turn_right_down

    if (
        direction_one == "south"
        and direction_two == "west") or (direction_one == "west"
                                         and direction_two == "south"):
        return snake_turn_down_left

    if (
        direction_one == "west"
        and direction_two == "north") or (direction_one == "north"
                                          and direction_two == "west"):
        return snake_turn_left_top

    return snake_body_vertical