# snake_view_extra_demo.py
from uib_inf100_graphics.simple import canvas, display
from snake_view import draw_board

test_boards = [
    [
        [0,-1, 0],
        [1, 2, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9,10,11, 0,-1, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 6, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 1, 2, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
]

info_mode = True

while True:
    for test_board in test_boards:
        draw_board(canvas, 25, 25, 375, 375, test_board, info_mode)
        display(canvas, min_duration_sec=2)
    info_mode = not info_mode
