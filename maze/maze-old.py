import sys
from typing import Any, Literal
from enum import Enum


class Draw(Enum):
    TOP = "▀▀"  
    BOTTOM = "▄▄"
    LATERAL = "█"
    EMPTY = "  "
    LEFT_WALL_PATTERN = "█ "
    TOP_LEFT_WALL_PATTERN = " ▄"
    WALL_TOP_RIGHT_PATTERN = "▄ "
    BOTTOM_LEFT_WALL_PATTERN = " ▀"
    WALL_LOWER_RIGHT_PATTERN = "▀ "
    WALL_RIGHT_PATTERN = " █"
    MIDDLE = "██"


class Color(Enum):
    RESET= '\033[0m'
    DEFAULT = '\033[0m'

    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'

    BG_BLACK   = '\033[40m'
    BG_RED     = '\033[41m'
    BG_GREEN   = '\033[42m'
    BG_YELLOW  = '\033[43m'
    BG_BLUE    = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN    = '\033[46m'
    BG_WHITE   = '\033[47m'


def grid_logo_42(data: dict, grid: list[list[int]]) -> bool:
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


def grid_caca(data: dict, grid: list[list[int]]) -> bool:
    x: int = data["WIDTH"]
    y: int = data["HEIGHT"]

    caca_matrix: list[list[int]] = [
        [0, 0, 0, 0, 0, 6, 2, 7, 0, 0, 0],
        [0, 0, 0, 6, 2, 1, 2, 7, 0, 0, 0],
        [0, 0, 6, 1, 1, 1, 1, 1, 7, 0, 0],
        [0, 6, 1, 0, 1, 1, 1, 0, 1, 7, 0],
        [6, 1, 1, 1, 1, 0, 1, 1, 1, 1, 7],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [8, 3, 3, 3, 3, 3, 3, 3, 3, 3, 9],
    ]
    logo_y = len(caca_matrix)
    logo_x = len(caca_matrix[0])

    if x >= logo_x and y >= logo_y:
        start_x = (x // 2) - (logo_x // 2)
        start_y = (y // 2) - (logo_y // 2)

        for i in range(logo_y):
            for j in range(logo_x):
                grid[start_y + i][start_x + j] = caca_matrix[i][j]
        return True

    print("Error: maze too small to display 42.")
    return False


class Maze:
    def __init__(self, data: dict):
        self.x: int = data["WIDTH"]
        self.y: int = data["HEIGHT"]
        self.grid: list[list[int]] = [
            [0 for _ in range(self.x)] for _ in range(self.y)]
        self.flag = grid_caca(data, self.grid)
        self.color_select = Color.BG_YELLOW.value

    def set_color() -> None:
        pass

    def draw_maze(self) -> None:
        for i in range(self.y):
            sys.stdout.write(
                f"{self.color_select}"
                f"{Draw.LATERAL.value}"
                f"{Color.DEFAULT.value}")
            for j in range(self.x):
                if i == 0:
                    sys.stdout.write(
                        f"{self.color_select}"
                        f"{Draw.TOP.value}"
                        f"{Color.DEFAULT.value}")
                elif i == self.y - 1:
                    sys.stdout.write(
                        f"{self.color_select}"
                        f"{Draw.BOTTOM.value}"
                        f"{Color.DEFAULT.value}")
                else:
                    if self.flag:
                        val: Any | int = self.grid[i][j]
                        if val == 1:
                            sys.stdout.write(
                                f"{self.color_select}"
                                f"{Draw.MIDDLE.value}"
                                f"{Color.DEFAULT.value}")
                        elif val == 10:
                            sys.stdout.write(
                                f"{self.color_select}"
                                f"{Draw.MIDDLE.value}"
                                f"{Color.DEFAULT.value}")
                        elif val == 2:
                            sys.stdout.write(
                                f"{self.color_select}"
                                f"{Draw.BOTTOM.value}"
                                f"{Color.DEFAULT.value}")
                        elif val == 3:
                            sys.stdout.write(
                                f"{self.color_select}"
                                f"{Draw.TOP.value}"
                                f"{Color.DEFAULT.value}")
                        elif val == 4:
                            sys.stdout.write(
                                f"{self.color_select}"
                                f"{Draw.WALL_RIGHT_PATTERN.value}"
                                f"{Color.DEFAULT.value}")
                        elif val == 5:
                            sys.stdout.write(
                                f"{self.color_select}"
                                f"{Draw.LEFT_WALL_PATTERN.value}"
                                f"{Color.DEFAULT.value}")
                        elif val == 6:
                            sys.stdout.write(
                                f"{self.color_select}"
                                f"{Draw.TOP_LEFT_WALL_PATTERN.value}"
                                f"{Color.DEFAULT.value}")
                        elif val == 7:
                            sys.stdout.write(
                                f"{self.color_select}"
                                f"{Draw.WALL_TOP_RIGHT_PATTERN.value}"
                                f"{Color.DEFAULT.value}")
                        elif val == 8:
                            sys.stdout.write(
                                f"{self.color_select}"
                                f"{Draw.BOTTOM_LEFT_WALL_PATTERN.value}"
                                f"{Color.DEFAULT.value}")
                        elif val == 9:
                            sys.stdout.write(
                                f"{self.color_select}"
                                f"{Draw.WALL_LOWER_RIGHT_PATTERN.value}"
                                f"{Color.DEFAULT.value}")
                        else:
                            sys.stdout.write(
                                f"{self.color_select}{Draw.EMPTY.value}"
                                f"{Color.DEFAULT.value}")
                    else:
                        sys.stdout.write(
                            f"{self.color_select}"
                            f"{Draw.EMPTY.value}"
                            f"{Color.DEFAULT.value}")
            sys.stdout.write(
                f"{self.color_select}"
                f"{Draw.LATERAL.value}"
                f"{Color.DEFAULT.value}\n")
        sys.stdout.write(Color.RESET.value)
        sys.stdout.flush()