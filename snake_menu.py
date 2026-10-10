from uib_inf100_graphics.helpers import load_image, image_in_box

unknown_icon = load_image("source/img/store/unknown.png")

speed_up_icon = load_image("source/img/store/speed_up.png")
slow_down_icon = load_image("source/img/store/slow_down.png")
extra_life_icon = load_image("source/img/store/buy_heart.png")
coin_chance_icon = load_image("source/img/store/coin_upchance.png")
meat_icon = load_image("source/img/store/buy_meat.png")
floor_selection_icon = load_image("source/img/store/board_buy.png")

back = load_image("source/img/back.png")
title = load_image("source/img/Title.png")
fon = load_image("source/img/fon.png")

left_arrow = load_image("source/img/left_arrow.png")
right_arrow = load_image("source/img/right_arrow.png")

arcade_button = load_image("source/img/arcade.png")
levels_button = load_image("source/img/levels.png")
store_button = load_image("source/img/store.png")
settings_button = load_image("source/img/settings.png")

restart_button = load_image("source/img/restart.png")
continue_button = load_image("source/img/continue.png")
menu_button = load_image("source/img/menu.png")
reset_button = load_image("source/img/reset.png")
exit_button = load_image("source/img/exit.png")

gameover_fon = load_image("source/img/gameover_fon.png")
gameover_title = load_image("source/img/gameover_title.png")

settings_fon = load_image("source/img/settings_fon.png")
settings_title = load_image("source/img/settings_title.png")

levels_title = load_image("source/img/levels_title.png")
levels_fon = load_image("source/img/levels_fon.png")
lock = load_image("source/img/lock.png")

pause_fon = load_image("source/img/pause_fon.png")
pause_title = load_image("source/img/Pause.png")

coin = load_image("source/img/coin.png")
coin_container = load_image("source/img/coin_container.png")
shop_fon = load_image("source/img/shop_fon.png")


def get_button_image(action):
    if action == "active":
        return arcade_button

    if action == "levels":
        return levels_button

    if action == "store":
        return store_button

    if action == "settings":
        return settings_button

    if action == "restart":
        return restart_button

    if action == "menu":
        return menu_button

    if action == "continue":
        return continue_button

    if action == "reset":
        return reset_button

    if action == "exit":
        return exit_button

    return None

def get_scale(app):
    scale_x = app.width / 1200
    scale_y = app.height / 800

    return min(scale_x, scale_y)

def draw_selected_arrows(app, canvas, button):
    scale = get_scale(app)

    arrow_width = 105 * scale
    arrow_height = 80 * scale
    gap = 0

    center_y = (button["y1"] + button["y2"]) / 2

    image_in_box(
        canvas,
        button["x1"] - gap - arrow_width,
        center_y - arrow_height / 2,
        button["x1"] - gap,
        center_y + arrow_height / 2,
        right_arrow
    )

    image_in_box(
        canvas,
        button["x2"] + gap,
        center_y - arrow_height / 2,
        button["x2"] + gap + arrow_width,
        center_y + arrow_height / 2,
        left_arrow
    )

def get_menu_buttons(app):
    scale = get_scale(app)

    button_width = 250 * scale
    button_height = 70 * scale
    gap = 5 * scale

    center_x = app.width / 2

    x1 = center_x - button_width / 2
    x2 = center_x + button_width / 2

    buttons_amount = 5

    total_height = (button_height * buttons_amount + gap * (buttons_amount - 1))
    start_y = app.height / 2 - total_height / 2
    start_y += 35 * scale

    return [
        {
            "text": "ARCADE",
            "x1": x1,
            "y1": start_y,
            "x2": x2,
            "y2": start_y + button_height,
            "action": "active"
        },
        {
            "text": "LEVELS",
            "x1": x1,
            "y1": start_y + (button_height + gap),
            "x2": x2,
            "y2": start_y + (button_height + gap) + button_height,
            "action": "levels"
        },
        {
            "text": "STORE",
            "x1": x1,
            "y1": start_y + (button_height + gap) * 2,
            "x2": x2,
            "y2": start_y + (button_height + gap) * 2 + button_height,
            "action": "store"
        },
        {
            "text": "SETTINGS",
            "x1": x1,
            "y1": start_y + (button_height + gap) * 3,
            "x2": x2,
            "y2": start_y + (button_height + gap) * 3 + button_height,
            "action": "settings"
        },
        {
            "text": "EXIT",
            "x1": x1,
            "y1": start_y + (button_height + gap) * 4,
            "x2": x2,
            "y2": start_y + (button_height + gap) * 4 + button_height,
            "action": "exit"
        }
    ]

def get_back_button(app):
    scale = get_scale(app)

    button_size = 60 * scale
    margin = 25 * scale

    x2 = app.width - margin
    x1 = x2 - button_size

    y2 = app.height - margin
    y1 = y2 - button_size

    return {
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2
    }

def draw_button(app, canvas, button):
    image = get_button_image(button["action"])

    if image is not None:
        image_in_box(
            canvas,
            button["x1"],
            button["y1"],
            button["x2"],
            button["y2"],
            image
        )
    else:
        canvas.create_rectangle(
            button["x1"],
            button["y1"],
            button["x2"],
            button["y2"],
            fill="lightgray",
            outline="black",
            width=2
        )

        canvas.create_text(
            (button["x1"] + button["x2"]) / 2,
            (button["y1"] + button["y2"]) / 2,
            text=button["text"],
            font=("Arial", 18, "bold")
        )

def is_inside_button(x, y, button):
    return (
        button["x1"] <= x <= button["x2"]
        and button["y1"] <= y <= button["y2"]
    )

def get_levels_back_button(app):
    scale = get_scale(app)
    button_width = 300 * scale
    button_height = 70 * scale

    x1 = app.width / 2 - button_width / 2
    x2 = app.width / 2 + button_width / 2

    y1 = app.height - 100
    y2 = y1 + button_height

    return {
        "image": back,
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2
    }

def draw_menu(app, canvas):
    scale = get_scale(app)
    image_in_box(canvas, 0, 0, app.width, app.height, fon, fit_mode="stretch")

    logo_width = 600 * scale
    logo_height = 200 * scale

    logo_x1 = app.width / 2 - logo_width / 2
    logo_y1 = 25 * scale

    logo_x2 = app.width / 2 + logo_width / 2
    logo_y2 = logo_y1 + logo_height

    image_in_box(canvas, logo_x1, logo_y1, logo_x2, logo_y2, title)

    buttons = get_menu_buttons(app)

    for i in range(len(buttons)):
        button = buttons[i]
        draw_button(app, canvas, button)

        if i == app.menu_index:
            draw_selected_arrows(app, canvas, button)


def menu_mouse_pressed(app, event):

    buttons = get_menu_buttons(app)

    for i in range(len(buttons)):
        button = buttons[i]

        if is_inside_button(event.x, event.y, button):
            app.menu_index = i
            return button["action"]
    return None

def menu_mouse_moved(app, event):
    buttons = get_menu_buttons(app)

    for i in range(len(buttons)):
        button = buttons[i]

        if is_inside_button(event.x, event.y, button):
            app.menu_index = i
            return button["action"]

    return None

def menu_key_pressed(app, key):
    buttons = get_menu_buttons(app)

    if key == "Up":
        app.menu_index -= 1

        if app.menu_index < 0:
            app.menu_index = len(buttons) - 1

        app.hover_sound.play()

    elif key == "Down":
        app.menu_index += 1

        if app.menu_index >= len(buttons):
            app.menu_index = 0

        app.hover_sound.play()

    elif key == "Enter":
        app.click_sound.play()
        return buttons[app.menu_index]["action"]

    return None

# \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/
# LEVELS
# \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/

def get_level_buttons(app):
    button_width = 120
    button_height = 50
    gap = 20

    total_width = button_width * 3 + gap * 2
    start_x = app.width / 2 - total_width / 2

    y1 = app.height / 2 - button_height / 2
    y2 = y1 + button_height

    return [
        {
            "level": 1,
            "x1": start_x,
            "y1": y1,
            "x2": start_x + button_width,
            "y2": y2
        },
        {
            "level": 2,
            "x1": start_x + button_width + gap,
            "y1": y1,
            "x2": start_x + button_width * 2 + gap,
            "y2": y2
        },
        {
            "level": 3,
            "x1": start_x + (button_width + gap) * 2,
            "y1": y1,
            "x2": start_x + (button_width + gap) * 2 + button_width,
            "y2": y2
        }
    ]

def draw_levels(app, canvas):
    scale_x = app.width / 1200
    scale_y = app.height / 800
    scale = min(scale_x, scale_y)

    image_in_box(
        canvas,
        0,
        0,
        app.width,
        app.height,
        levels_fon,
        fit_mode="stretch"
    )

    title_width = 520 * scale
    title_height = 160 * scale

    title_x1 = app.width / 2 - title_width / 2
    title_y1 = 25 * scale

    title_x2 = app.width / 2 + title_width / 2
    title_y2 = title_y1 + title_height

    image_in_box(
        canvas,
        title_x1,
        title_y1,
        title_x2,
        title_y2,
        levels_title
    )

    levels_count = len(app.levels["levels"])

    for i in range(levels_count):
        level_number = i + 1

        x, y = get_level_position(app, level_number)

        if level_number in app.completed_levels:
            font_size = int(34 * scale)

            canvas.create_text(
                x,
                y,
                text=str(level_number),
                font=("Georgia", font_size, "bold"),
                fill="#00ff88",
                anchor="center"
            )

        elif level_number <= app.unlocked_level:
            font_size = int(34 * scale)

            canvas.create_text(
                x,
                y,
                text=str(level_number),
                font=("Georgia", font_size, "bold"),
                fill="#f1d58a",
                anchor="center"
            )
        else:
            lock_size = 100 * scale

            image_in_box(
                canvas,
                x - lock_size / 2,
                y - lock_size / 2,
                x + lock_size / 2,
                y + lock_size / 2,
                lock,
                fit_mode="stretch"
            )
            
    reset_button = get_reset_levels_button(app)
    draw_button(app, canvas, reset_button)

    draw_back_button(app, canvas)

def get_back_button(app):
    button_size = 90
    margin = 25

    x2 = app.width - margin
    x1 = x2 - button_size

    y2 = app.height - margin
    y1 = y2 - button_size

    return {
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2
    }

def draw_back_button(app, canvas):
    button = get_back_button(app)

    image_in_box(canvas, button["x1"], button["y1"], button["x2"], button["y2"], back, fit_mode="stretch")

def get_level_position(app, level_number):
    positions = {
        1:  (0.087, 0.300),
        2:  (0.172, 0.300),
        3:  (0.259, 0.300),
        4:  (0.346, 0.300),
        5:  (0.433, 0.300),
        6:  (0.520, 0.300),
        7:  (0.608, 0.300),
        8:  (0.695, 0.300),
        9:  (0.782, 0.300),
        10: (0.866, 0.300),

        11: (0.867, 0.515),
        12: (0.784, 0.515),
        13: (0.704, 0.515),
        14: (0.618, 0.515),
        15: (0.534, 0.515),
        16: (0.447, 0.515),
        17: (0.361, 0.515),
        18: (0.275, 0.515),
        19: (0.190, 0.515),
        20: (0.108, 0.515),

        21: (0.085, 0.723),
        22: (0.173, 0.723),
        23: (0.258, 0.723),
        24: (0.347, 0.723),
        25: (0.433, 0.723),
        26: (0.520, 0.723),
        27: (0.608, 0.723),
        28: (0.698, 0.723),
        29: (0.783, 0.723),
        30: (0.869, 0.723),
    }

    x_percent, y_percent = positions[level_number]

    x = app.width * (x_percent + 0.025)
    y = app.height * y_percent

    return x, y

def levels_mouse_moved(app, event):
    back_button = get_back_button(app)
    reset_button = get_reset_levels_button(app)

    if is_inside_button(event.x, event.y, back_button):
        return "levels_back"

    if is_inside_button(event.x, event.y, reset_button):
        return "levels_reset"

    levels_count = len(app.levels["levels"])
    button_size = 80

    for i in range(levels_count):
        level_number = i + 1

        x, y = get_level_position(app, level_number)

        if (x - button_size / 2 <= event.x <= x + button_size / 2 and y - button_size / 2 <= event.y <= y + button_size / 2):
            if level_number <= app.unlocked_level:
                return "level_" + str(level_number)

    return None

def levels_mouse_pressed(app, event):
    back_button = get_back_button(app)

    if is_inside_button(event.x, event.y, back_button):
        return "back"

    reset_button = get_reset_levels_button(app)

    if is_inside_button(event.x, event.y, reset_button):
        return "reset"

    levels_count = len(app.levels["levels"])
    button_size = 80

    for i in range(levels_count):
        level_number = i + 1

        x, y = get_level_position(app, level_number)

        if (
            x - button_size / 2 <= event.x <= x + button_size / 2
            and y - button_size / 2 <= event.y <= y + button_size / 2
        ):
            if level_number <= app.unlocked_level:
                app.level_index = i
                return "start_level"

    return None

# \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/
# PAUSE
# \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/

def pause_mouse_moved(app, event):
    buttons = get_pause_buttons(app)

    for button in buttons:
        if is_inside_button(event.x, event.y, button):
            return button["action"]

    return None

def get_pause_buttons(app):
    scale = get_scale(app)

    button_width = 260 * scale
    button_height = 80 * scale
    gap = 1 * scale

    center_x = app.width / 2    
    start_y = app.height / 2 - 35 * scale

    x1 = center_x - button_width / 2
    x2 = center_x + button_width / 2

    return [
        {
            "text": "CONTINUE",
            "x1": x1,
            "y1": start_y,
            "x2": x2,
            "y2": start_y + button_height,
            "action": "continue"
        },

        {
            "text": "MENU",
            "x1": x1,
            "y1": start_y + button_height + gap,
            "x2": x2,
            "y2": start_y + button_height * 2 + gap,
            "action": "menu"
        }
    ]


def draw_pause(app, canvas):
    scale = get_scale(app)

    window_width = 520 * scale
    window_height = 430 * scale

    x1 = app.width / 2 - window_width / 2
    x2 = app.width / 2 + window_width / 2

    y1 = app.height / 2 - window_height / 2
    y2 = app.height / 2 + window_height / 2

    image_in_box(
        canvas,
        x1,
        y1,
        x2,
        y2,
        pause_fon,
        fit_mode="stretch"
    )

    title_width = 320 * scale
    title_height = 100 * scale

    title_x1 = app.width / 2 - title_width / 2
    title_x2 = app.width / 2 + title_width / 2

    title_y1 = y1 + 75 * scale
    title_y2 = title_y1 + title_height

    image_in_box(
        canvas,
        title_x1,
        title_y1,
        title_x2,
        title_y2,
        pause_title
    )

    buttons = get_pause_buttons(app)

    for button in buttons:
        draw_button(app, canvas, button)


def pause_mouse_pressed(app, event):
    buttons = get_pause_buttons(app)

    for button in buttons:
        if is_inside_button(event.x, event.y, button):
            return button["action"]

    return None

# \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/
# STORE
# \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/

def get_store_boxes(app):
    scale = get_scale(app)

    box_size = 150 * scale
    gap_x = 40 * scale
    gap_y = 35 * scale

    total_width = box_size * 3 + gap_x * 2

    start_x = app.width / 2 - total_width / 2
    start_y = 220 * scale

    boxes = []

    for i in range(6):
        row = i // 3
        col = i % 3

        x1 = start_x + col * (box_size + gap_x)
        y1 = start_y + row * (box_size + gap_y)

        boxes.append({
            "x1": x1,
            "y1": y1,
            "x2": x1 + box_size,
            "y2": y1 + box_size
        })

    return boxes

def store_mouse_moved(app, event):
    back_button = get_back_button(app)

    if is_inside_button(event.x, event.y, back_button):
        return "store_back"

    return None

def draw_store(app, canvas):
    scale = get_scale(app)

    # Background
    image_in_box(
        canvas,
        0,
        0,
        app.width,
        app.height,
        shop_fon,
        fit_mode="stretch"
    )

    container_width = 360 * scale
    container_height = 110 * scale

    container_x1 = app.width / 2 - container_width / 2
    container_y1 = 125 * scale

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

    # Coin icon
    coin_size = 40 * scale

    coin_x1 = container_x1 + 100 * scale
    coin_y1 = (
        container_y1 - 1 * scale
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

    # Coin number
    canvas.create_text(
        coin_x2 + 30 * scale,
        container_y1 + container_height / 2 - 6 * scale,
        text=str(app.coin),
        font=("Georgia", int(34 * scale), "bold"),
        fill="#e8c978",
        anchor="w"
    )

    boxes = get_store_boxes(app)

    i = 0

    for upgrade_key in app.upgrades:
        item = app.upgrades[upgrade_key]
        box = boxes[i]

        if item["bought"]:
            image = load_image(item["image"])
        else:
            image = unknown_icon

        image_in_box(
            canvas,
            box["x1"],
            box["y1"],
            box["x2"],
            box["y2"],
            image,
            fit_mode="contain"
        )

        i += 1

    draw_back_button(app, canvas)

def store_mouse_pressed(app, event):
    back_button = get_back_button(app)

    if is_inside_button(event.x, event.y, back_button):
        return "back"

    return None

# \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/
# SETTINGS
# \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/

def get_volume_sliders(app):
    controls = app.config["controls"]

    label_width = 140
    button_width = 120
    button_height = 35
    button_gap = 20
    row_gap = 8

    total_width = (
        label_width
        + button_width
        + button_gap
        + button_width
    )

    total_height = (
        button_height * len(controls)
        + row_gap * (len(controls) - 1)
    )

    start_x = app.width / 2 - total_width / 2
    available_center_y = app.height / 2 - 45
    start_y = available_center_y - total_height / 2

    panel_x1 = start_x - 35
    panel_x2 = start_x + total_width + 35

    slider_x1 = start_x + label_width
    slider_x2 = panel_x2 - 25

    music_y = start_y + total_height + 55
    sound_y = start_y + total_height + 95

    return {
        "music": {
            "label_x": start_x,
            "x1": slider_x1,
            "x2": slider_x2,
            "y": music_y,
            "height": 10
        },

        "sound": {
            "label_x": start_x,
            "x1": slider_x1,
            "x2": slider_x2,
            "y": sound_y,
            "height": 10
        }
    }

def get_reset_settings_button(app):
    scale = get_scale(app)

    button_width = 300 * scale
    button_height = 70 * scale

    x1 = app.width / 2 - button_width / 2
    x2 = app.width / 2 + button_width / 2

    y2 = app.height - 50 * scale
    y1 = y2 - button_height

    return {
        "text": "RESET",
        "action": "reset",
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2
    }

def get_reset_levels_button(app):
    scale = get_scale(app)

    button_width = 300 * scale
    button_height = 70 * scale

    x1 = app.width / 2 - button_width / 2
    x2 = app.width / 2 + button_width / 2

    y2 = app.height - 50 * scale
    y1 = y2 - button_height

    return {
        "text": "RESET",
        "action": "reset",
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2
    }

def get_control_buttons(app):
    controls = app.config["controls"]

    label_width = 140
    button_width = 120
    button_height = 35
    button_gap = 20
    row_gap = 8

    total_width = (label_width + button_width + button_gap + button_width)

    total_height = (button_height * len(controls) + row_gap * (len(controls) - 1))

    start_x = app.width / 2 - total_width / 2
    available_center_y = app.height / 2 - 45
    start_y = available_center_y - total_height / 2

    first_button_x1 = start_x + label_width
    first_button_x2 = first_button_x1 + button_width

    second_button_x1 = first_button_x2 + button_gap
    second_button_x2 = second_button_x1 + button_width

    buttons = []

    i = 0

    for action in controls:
        y1 = start_y + i * (button_height + row_gap)
        y2 = y1 + button_height

        buttons.append({
            "action": action,
            "index": 0,
            "x1": first_button_x1,
            "y1": y1,
            "x2": first_button_x2,
            "y2": y2
        })

        buttons.append({
            "action": action,
            "index": 1,
            "x1": second_button_x1,
            "y1": y1,
            "x2": second_button_x2,
            "y2": y2
        })

        i += 1

    return buttons

def get_key_text(key):
    if key == "":
        return "None"

    return key

def draw_control_button(canvas, button, text):
    text_color = "#8f8f7a"

    if text != "None":
        text_color = "#f1d58a"

    canvas.create_rectangle(
        button["x1"],
        button["y1"],
        button["x2"],
        button["y2"],
        fill="#2f3a2a",
        outline="#c9a45c",
        width=3
    )

    canvas.create_rectangle(
        button["x1"] + 3,
        button["y1"] + 3,
        button["x2"] - 3,
        button["y2"] - 3,
        outline="#587044",
        width=1
    )

    canvas.create_text(
        (button["x1"] + button["x2"]) / 2,
        (button["y1"] + button["y2"]) / 2,
        text=text,
        font=("Georgia", 14, "bold"),
        fill=text_color
    )

def draw_settings(app, canvas):
    scale = get_scale(app)

    image_in_box(canvas, 0, 0, app.width, app.height, settings_fon, fit_mode="stretch")

    title_width = 520 * scale
    title_height = 160 * scale

    title_x1 = app.width / 2 - title_width / 2
    title_y1 = 20 * scale
    title_x2 = app.width / 2 + title_width / 2
    title_y2 = title_y1 + title_height

    image_in_box(canvas, title_x1, title_y1, title_x2, title_y2, settings_title)

    controls = app.config["controls"]

    buttons = get_control_buttons(app)

    label_width = 140
    button_width = 120
    button_height = 35
    button_gap = 20
    row_gap = 8

    total_width = (label_width + button_width + button_gap + button_width)
    total_height = (button_height * len(controls) + row_gap * (len(controls) - 1))

    start_x = app.width / 2 - total_width / 2
    available_center_y = app.height / 2 - 45
    start_y = (available_center_y - total_height / 2)

    panel_x1 = start_x - 35
    panel_x2 = start_x + total_width + 35

    panel_y1 = start_y - 35
    panel_y2 = start_y + total_height + 135

    canvas.create_rectangle(
        panel_x1,
        panel_y1,
        panel_x2,
        panel_y2,
        fill="#1d2419",
        outline="#c9a45c",
        width=4
    )

    canvas.create_rectangle(
        panel_x1 + 7,
        panel_y1 + 7,
        panel_x2 - 7,
        panel_y2 - 7,
        outline="#587044",
        width=2
    )

    i = 0

    for action in controls:
        label = action.capitalize()

        y1 = start_y + i * (button_height + row_gap)
        center_y = y1 + button_height / 2

        canvas.create_text(
            start_x,
            center_y,
            text=label.upper(),
            font=("Georgia", 16, "bold"),
            fill="#e8c978",
            anchor="w"
        )

        key1 = app.config["controls"][action][0]
        key2 = app.config["controls"][action][1]

        key1 = get_key_text(key1)
        key2 = get_key_text(key2)

        button1 = buttons[i * 2]
        button2 = buttons[i * 2 + 1]

        draw_control_button(canvas, button1, key1)
        draw_control_button(canvas, button2, key2)

        i += 1

    reset_button = get_reset_settings_button(app)

    draw_button(app, canvas, reset_button)
    draw_back_button(app, canvas)

    sliders = get_volume_sliders(app)

    music_slider = sliders["music"]
    sound_slider = sliders["sound"]

    music_volume = app.config["music_volume"]
    sound_volume = app.config["sound_volume"]

    canvas.create_text(
        music_slider["label_x"],
        music_slider["y"],
        text="MUSIC",
        font=("Georgia", 16, "bold"),
        fill="#e8c978",
        anchor="w"
    )

    canvas.create_rectangle(
        music_slider["x1"],
        music_slider["y"] - music_slider["height"] / 2,
        music_slider["x2"],
        music_slider["y"] + music_slider["height"] / 2,
        fill="#2f3a2a",
        outline="#c9a45c",
        width=2
    )

    music_knob_x = (
        music_slider["x1"]
        + (music_slider["x2"] - music_slider["x1"]) * music_volume
    )

    canvas.create_oval(
        music_knob_x - 10,
        music_slider["y"] - 10,
        music_knob_x + 10,
        music_slider["y"] + 10,
        fill="#e8c978",
        outline="#c9a45c",
        width=2
    )

    canvas.create_text(
        sound_slider["label_x"],
        sound_slider["y"],
        text="SOUNDS",
        font=("Georgia", 16, "bold"),
        fill="#e8c978",
        anchor="w"
    )

    canvas.create_rectangle(
        sound_slider["x1"],
        sound_slider["y"] - sound_slider["height"] / 2,
        sound_slider["x2"],
        sound_slider["y"] + sound_slider["height"] / 2,
        fill="#2f3a2a",
        outline="#c9a45c",
        width=2
    )

    sound_knob_x = (
        sound_slider["x1"]
        + (sound_slider["x2"] - sound_slider["x1"]) * sound_volume
    )

    canvas.create_oval(
        sound_knob_x - 10,
        sound_slider["y"] - 10,
        sound_knob_x + 10,
        sound_slider["y"] + 10,
        fill="#e8c978",
        outline="#c9a45c",
        width=2
    )

    if app.changing_control is not None:
        draw_key_popup(app, canvas)

def settings_mouse_moved(app, event):

    sliders = get_volume_sliders(app)

    for slider_name in sliders:
        slider = sliders[slider_name]

        if (
            slider["x1"] <= event.x <= slider["x2"]
            and slider["y"] - 15 <= event.y <= slider["y"] + 15
        ):
            return slider_name + "_volume"

    if app.changing_control is not None:
        return None

    back_button = get_back_button(app)

    if is_inside_button(event.x, event.y, back_button):
        return "settings_back"

    reset_button = get_reset_settings_button(app)

    if is_inside_button(event.x, event.y, reset_button):
        return "settings_reset"

    buttons = get_control_buttons(app)

    for i in range(len(buttons)):
        button = buttons[i]

        if is_inside_button(event.x, event.y, button):
            return "control_" + str(i)

    return None

def settings_mouse_pressed(app, event):

    if app.changing_control is not None:
        return None

    back_button = get_back_button(app)

    if is_inside_button(event.x, event.y, back_button):
        return "back"

    reset_button = get_reset_settings_button(app)

    if is_inside_button(event.x, event.y, reset_button):
        return "reset"

    buttons = get_control_buttons(app)

    for button in buttons:
        if is_inside_button(event.x, event.y, button):
            app.changing_control = (button["action"], button["index"])
            return "control"
    return None

def draw_key_popup(app, canvas):
    width = 300
    height = 140

    x1 = app.width / 2 - width / 2
    x2 = app.width / 2 + width / 2

    y1 = app.height / 2 - height / 2
    y2 = app.height / 2 + height / 2

    canvas.create_rectangle(x1, y1, x2, y2, fill="white", width=3)

    action, index = app.changing_control

    canvas.create_text(
        app.width / 2,
        app.height / 2 - 25,
        text=f"Choose key for {action.upper()}",
        font="Arial 16 bold"
    )

    canvas.create_text(app.width / 2, app.height / 2 + 20, text="Press any key...")

# \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/
# GAME OVER
# \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/

def get_gameover_buttons(app):
    scale = get_scale(app)

    button_width = 360 * scale
    button_height = 110 * scale
    gap = 0 * scale

    center_x = app.width / 2
    start_y = app.height * 0.43

    return [
        {
            "text": "RESTART",
            "x1": center_x - button_width / 2,
            "y1": start_y,
            "x2": center_x + button_width / 2,
            "y2": start_y + button_height,
            "action": "restart"
        },
        {
            "text": "MENU",
            "x1": center_x - button_width / 2,
            "y1": start_y + button_height + gap,
            "x2": center_x + button_width / 2,
            "y2": start_y + button_height * 2 + gap,
            "action": "menu"
        }
    ]

def gameover_key_pressed(app, key):
    buttons = get_gameover_buttons(app)

    if key == "Up":
        app.gameover_index -= 1

        if app.gameover_index < 0:
            app.gameover_index = len(buttons) - 1

        app.hover_sound.play()

    elif key == "Down":
        app.gameover_index += 1

        if app.gameover_index >= len(buttons):
            app.gameover_index = 0

        app.hover_sound.play()

    elif key == "Enter":
        app.click_sound.play()
        return buttons[app.gameover_index]["action"]

    return None

def draw_gameover(app, canvas):
    scale = get_scale(app)
    image_in_box(canvas, 0, 0, app.width, app.height, gameover_fon, fit_mode="stretch")

    title_width = 600 * scale
    title_height = 180 * scale

    title_x1 = app.width / 2 - title_width / 2
    title_x2 = app.width / 2 + title_width / 2

    title_y1 = 70 * scale
    title_y2 = title_y1 + title_height

    image_in_box(canvas, title_x1, title_y1, title_x2, title_y2, gameover_title)

    buttons = get_gameover_buttons(app)

    for i in range(len(buttons)):
        button = buttons[i]

        draw_button(app, canvas, button)

        if i == app.gameover_index:
            draw_selected_arrows(app, canvas, button)

def gameover_mouse_pressed(app, event):
    buttons = get_gameover_buttons(app)

    for button in buttons:
        if is_inside_button(event.x, event.y, button):
            return button["action"]

    return None


def gameover_mouse_moved(app, event):
    buttons = get_gameover_buttons(app)

    for i in range(len(buttons)):
        button = buttons[i]

        if is_inside_button(event.x, event.y, button):
            app.gameover_index = i
            return button["action"]

    return None