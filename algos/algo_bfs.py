from random import shuffle, randrange
from maze.utils_enum import Color, Theme
from utils.parser import clear
import time
from utils.timer import Timer
from collections import deque 


def find_path_bfs(maze):
    maze.all_cell_false()
    stack = deque([(maze.entry[0], maze.entry[1])])
    delay: int = Theme.delais_draw
    time_start = Timer()
    path = {}
    while stack:
        cell_work = stack.popleft()
        x = cell_work[0]
        y = cell_work[1]
        if x == maze.exit[0] and y == maze.exit[1]:
            current = (maze.exit[0], maze.exit[1])
            i:int = 0
            while current != (maze.entry[0], maze.entry[1]):
                maze.grid[current[1]][current[0]].path_id = i
                i+=1
                current = path[current]
            return
        cell = maze.grid[y][x]
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
                if direct_x == x and verif_visit.visit == False:
                    if direct_y < y and cell_destruction.walls["North"] == False:
                        neighbor.visit = True
                        stack.append((direct_x, direct_y))
                        path[(direct_x, direct_y)] = (x, y)

                    elif direct_y > y and cell_destruction.walls["South"] == False:
                        neighbor.visit = True
                        stack.append((direct_x, direct_y))
                        path[(direct_x, direct_y)] = (x, y)

                elif direct_y == y and verif_visit.visit == False:
                    if direct_x < x and cell_destruction.walls["West"] == False:
                        neighbor.visit = True
                        stack.append((direct_x, direct_y))
                        path[(direct_x, direct_y)] = (x, y)

                    elif direct_x > x and cell_destruction.walls["East"] == False:
                        neighbor.visit = True
                        stack.append((direct_x, direct_y))
                        path[(direct_x, direct_y)] = (x, y)
                # stack.append((direct_x, direct_y))
                if Theme.logo_chrono:
                    # maze.logo.reset_logo()
                    maze.logo.reset_logo()
                    maze.generate_logo()
                    timestr = f"{time_start.get_time(): .0f}"
                    Theme.logo_midile = str(timestr)
                    maze.generate_logo()
        
