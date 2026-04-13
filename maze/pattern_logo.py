from enum import Enum
from maze.utils_enum import Color, Theme
import random

class Logo:
    def __init__(self,  maze) -> None:
        self.maze = maze
        self.color =  Theme.color_case_logo
        if Theme.color_case_logo == "random":
            self.color =  Color.random_color()
        
    def random_color_2(self) -> None:
        valid_colors = [c.value for c in Color if c not in (Color.RESET, Color.DEFAULT)]
        self.color = random.choice(valid_colors)
        self.select_logo()

    def select_logo(self):
        if Theme.logo_midile == "logo_42":
            self.logo_42()
        if Theme.logo_midile == "caca":
            self.logo_caca()
        if Theme.logo_midile == "logo_surprise":
            self.logo_surprise()

    def change_color_logo(self):
        self.color =  Theme.color_case_logo
        if Theme.color_case_logo == "random":
            self.color =  Color.random_color()

    def logo_42(self):
        self.pattern = [
            [1, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 1, 1]
        ]
        self.make_logo()
    def logo_caca(self):
        self.pattern = [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0]
        ]
        self.make_logo()
    def logo_surprise(self):
        self.pattern = [
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1]
        ]
        self.make_logo()
    def make_logo(self):
        with_logo:int = len(self.pattern[0])
        height_logo:int = len(self.pattern)
        if self.maze.width <= with_logo + 4 and self.maze.height < height_logo + 4:
            return
        start_x = (self.maze.width - with_logo) // 2
        start_y = (self.maze.height - height_logo) // 2

        for row in range(height_logo):
            for col in range(with_logo):
                if self.pattern[row][col] == 1:
                    grid_y = start_y + row
                    grid_x = start_x + col
                    cell = self.maze.grid[grid_y][grid_x]
                    cell.color_case = self.color
                    cell.visit = True
                    if row > 0 and self.pattern[row - 1][col] == 1:
                        cell.walls["North"] = False
                    if row < height_logo - 1 and self.pattern[row + 1][col] == 1:
                        cell.walls["South"] = False
                    if col > 0 and self.pattern[row][col - 1] == 1:
                        cell.walls["West"] = False
                    if col < with_logo - 1 and self.pattern[row][col + 1] == 1:
                        cell.walls["East"] = False



