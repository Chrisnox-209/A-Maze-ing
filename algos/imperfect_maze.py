from random import randrange, seed
from maze.utils_enum import Theme
import time


def imperfect_maze_func(maze):
    delay: int = Theme.delais_draw
    if maze.seed:
        seed(maze.seed)
    maze.all_cell_false()
    for height in range(maze.height):
        for width in range(maze.width):
            nbr_random = randrange(1, 3)
            cell_destruction = maze.grid[height][width]
            if height != 0 and width != 0 and height < maze.height - \
                    1 and width < maze.width and not cell_destruction.visit:
                cell_destruction.visit = True
                if nbr_random == 1:
                    neighbor = maze.grid[height - 1][width]
                    if neighbor.visit is not True:
                        cell_destruction.walls["North"] = False
                        neighbor.walls["South"] = False
                if nbr_random == 2:
                    neighbor = maze.grid[height][width - 1]
                    if neighbor.visit is not True:
                        cell_destruction.walls["West"] = False
                        neighbor.walls["East"] = False
                # maze.draw_maze()
                if Theme.animation_draw:
                    maze.draw_maze(False)
                    time.sleep(delay)
