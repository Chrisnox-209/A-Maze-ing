import sys
import random
import time
from typing import Any
try:
    from maze_core.mazegen.algos.algo_bfs import find_path_bfs # type: ignore
    from maze_core.mazegen.algos.algo_dfs import dfs # type: ignore
    from maze_core.mazegen.algos.kruskal import kruskal # type: ignore
    from maze_core.mazegen.maze.logo import Logo # type: ignore
    from maze_core.mazegen.algos.imperfect_maze import imperfect_maze_func # type: ignore
    from maze_core.mazegen.maze.output_maze import output_maze_func # type: ignore
    from maze_core.mazegen.options.timer import Timer # type: ignore
    from maze_core.mazegen.maze.utils_enum import Color, Theme # type: ignore
except Exception as e:
    print(e)
    sys.exit(1)


class Cell:
    def __init__(self, x: int, y: int, cell_id: int) -> None:
        self.x: int = int(x)
        self.y: int = int(y)
        self.cell_id = int(cell_id)
        self.color_case = Theme.color_case
        self.visit = False
        self.path_id = -1
        self.path_active = False
        self.path_content = "   "
        self.walls: dict = {
            "North": True,
            "East": True,
            "South": True,
            "West": True
        }

    def __repr__(self) -> str:
        return f"{self.x}:{self.y}, id={self.cell_id}"


class Maze:
    def __init__(self, data: Any) -> None:
        self.width: int = data.WIDTH
        self.height: int = data.HEIGHT
        self.entry: tuple[int, int] = (data.ENTRY_X, data.ENTRY_Y)
        self.exit: tuple[int, int] = (data.EXIT_X, data.EXIT_Y)
        self.logo: Logo = Logo(self)
        self.seed: str | None = data.SEED
        self.file: str = data.OUTPUT_FILE
        self.perfect: bool = data.PERFECT
        self.delay = 0.08
        self.generate_grid()

    def generate_grid(self) -> None:
        self.grid: list[list[Cell]] = []
        for y in range(self.height):
            row: list[Cell] = []
            for x in range(self.width):
                cell_id: int = y * self.width + x
                row.append(Cell(x, y, cell_id))
            self.grid.append(row)

    def output_maze(self) -> None:
        output_maze_func(self)

    def generate_logo(self) -> None:
        self.logo = Logo(self)
        return self.logo.select_logo()

    def generate_maze(self, algo_name: str) -> None:
        algorithms = ["DFS", "KRUSKAL", "PRIMS", "DEMO"]
        if algo_name not in algorithms:
            raise ValueError(f"Unknown algorithm: {algo_name}")
        if algo_name == "DFS":
            dfs(self)
            self.output_maze()
        elif algo_name == "KRUSKAL":
            kruskal(self)
            self.output_maze()

        elif algo_name == "DEMO":
            self.logo.make_logo_start()

    def imperfect_maze(self) -> None:
        imperfect_maze_func(self)

    def generate_path(self) -> None:
        find_path_bfs(self)

    def draw_grid(self) -> None:
        for data in self.grid:
            for visited in data:
                if not visited.visit:
                    print("0 ", end='')
                else:
                    print("1 ", end='')
            print()

    def all_cell_false(self) -> None:
        for height in self.grid:
            for width in height:
                width.visit = False
        if Theme.logo_midile:
            self.generate_logo()

    def draw_path(self, type: str) -> None:
        max_id_path = 0
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                if cell.path_id > max_id_path:
                    max_id_path = cell.path_id

        if type == "game":
            i = max_id_path
            old_x = 0
            old_y = 0
            while i != 0:
                for y in range(self.height):
                    for x in range(self.width):
                        cell = self.grid[y][x]
                        if cell.path_id != -1 and cell.path_id == i:
                            self.logo.reset_logo()
                            self.generate_logo()
                            if Theme.logo_chrono:
                                Theme.logo_midile = "0" + str(i)
                                self.generate_logo()
                            cell.path_active = True
                            if old_x < x:
                                cell.path_content = "(>)"
                                old_x = x
                            elif old_x > x:
                                cell.path_content = "(<)"
                                old_x = x
                            elif old_y > y:
                                cell.path_content = "(^)"
                                old_y = y
                            elif old_y < y:
                                cell.path_content = "(v)"
                                old_y = y
                            self.draw_maze(False)
                            cell.path_active = False
                            time.sleep(0.1)
                            i -= 1
                            break
        elif type == "basic":
            valid_colors = [
                c.value for c in Color
                if c not in (Color.RESET, Color.DEFAULT)]
            self.color = random.choice(valid_colors)
            time_start = Timer()
            b = 0
            while b <= max_id_path:
                i = max_id_path
                while i >= b:
                    for y in range(self.height):
                        for x in range(self.width):
                            cell = self.grid[y][x]
                            if cell.path_id == i:
                                if Theme.logo_chrono:
                                    self.logo.reset_logo()
                                    self.generate_logo()
                                    timestr = f"{time_start.get_time(): .0f}"
                                    Theme.logo_midile = str(timestr)
                                    self.generate_logo()
                                cell.color_case = Theme.color_path
                                self.draw_maze(False)
                                if i > b:
                                    cell.color_case = Color.DEFAULT.value
                                break
                    i -= 1
                b += 1

    def all_path_false(self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                cell.path_active = False

    def draw_maze(self, start: bool) -> None:
        print("\033[H", end="")
        w = Theme.wall
        res = Color.DEFAULT.value
        entry = self.grid[self.entry[1]][self.entry[0]]
        exit_cel = self.grid[self.exit[1]][self.exit[0]]
        entry.color_case = Theme.entry_color_case
        exit_cel.color_case = Theme.exit_color_case
        for y in range(self.height):
            line_top = ""
            for x in range(self.width):
                cell = self.grid[y][x]
                cc = Theme.color_wall

                if y == 0:
                    inter = w.corner_tl.value if x == 0 else w.corner_tt.value
                else:
                    inter = w.corner_lt.value if x == 0 else w.corner_x.value

                if not cell.walls["North"]:
                    if (cell.color_case != Color.DEFAULT.value
                       and cell != entry and cell != exit_cel):
                        h_char = cell.color_case + w.cursor.value
                    else:
                        h_char = w.box.value
                else:
                    h_char = Theme.color_wall + w.horizontal.value
                line_top += f"{cc}{inter}{h_char}{Color.DEFAULT.value}"
            last_inter = w.corner_tr.value if y == 0 else w.corner_rt.value
            print(
                f"{line_top}{Theme.color_wall}{last_inter}{res}\033[K",
                flush=True)

            line_mid = ""
            for x in range(self.width):
                cell = self.grid[y][x]

                if not cell.walls["West"]:
                    if (cell.color_case != Color.DEFAULT.value
                       and cell != entry and cell != exit_cel):
                        v_char = cell.color_case + w.cursor.value[0]
                    else:
                        v_char = " "
                else:
                    v_char = Theme.color_wall + w.vertical.value

                if cell.path_active is not True:
                    content = (
                        cell.color_case + w.cursor.value
                        if cell.color_case != Color.DEFAULT.value
                        else w.box.value
                    )
                else:
                    content = (
                        cell.color_case + w.cursor.value
                        if cell.color_case != Color.DEFAULT.value
                        else cell.path_content
                    )

                line_mid += f"{v_char}{content}{Color.DEFAULT.value}"
            print(
                f"{line_mid}{Theme.color_wall}{w.vertical.value}{res}\033[K",
                flush=True)
            if start:
                time.sleep(self.delay)
        line_bot = ""
        for x in range(self.width):
            cell = self.grid[self.height - 1][x]
            inter = w.corner_bl.value if x == 0 else w.corner_bt.value
            if not cell.walls["South"]:
                if (cell.color_case != Color.DEFAULT.value
                   and cell != entry and cell != exit_cel):
                    h_char = cell.color_case + w.cursor.value
                else:
                    h_char = w.box.value
            else:
                h_char = Theme.color_wall + w.horizontal.value

            line_bot += f"{Theme.color_wall}{inter}{h_char}"
            f"{Color.DEFAULT.value}"
        print(
            f"{line_bot}{Theme.color_wall}{w.corner_br.value}{res}\033[K",
            flush=True)
