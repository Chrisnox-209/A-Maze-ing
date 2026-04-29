from random import shuffle
from ..maze.utils_enum import Color
from collections import deque
from typing import Any


def find_path_bfs(maze: Any) -> None:
    """Trouve le chemin le plus court entre l'entrée et la sortie via BFS.
    Explore le labyrinthe niveau par niveau (parcours en largeur).
    Marque les cellules et reconstruit le chemin optimal.
    """
    maze.all_cell_false()
    for row in maze.grid:
        for cell2 in row:
            cell2.path_id = -1
    stack: deque[tuple[Any, Any]] = deque([(maze.entry[0], maze.entry[1])])
    path: dict[Any, Any] = {}
    while stack:
        cell_work = stack.popleft()
        x: Any = cell_work[0]
        y: Any = cell_work[1]

        if x == maze.exit[0] and y == maze.exit[1]:
            current: tuple[Any, Any] = (maze.exit[0], maze.exit[1])
            i: int = 0
            while current != (maze.entry[0], maze.entry[1]):
                maze.grid[current[1]][current[0]].path_id = i
                i += 1
                current = path[current]
            return
        cell: Any = maze.grid[y][x]
        cell.visit = True
        direction: list[tuple[Any, Any]] = [(x - 1, y),
                                            (x, y + 1),
                                            (x + 1, y),
                                            (x, y - 1)]
        shuffle(direction)
        for direct_x, direct_y in direction:
            if 0 <= direct_x < maze.width and 0 <= direct_y < maze.height:
                verif_visit: Any = maze.grid[direct_y][direct_x]
                if verif_visit.visit:
                    continue
                cell.color_case = Color.DEFAULT.value
                cell_destruction: Any = maze.grid[y][x]
                neighbor: Any = maze.grid[direct_y][direct_x]
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
