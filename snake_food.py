import random


# -- Apple function
def add_apple_at_random_location(grid):
    free_positions = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                free_positions.append((row, col))

    if len(free_positions) > 0:
        row, col = random.choice(free_positions)
        grid[row][col] = -1


# -- Coin function
def add_coin_at_random_location(grid):
    for row in grid:
        if -2 in row:
            return

    free_positions = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                free_positions.append((row, col))

    if len(free_positions) > 0:
        row, col = random.choice(free_positions)
        grid[row][col] = -2


# -- Meat function
def add_meat_at_random_location(grid):
    free_positions = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                free_positions.append((row, col))

    if len(free_positions) > 0:
        row, col = random.choice(free_positions)
        grid[row][col] = -3


# -- Meat and apple function
def add_food_at_random_location(app):
    if (
        app.upgrades["meat"]["bought"]
        and random.randint(1, 100) <= 10
    ):
        add_meat_at_random_location(app.board)

    else:
        add_apple_at_random_location(app.board)


# -- Coin chance function
def get_coin_chance(app):
    if app.upgrades["coin_chance"]["bought"]:
        return 25

    return 10


# -- Spawn next food and possible coin
def spawn_next_food(app):
    add_food_at_random_location(app)

    coin_chance = get_coin_chance(app)

    if random.randint(1, 100) <= coin_chance:
        add_coin_at_random_location(app.board)