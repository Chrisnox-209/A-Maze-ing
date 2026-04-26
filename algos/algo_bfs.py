from random import shuffle
from maze.utils_enum import Color
from collections import deque


def find_path_bfs(maze):
    maze.all_cell_false()
    stack = deque([(maze.entry[0], maze.entry[1])])
    path = {}
    while stack:
        cell_work = stack.popleft()
        x = cell_work[0]
        y = cell_work[1]
        if x == maze.exit[0] and y == maze.exit[1]:
            current = (maze.exit[0], maze.exit[1])
            i: int = 0
            while current != (maze.entry[0], maze.entry[1]):
                maze.grid[current[1]][current[0]].path_id = i
                i += 1
                current = path[current]
            return
        cell = maze.grid[y][x]
        cell.visit = True
        direction = [(x - 1, y),
                     (x, y + 1),
                     (x + 1, y),
                     (x, y - 1)]
        shuffle(direction)
        for direct_x, direct_y in direction:
            if 0 <= direct_x < maze.width and 0 <= direct_y < maze.height:
                verif_visit = maze.grid[direct_y][direct_x]
                if verif_visit.visit:
                    continue
                cell.color_case = Color.DEFAULT.value
                cell_destruction = maze.grid[y][x]
                neighbor = maze.grid[direct_y][direct_x]
                if direct_x == x and not verif_visit.visit:
                    if direct_y < y and not cell_destruction.walls["North"]:
                        neighbor.visit = True
                        stack.append((direct_x, direct_y))
                        path[(direct_x, direct_y)] = (x, y)

                    elif direct_y > y and not cell_destruction.walls["South"]:
                        neighbor.visit = True
                        stack.append((direct_x, direct_y))
                        path[(direct_x, direct_y)] = (x, y)

                elif direct_y == y and not verif_visit.visit:
                    if direct_x < x and not cell_destruction.walls["West"]:
                        neighbor.visit = True
                        stack.append((direct_x, direct_y))
                        path[(direct_x, direct_y)] = (x, y)

                    elif direct_x > x and not cell_destruction.walls["East"]:
                        neighbor.visit = True
                        stack.append((direct_x, direct_y))
                        path[(direct_x, direct_y)] = (x, y)
