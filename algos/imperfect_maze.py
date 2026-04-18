from random import shuffle, randrange
from maze.utils_enum import Color, Theme
from utils.parser import clear
import time

def imperfect_maze_func(maze):
    stack = [(maze.entry[0], maze.entry[1])]
    delay: int = Theme.delais_draw
    maze.all_cell_false()
    for height in range(maze.height):
        for width in range(maze.width):
            nbr_random = randrange(1, 10)
            cell_destruction = maze.grid[width][height]
            neighbor = maze.grid[width][height]
            if height != 0 and width != 0 and height != maze.height and width != maze.width - 1 and cell_destruction.visit is not True:
                if nbr_random == 1:
                        cell_destruction.walls["North"] = False
                        neighbor.walls["South"] = False
                elif nbr_random == 2:
                    cell_destruction.walls["West"] = False
                    neighbor.walls["East"] = False
                # maze.draw_maze()
                if Theme.animation_draw:
                    maze.draw_maze()
                    time.sleep(delay)
