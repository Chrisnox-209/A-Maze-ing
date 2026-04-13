from enum import Enum
from maze.utils_enum import Color, Theme
import random

def number_zero() -> None:
    pattern = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    return pattern

def number_one() -> None:
    pattern = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]
    return pattern

def number_two() -> None:
    pattern = [
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1]
    ]
    return pattern

def number_tree() -> None:
    pattern = [
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1]
    ]
    return pattern


def number_fourth() -> None:
    pattern = [
        [1, 0, 1,],
        [1, 0, 1,],
        [1, 1, 1,],
        [0, 0, 1,],
        [0, 0, 1,]
    ]
    return pattern


def number_five() -> None:
    pattern = [
        [1, 1, 1,],
        [1, 0, 0,],
        [1, 1, 1,],
        [0, 0, 1,],
        [1, 1, 1,]
    ]
    return pattern

def number_six() -> None:
    pattern = [
        [1, 1, 1,],
        [1, 0, 0,],
        [1, 1, 1,],
        [1, 0, 1,],
        [1, 1, 1,]
    ]
    return pattern

def number_seven() -> None:
    pattern = [
        [1, 1, 1,],
        [0, 0, 1,],
        [0, 0, 1,],
        [0, 0, 1,],
        [0, 0, 1,]
    ]
    return pattern

def number_eighth() -> None:
    pattern = [
        [1, 1, 1,],
        [1, 0, 1,],
        [1, 1, 1,],
        [1, 0, 1,],
        [1, 1, 1,]
    ]
    return pattern

def number_ninth() -> None:
    pattern = [
        [1, 1, 1,],
        [1, 0, 1,],
        [1, 1, 1,],
        [0, 0, 1,],
        [1, 1, 1,]
    ]
    return pattern

def choice_number(number:str):
    if number == "0":
        return number_zero()
    if number == "1":
        return number_one()
    if number == "2":
        return number_two()
    if number == "3":
        return number_tree()
    if number == "4":
        return number_fourth()
    if number == "5":
        return number_five()
    if number == "6":
        return number_six()
    if number == "7":
        return number_seven()
    if number == "8":
        return number_eighth()
    if number == "9":
        return number_ninth()
    return number_zero()


def combine_twoo_number(number_one:str, number_twoo:str):
    res_number = []
    res_ligne_fusion = []
    res_choice_one = choice_number(number_one)
    res_choice_twoo = choice_number(number_twoo)
    len_number_one = len(res_choice_one[0])
    len_number_twoo = len(res_choice_twoo[0])
    for a in range(5):
        for i in range(len_number_one + len_number_twoo + 1):
            if i < len_number_one:
                res_ligne_fusion.append(res_choice_one[a][i])
            if i == (len_number_one + 1):
                res_ligne_fusion.append(0)
            if i > len_number_one:
                res_ligne_fusion.append(res_choice_twoo[a][i - (len_number_one + 1)])
        res_number.append(res_ligne_fusion)
        res_ligne_fusion = []
    return res_number

def create_number(number:str):
    for i in range(len(number)):
        number_res = combine_twoo_number(number[i - 1], number[i])
    return number_res


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
        try:
            int(Theme.logo_midile)
            self.pattern = create_number(Theme.logo_midile)
            # self.tour_logo()
        except:
            pass
        self.make_logo()

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
    def logo_caca(self):
        self.pattern = [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0]
        ]
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
    # def tour_logo(self):
    #     self.pattern = [
    #         [1, 1, 1, 1, 1, 1, 1],
    #         [1, 0, 0, 0, 0, 0, 1],
    #         [1, 0, 0, 0, 0, 0, 1],
    #         [1, 0, 0, 0, 0, 0, 1],
    #         [1, 1, 1, 1, 1, 1, 1]
    #     ]
    def create_logo(number:int):
        pass

    def make_logo(self):
        with_logo:int = len(self.pattern[0])
        height_logo:int = len(self.pattern)
        if self.maze.width <= with_logo + 4 and self.maze.height < height_logo + 4:
            return
        start_x = (self.maze.width - with_logo) // 2
        start_y = (self.maze.height - height_logo) // 2

        for row in range(height_logo):
            for col in range(with_logo):
                if self.pattern[row][col] == 2:
                        cell.visit = True
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



