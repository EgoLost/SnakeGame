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
coin_container = load_image("source/img/coin_container.png")
coin = load_image("source/img/coin.png")
floor = load_image("source/img/floor.png")
game_fon = load_image("source/img/fon_game.png")

extra_life = load_image("source/img/heart.png")
meat = load_image("source/img/meat.png")

def draw_game_background(app, canvas):
    image_in_box(
        canvas,
        0,
        0,
        app.width,
        app.height,
        game_fon,
        fit_mode="stretch",
        antialias=False
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

    positions = {}

    for row in range(lines_amount):
        for col in range(columns_amount):
            value = board[row][col]

            if value > 0:
                positions[value] = (row, col)

    if len(positions) > 0:
        biggest = max(positions)
    else:
        biggest = 0

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
                fit_mode="stretch",
                antialias=False
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

            elif value == -3:
                image_in_box(
                    canvas,
                    x_one,
                    y_one,
                    x_two,
                    y_two,
                    meat
                )

            elif value > 0:
                image = get_snake_image(
                    board,
                    positions,
                    row,
                    col,
                    biggest,
                    direction
                )

                image_in_box(
                    canvas,
                    x_one,
                    y_one,
                    x_two,
                    y_two,
                    image,
                    fit_mode="stretch",
                    antialias=False
                )


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

    if (
    app.game_mode == "arcade"
    and app.upgrades["extra_life"]["bought"]
    and app.extra_life_available):
        life_size = 80 * scale

        life_x1 = info_x - life_size / 2
        life_y1 = 360 * scale

        life_x2 = life_x1 + life_size
        life_y2 = life_y1 + life_size

        canvas.create_text(
            info_x,
            345 * scale,
            text="EXTRA LIFE",
            font=("Georgia", int(18 * scale), "bold"),
            fill=main_color
        )

        image_in_box(
            canvas,
            life_x1,
            life_y1,
            life_x2,
            life_y2,
            extra_life
        )

    container_width = 360 * scale
    container_height = 110 * scale

    container_x1 = info_x - container_width / 2
    container_y1 = 575 * scale

    container_x2 = container_x1 + container_width
    container_y2 = container_y1 + container_height

    image_in_box(
        canvas,
        container_x1,
        container_y1,
        container_x2,
        container_y2,
        coin_container,
        fit_mode="stretch"
    )

    coin_size = 42 * scale

    coin_x1 = container_x1 + 100 * scale

    coin_y1 = (
        container_y1
        + container_height / 2
        - coin_size / 2
    )

    coin_x2 = coin_x1 + coin_size
    coin_y2 = coin_y1 + coin_size

    image_in_box(
        canvas,
        coin_x1,
        coin_y1,
        coin_x2,
        coin_y2,
        coin,
        fit_mode="stretch"
    )

    text_x = coin_x2 + 28 * scale
    text_y = container_y1 + container_height / 2 - 3 * scale

    coin_font = (
        "Georgia",
        int(36 * scale),
        "bold"
    )

    canvas.create_text(
        text_x + 3 * scale,
        text_y + 3 * scale,
        text=str(app.coin),
        font=coin_font,
        fill="#3b210d",
        anchor="w"
    )

    canvas.create_text(
        text_x,
        text_y,
        text=str(app.coin),
        font=coin_font,
        fill="#f5d56b",
        anchor="w"
    )


def get_direction(row, col, other_row, other_col):
    if other_row < row:
        return "north"

    if other_row > row:
        return "south"

    if other_col < col:
        return "west"

    if other_col > col:
        return "east"


def get_snake_image(
    board,
    positions,
    row,
    col,
    biggest,
    direction
):
    value = board[row][col]

    if value == biggest:
        return get_head_image(direction)

    if value == 1:
        return get_tail_image(
            positions
        )

    return get_body_image(
        positions,
        value
    )


def get_head_image(direction):
    if direction == "north":
        return snake_head_up

    if direction == "south":
        return snake_head_down

    if direction == "west":
        return snake_head_left

    return snake_head_right


def get_tail_image(positions):
    if 2 not in positions:
        return snake_tail_up

    tail_row, tail_col = positions[1]
    body_row, body_col = positions[2]

    direction = get_direction(
        tail_row,
        tail_col,
        body_row,
        body_col
    )

    if direction == "south":
        return snake_tail_up

    if direction == "north":
        return snake_tail_down

    if direction == "west":
        return snake_tail_right

    return snake_tail_left


def get_body_image(positions, value):
    if value - 1 not in positions:
        return snake_body_vertical

    if value + 1 not in positions:
        return snake_body_vertical

    row, col = positions[value]

    previous_row, previous_col = positions[
        value - 1
    ]

    next_row, next_col = positions[
        value + 1
    ]

    direction_one = get_direction(
        row,
        col,
        previous_row,
        previous_col
    )

    direction_two = get_direction(
        row,
        col,
        next_row,
        next_col
    )

    if {
        direction_one,
        direction_two
    } == {"north", "south"}:
        return snake_body_vertical

    if {
        direction_one,
        direction_two
    } == {"east", "west"}:
        return snake_body_horizontal

    return get_turn_image(
        direction_one,
        direction_two
    )

def get_turn_image(direction_one, direction_two):
    directions = {direction_one, direction_two}

    if directions == {"north", "east"}:
        return snake_turn_top_right

    if directions == {"east", "south"}:
        return snake_turn_right_down

    if directions == {"south", "west"}:
        return snake_turn_down_left

    if directions == {"west", "north"}:
        return snake_turn_left_top

    if directions == {"north", "south"}:
        return snake_body_vertical

    return snake_body_horizontal