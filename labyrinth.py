import sys


def gird_logo(data: dict):
    x = data["WIDTH"]
    y = data["HEIGHT"]

    grid = [[0 for _ in range(x)] for _ in range(y)]

    logo_42 = [
        [6, 2, 2, 2, 2, 2, 2, 2, 7],
        [4, 0, 1, 0, 10, 0, 0, 0, 5],
        [4, 0, 1, 0, 10, 1, 1, 0, 5],
        [4, 0, 0, 0, 10, 0, 0, 0, 5],
        [4, 1, 1, 0, 10, 0, 1, 1, 5],
        [4, 1, 1, 0, 10, 0, 0, 0, 5],
        [8, 3, 3, 3, 3, 3, 3, 3, 9],
    ]

    logo_y = len(logo_42)
    logo_x = len(logo_42[0])

    if x >= 13 and y >= 13:
        start_x = (x // 2) - (logo_x // 2)
        start_y = (y // 2) - (logo_y // 2)

        for i in range(logo_y):
            for j in range(logo_x):
                grid[start_y + i][start_x + j] = logo_42[i][j]
        return grid
    else:
        print("Error: maze too small to display 42.")


def labyrinth_generation(data: dict) -> None:
    x = data["WIDTH"]
    y = data["HEIGHT"]

    grid = gird_logo(data)

    top = "▀▀"
    bottom = "▄▄"
    lateral = "█"
    mur_interieur = "██"
    empty = "  "
    left_wall_pattern = "█ "
    top_left_wall_pattern = " ▄"
    wall_top_right_pattern = "▄ "
    bottom_left_wall_pattern = " ▀"
    wall_lower_right_pattern = "▀ "
    wall_right_pattern = " █"
    middle = "██"

    for i in range(y):
        sys.stdout.write(lateral)
        for j in range(x):
            if i == 0:
                sys.stdout.write(top)
            elif i == y - 1:
                sys.stdout.write(bottom)
            else:
                val = grid[i][j]
                if val == 1:
                    sys.stdout.write(mur_interieur)
                elif val == 10:
                    sys.stdout.write(middle)
                elif val == 2:
                    sys.stdout.write(bottom)
                elif val == 3:
                    sys.stdout.write(top)
                elif val == 4:
                    sys.stdout.write(wall_right_pattern)
                elif val == 5:
                    sys.stdout.write(left_wall_pattern)
                elif val == 6:
                    sys.stdout.write(top_left_wall_pattern)
                elif val == 7:
                    sys.stdout.write(wall_top_right_pattern)
                elif val == 8:
                    sys.stdout.write(bottom_left_wall_pattern)
                elif val == 9:
                    sys.stdout.write(wall_lower_right_pattern)
                else:
                    sys.stdout.write(empty)
        sys.stdout.write(f"{lateral}\n")
