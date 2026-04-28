from random import shuffle
import random
from maze_core.mazegen.maze.utils_enum import Color, Theme
import time
from maze_core.mazegen.options.timer import Timer
from typing import Any


def dfs(maze: Any) -> None:
    stack = [(maze.entry[0], maze.entry[1])]
    delay = Theme.delais_draw
    list_color = ["NEON_RED",
                  "NEON_GREEN",
                  "NEON_YELLOW",
                  "NEON_BLUE",
                  "NEON_CYAN",
                  "NEON_MAGENTA",
                  "NEON_ORANGE",
                  "NEON_PURPLE",
                  "NEON_PINK",]
    time_start = Timer()
    if maze.seed:
        random.seed(maze.seed)
    while stack:
        if Theme.color_case_logo == "random" and Theme.logo_midile:
            maze.logo.random_color_2()
        cell_work = stack[-1]
        x = cell_work[0]
        y = cell_work[1]
        cell = maze.grid[y][x]
        if Theme.animation_algo:
            col = random.choice(list_color)
            cell.color_case = getattr(Color, col).value
        if Theme.logo_chrono and Theme.animation_algo:
            maze.logo.reset_logo()
            maze.logo.reset_logo()
            maze.generate_logo()
            timestr = f"{time_start.get_time(): .0f}"
            Theme.logo_midile = str(timestr)
            maze.generate_logo()
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
                    cell.color_case = Color.DEFAULT.value
                    continue
                if not verif_visit.visit:
                    found = True
                cell_destruction = maze.grid[y][x]
                neighbor = maze.grid[direct_y][direct_x]
                # Mouvement Vertical
                if direct_x == x and not verif_visit.visit:
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
                elif direct_y == y and not verif_visit.visit:
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
                if Theme.animation_algo:
                    maze.draw_maze(False)
                    time.sleep(delay)
                cell.color_case = Color.DEFAULT.value
                break
        if not found:
            stack.pop()
