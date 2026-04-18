from random import shuffle, randrange
from maze.utils_enum import Color, Theme
from utils.parser import clear
import time


def create_maze(maze):
    stack = [(maze.entry[0], maze.entry[1])]
    delay: int = Theme.delais_draw
    while stack:
        if Theme.color_case_logo == "random" and Theme.logo_midile:
            maze.logo.random_color_2()
        cell_work = stack[-1]
        x = cell_work[0]
        y = cell_work[1]
        cell = maze.grid[y][x]
        if Theme.animation_draw and Theme.color_animation_backtraking is not None:
            cell.color_case = Theme.color_animation_backtraking
        cell.visit = True
        direction = [(x - 1, y),
                     (x, y + 1),
                     (x + 1, y),
                     (x, y - 1)]
        shuffle(direction)
        found = False
        for direct_x, direct_y in direction:
            if 0 <= direct_x < maze.width and 0 <= direct_y < maze.height:
                verif_visit = maze.grid[direct_y][direct_x]
                if verif_visit.visit:
                    continue
                if not verif_visit.visit:
                    found = True
                cell_destruction = maze.grid[y][x]
                neighbor = maze.grid[direct_y][direct_x]
                # Mouvement Vertical
                if direct_x == x and verif_visit.visit == False:
                    # on monte vers le nord
                    if direct_y < y:
                        cell_destruction.walls["North"] = False
                        neighbor.walls["South"] = False
                        neighbor.visit = True
                    elif direct_y > y:
                        # on dessend vers le sud
                        cell_destruction.walls["South"] = False
                        neighbor.walls["North"] = False
                        neighbor.visit = True
                # Mouvement Horizontal
                elif direct_y == y and verif_visit.visit == False:
                    if direct_x < x:
                        # on va vers l ouest
                        cell_destruction.walls["West"] = False
                        neighbor.walls["East"] = False
                        neighbor.visit = True
                    elif direct_x > x:
                        # on va vers l est
                        cell_destruction.walls["East"] = False
                        neighbor.walls["West"] = False
                        neighbor.visit = True
                stack.append((direct_x, direct_y))
                # print(stack)
                if Theme.animation_draw:
                    maze.draw_maze()
                    time.sleep(delay)
                break
        if not found:
            stack.pop()
            if Theme.animation_draw:
                cell.color_case = Color.DEFAULT.value
