from maze.utils_enum import Color, Theme
from algos.algo_dfs import create_maze
from algos.algo_bfs import find_path_bfs
from algos.kruskal import kruskal
from maze.logo import Logo
import time
from algos.imperfect_maze import imperfect_maze_func

class Cell:
    def __init__(self, x: int, y: int, cell_id: int) -> None:
        self.x: int = int(x)
        self.y: int = int(y)
        self.cell_id: int = int(cell_id)
        self.color_case: Color = Theme.color_case
        self.visit = False
        self.walls: dict = {
            "North": True,
            "East": True,
            "South": True,
            "West": True
        }

    def __repr__(self) -> str:
        return f"{self.x}:{self.y}, id={self.cell_id}"


class Maze:
    def __init__(self, data: dict) -> None:
        self.width: int = data.WIDTH
        self.height: int = data.HEIGHT
        self.entry: int = (data.ENTRY_X, data.ENTRY_Y)
        self.exit: int = (data.EXIT_X, data.EXIT_Y)
        self.logo = Logo(self)
        self.seed = data.SEED
        self.generate_grid()

    def generate_grid(self) -> None:
        self.grid: list[list[Cell]] = []
        for y in range(self.height):
            row: list[Cell] = []
            for x in range(self.width):
                cell_id: int = y * self.width + x
                row.append(Cell(x, y, cell_id))
            self.grid.append(row)

    def generate_logo(self) -> None:
        self.logo.select_logo()

    def generate_maze(self) -> None:
        create_maze(self)

    def generate_maze2(self) -> None:
        kruskal(self)


    def imperfect_maze(self) -> None:
        imperfect_maze_func(self)


    def generate_path(self) -> None:
        # self.logo.select_logo()
        find_path_bfs(self)

    # laisse cette fonction pour le moment ca sert pour le debug pour voir la
    # matrice de chiffre
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
        self.generate_logo()

    def draw_maze(self) -> None:
        print("\033[H", end="")
        w = Theme.wall
        res = Color.DEFAULT.value
        entry = self.grid[self.entry[1]][self.entry[0]]
        exit_cel = self.grid[self.exit[1]][self.exit[0]]
        entry.color_case = Theme.entry_color_case
        exit_cel.color_case = Theme.exit_color_case
        for y in range(self.height):
            # La ligne du haut
            line_top = ""
            for x in range(self.width):
                cell = self.grid[y][x]
                cc = Theme.color_wall

                if y == 0:
                    inter = w.corner_tl.value if x == 0 else w.corner_tt.value
                else:
                    inter = w.corner_lt.value if x == 0 else w.corner_x.value

                if not cell.walls["North"]:
                    if cell.color_case != Color.DEFAULT.value:
                        h_char = cell.color_case + w.cursor.value
                    else:
                        h_char = w.box.value
                else:
                    h_char = Theme.color_wall + w.horizontal.value
                line_top += f"{cc}{inter}{h_char}{Color.DEFAULT.value}"
            last_inter = w.corner_tr.value if y == 0 else w.corner_rt.value
            print(
                f"{line_top}{
                    Theme.color_wall}{last_inter}{res}\033[K",
                flush=True)

            # La putain de ligne du millieu
            line_mid = ""
            for x in range(self.width):
                cell = self.grid[y][x]

                if not cell.walls["West"]:
                    if cell.color_case != Color.DEFAULT.value:
                        v_char = cell.color_case + w.cursor.value[0]
                    else:
                        v_char = " "
                else:
                    v_char = Theme.color_wall + w.vertical.value

                content = (
                    cell.color_case + w.cursor.value
                    if cell.color_case != Color.DEFAULT.value
                    else w.box.value
                )

                line_mid += f"{v_char}{content}{Color.DEFAULT.value}"
            print(
                f"{line_mid}{
                    Theme.color_wall}{
                    w.vertical.value}{res}\033[K",
                flush=True)
            # time.sleep(self.delay)
        # La ligne du bas
        line_bot = ""
        for x in range(self.width):
            cell = self.grid[self.height - 1][x]

            inter = w.corner_bl.value if x == 0 else w.corner_bt.value

            if not cell.walls["South"]:
                if cell.color_case != Color.DEFAULT.value:
                    h_char = cell.color_case + w.cursor.value
                else:
                    h_char = w.box.value
            else:
                h_char = Theme.color_wall + w.horizontal.value

            line_bot += f"{Theme.color_wall}{inter}{h_char}{Color.DEFAULT.value}"
        print(
            f"{line_bot}{
                Theme.color_wall}{
                w.corner_br.value}{res}\033[K",
            flush=True)
