import sys
from typing import Any, Literal
from enum import Enum

class Draw(Enum):
    TOP = "▀▀"
    BOTTOM = "▄▄"
    LATERAL = "█"
    mur_interieur = "██"
    EMPTY = "  "
    LEFT_WALL_PATTERN = "█ "
    TOP_LEFT_WALL_PATTERN = " ▄"
    WALL_TOP_RIGHT_PATTERN = "▄ "
    BOTTOM_LEFT_WALL_PATTERN = " ▀"
    WALL_LOWER_RIGHT_PATTERN = "▀ "
    WALL_RIGHT_PATTERN = " █"
    MIDDLE = "██"

def grid_logo_42(data: dict, grid:list[list[int]]) -> bool:
    x: int = data["WIDTH"]
    y: int = data["HEIGHT"]

    logo_42: list[list[int]] = [
        [6, 2, 2, 2, 2, 2, 2, 2, 7],
        [4, 0, 1, 0, 10, 0, 0, 0, 5],
        [4, 0, 1, 0, 10, 1, 1, 0, 5],
        [4, 0, 0, 0, 10, 0, 0, 0, 5],
        [4, 1, 1, 0, 10, 0, 1, 1, 5],
        [4, 1, 1, 0, 10, 0, 0, 0, 5],
        [8, 3, 3, 3, 3, 3, 3, 3, 9],
    ]

    logo_y: int = len(logo_42)
    logo_x: int = len(logo_42[0])

    if x >= 13 and y >= 13:
        start_x: Any | int = (x // 2) - (logo_x // 2)
        start_y: Any | int = (y // 2) - (logo_y // 2)

        for i in range(logo_y):
            for j in range(logo_x):
                grid[start_y + i][start_x + j] = logo_42[i][j]
    else:
        print("Error: maze too small to display 42.")
        return False
    return True

class Maze:
    def __init__(self, data:dict):
        self.x: int = data["WIDTH"]
        self.y: int = data["HEIGHT"]
        self.grid: list[list[int]] = [[0 for _ in range(self.x)] for _ in range(self.y)]
        self.flag = grid_logo_42(data, self.grid)

    def draw_maze(self) -> None:
      for i in range(self.y):
        sys.stdout.write(Draw.LATERAL.value)
        for j in range(self.x):
            if i == 0:
                sys.stdout.write(Draw.TOP.value)
            elif i == self.y - 1:
                sys.stdout.write(Draw.BOTTOM.value)
            else:
                if self.flag:
                    val: Any | int = self.grid[i][j]
                    if val == 1:
                        sys.stdout.write(Draw.MIDDLE.value)
                    elif val == 10:
                        sys.stdout.write(Draw.MIDDLE.value)
                    elif val == 2:
                        sys.stdout.write(Draw.BOTTOM.value)
                    elif val == 3:
                        sys.stdout.write(Draw.TOP.value)
                    elif val == 4:
                        sys.stdout.write(Draw.WALL_RIGHT_PATTERN.value)
                    elif val == 5:
                        sys.stdout.write(Draw.LEFT_WALL_PATTERN.value)
                    elif val == 6:
                        sys.stdout.write(Draw.TOP_LEFT_WALL_PATTERN.value)
                    elif val == 7:
                        sys.stdout.write(Draw.WALL_TOP_RIGHT_PATTERN.value)
                    elif val == 8:
                        sys.stdout.write(Draw.BOTTOM_LEFT_WALL_PATTERN.value)
                    elif val == 9:
                        sys.stdout.write(Draw.WALL_LOWER_RIGHT_PATTERN.value)
                    else:
                        sys.stdout.write(Draw.EMPTY.value)
                else:
                    sys.stdout.write(Draw.EMPTY.value)
        sys.stdout.write(f"{Draw.LATERAL.value}\n")