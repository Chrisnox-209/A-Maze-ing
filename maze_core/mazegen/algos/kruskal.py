from maze_core.mazegen.maze.utils_enum import Color, Theme
import random
import time
from maze_core.mazegen.options.timer import Timer
from typing import Any


def kruskal(maze: Any) -> None:
    breakable_walls: list = wall_classification(maze)
    familly_cell: dict = cell_familly(maze)
    create_family(maze, breakable_walls, familly_cell)


def wall_classification(maze: Any) -> list:
    breakable_walls: list = []

    for y in range(maze.height):
        for x in range(maze.width):
            pos: Any = maze.grid[y][x]

            if x > 0:
                west_cell: Any = maze.grid[y][x - 1]
                if (pos.cell_id not in maze.logo_ids and
                   west_cell.cell_id not in maze.logo_ids):
                    breakable_walls.append(("W", pos, west_cell))

            if x < maze.width - 1:
                east_cell: Any = maze.grid[y][x + 1]
                if (pos.cell_id not in maze.logo_ids and
                   east_cell.cell_id not in maze.logo_ids):
                    breakable_walls.append(("E", pos, east_cell))

            if y > 0:
                north_cell: Any = maze.grid[y - 1][x]
                if (pos.cell_id not in maze.logo_ids and
                   north_cell.cell_id not in maze.logo_ids):
                    breakable_walls.append(("N", pos, north_cell))

            if y < maze.height - 1:
                south_cell: Any = maze.grid[y + 1][x]
                if (pos.cell_id not in maze.logo_ids and
                   south_cell.cell_id not in maze.logo_ids):
                    breakable_walls.append(("S", pos, south_cell))

    return breakable_walls


def cell_familly(maze: Any) -> dict:
    familly_cell: dict = {}
    for line in maze.grid:
        for id in line:
            familly_cell[id.cell_id] = id.cell_id
    return familly_cell


def check_familly(id_cell: int, id_neighbor: int, familly_cell: dict) -> bool:
    if familly_cell[id_cell] == familly_cell[id_neighbor]:
        return True
    else:
        return False


def pair_wall(direction: str) -> tuple[str, str]:
    if direction == 'N':
        return ("North", "South")
    if direction == 'S':
        return ("South", "North")
    if direction == 'E':
        return ("East", "West")
    if direction == 'W':
        return ("West", "East")
    raise ValueError(f"Invalid direction: {direction}")


list_color: list[str] = ["NEON_RED",
                         "NEON_GREEN",
                         "NEON_YELLOW",
                         "NEON_BLUE",
                         "NEON_CYAN",
                         "NEON_MAGENTA",
                         "NEON_ORANGE",
                         "NEON_PURPLE",
                         "NEON_PINK",]


def create_family(maze: Any,
                  breakable_walls: list,
                  familly_cell: dict) -> None:
    total_cell: Any = maze.width * maze.height - len(maze.logo_ids)
    nb_wall_broken = 0
    time_start = Timer()
    if maze.seed is not None:
        random.seed(maze.seed)

    random.shuffle(breakable_walls)
    while len(breakable_walls) > 0:
        element: Any = breakable_walls[0]
        direction: Any = element[0]
        cell1: Any = element[1]
        cell2: Any = element[2]
        check: bool = check_familly(cell1.cell_id, cell2.cell_id, familly_cell)
        if check:
            del breakable_walls[0]
        else:
            wall_1: Any
            wall_2: Any
            wall_1, wall_2 = pair_wall(direction)
            cell1.walls[wall_1] = False
            cell2.walls[wall_2] = False

            col: str = random.choice(list_color)
            color_case: Any = getattr(Color, col).value

            if Theme.animation_algo:
                cell2.color_case = color_case
                cell1.color_case = color_case

            old_familly: Any = familly_cell[cell2.cell_id]
            new_familly: Any = familly_cell[cell1.cell_id]

            for id_cell in familly_cell:
                if familly_cell[id_cell] == old_familly:
                    familly_cell[id_cell] = new_familly
            del breakable_walls[0]
            nb_wall_broken += 1

        if nb_wall_broken == total_cell - 1:
            cell1.color_case = Color.DEFAULT.value
            cell2.color_case = Color.DEFAULT.value
            break

        if Theme.logo_chrono and Theme.animation_algo:
            maze.logo.reset_logo()
            maze.logo.reset_logo()
            maze.generate_logo()
            timestr: str = f"{time_start.get_time(): .0f}"
            Theme.logo_midile = str(timestr)
            maze.generate_logo()

        if Theme.animation_algo:
            maze.draw_maze(False)
            if nb_wall_broken < ((total_cell - 1) * 19) / 20:
                time.sleep(0.015)

            cell1.color_case = Color.DEFAULT.value
            cell2.color_case = Color.DEFAULT.value
    maze.draw_maze(False)
