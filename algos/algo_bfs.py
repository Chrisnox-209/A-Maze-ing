from random import shuffle, randrange
from maze.utils_enum import Color, Theme
from utils.parser import clear
import time

def find_path_bfs(maze):
    maze.all_cell_false()
    stack = [(maze.entry[0], maze.entry[1])]
    delay: int = Theme.delais_draw
    while stack:
        cell_work = stack[-1]
        x = cell_work[0]
        y = cell_work[1]
        if x == maze.exit[0] and y == maze.exit[1]:
            for x, y in stack:
                maze.grid[y][x].color_case = Theme.color_path
            return
        cell = maze.grid[y][x]
        cell.visit = True
        direction = [(x - 1, y),
                     (x, y + 1),
                     (x + 1, y),
                     (x, y - 1)]
        shuffle(direction)
        found = False
        cell.color_case = Color.BLUE.value
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
                    if direct_y < y and cell_destruction.walls["North"] == False:
                        neighbor.visit = True
                        stack.append((direct_x, direct_y))

                    elif direct_y > y and cell_destruction.walls["South"] == False:
                        # on dessend vers le sud
                        neighbor.visit = True
                        stack.append((direct_x, direct_y))

                # Mouvement Horizontal
                elif direct_y == y and verif_visit.visit == False:
                    if direct_x < x and cell_destruction.walls["West"] == False:
                        # on va vers l ouest
                        neighbor.visit = True
                        stack.append((direct_x, direct_y))

                    elif direct_x > x and cell_destruction.walls["East"] == False:
                        # on va vers l est
                        neighbor.visit = True
                        stack.append((direct_x, direct_y))


                # stack.append((direct_x, direct_y))
                if Theme.animation_draw_path:
                    maze.draw_maze()
                    time.sleep(delay)
                break
        if not found:
            stack.pop()
            cell.color_case = Color.DEFAULT.value
        
