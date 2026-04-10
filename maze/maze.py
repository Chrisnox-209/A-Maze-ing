from maze.utils_enum import Wall, Color
from typing import Any
import time
import random


class Cell:
    def __init__(self, x: int, y: int, cell_id: int) -> None:
        self.x: int = int(x)
        self.y: int = int(y)
        self.cell_id: int = int(cell_id)
        self.visitee: bool = False
        self.color_case: Color = Color.DEFAULT.value
        self.walls: dict = {
            "North": True,
            "East": True,
            "South": True,
            "West": True
        }

    def __repr__(self) -> str:
        return f"{self.x}:{self.y}, id={self.cell_id}"


class Maze:
    def __init__(self, data: dict, wall_style) -> None:
        self.width: int = data["WIDTH"]
        self.height: int = data["HEIGHT"]
        self.grid: list[list[Cell]] = []
        self.color_select = Color.DEFAULT.value
        self.wall = wall_style
        self.color_wall = Color.BLEU.value

        for y in range(self.height):
            row: list[Cell] = []
            for x in range(self.width):
                cell_id: int = y * self.width + x
                row.append(Cell(x, y, cell_id))
            self.grid.append(row)

    def set_color() -> None:
        pass

    def draw_maze(self) -> None:
        w = self.wall
        delay = 0.05
        for y in range(self.height):

            # La ligne du haut
            line_top = ""
            for x in range(self.width):
                cell = self.grid[y][x]
                cc = self.color_wall

                if y == 0:
                    inter = w.corners_tl.value if x == 0 else w.corners_tt.value
                else:
                    inter = w.corners_lt.value if x == 0 else w.corners_x.value

                if not cell.walls["North"]:
                    if cell.color_case != Color.DEFAULT.value:
                        h_char = cell.color_case + w.cursor.value
                    else:
                        h_char = w.box.value
                else:
                    h_char = self.color_wall + w.horizontal.value

                line_top += f"{cc}{inter}{h_char}"

            last_inter = w.corners_tr.value if y == 0 else w.corners_rt.value
            print(f"{line_top}{self.color_wall}{last_inter}{Color.DEFAULT.value}", flush=True)
            time.sleep(delay)

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
                    v_char = self.color_wall + w.vertical.value

                content = (
                    cell.color_case + w.cursor.value
                    if cell.color_case != Color.DEFAULT.value
                    else w.box.value
                )

                line_mid += f"{v_char}{content}{Color.DEFAULT.value}"

            print(f"{line_mid}{self.color_wall}{w.vertical.value}", flush=True)
            time.sleep(delay)

        # La ligne du bas
        line_bot = ""
        for x in range(self.width):
            cell = self.grid[self.height - 1][x]

            inter = w.corners_bl.value if x == 0 else w.corners_bt.value

            if not cell.walls["South"]:
                if cell.color_case != Color.DEFAULT.value:
                    h_char = cell.color_case + w.cursor.value
                else:
                    h_char = w.box.value
            else:
                h_char = self.color_wall + w.horizontal.value

            line_bot += f"{self.color_wall}{inter}{h_char}"

        print(f"{line_bot}{self.color_wall}{w.corners_br.value}{Color.DEFAULT.value}", flush=True)

    def logo(self):
        p4 = [
            [1,0,1],
            [1,0,1],
            [1,1,1],
            [0,0,1],
            [0,0,1]
        ]

        p2 = [
            [1,1,1],
            [0,0,1],
            [1,1,1],
            [1,0,0],
            [1,1,1]
        ]

        # ici on calcul le centrage
        # il faut rajouter un if else au nombre de cellules min
        # comme j'avais fait au debut dans le old
        #je pense WIDTH=12 et HEIGHT=9 c'est bien pour laisser deux case
        #j'ai aussi laissé deux cases entre le 4 et 2 pour faire passer
        #le labyrinthe
        start_x = (self.width - 8) // 2
        start_y = (self.height - 5) // 2

        logo_cells = []

        for y in range(5):
            for x in range(3):
                if p4[y][x]:
                    logo_cells.append((start_y + y, start_x + x))

        for y in range(5):
            for x in range(3):
                if p2[y][x]:
                    logo_cells.append((start_y + y, start_x + 5 + x))


        for y, x in logo_cells:
            cell = self.grid[y][x]
            cell.color_case = Color.OR.value
            if y > 0 and (y - 1, x) in logo_cells:
                cell.walls["North"] = False
            if x < self.width - 1 and (y, x + 1) in logo_cells:
                cell.walls["East"] = False
            if y < self.height - 1 and (y + 1, x) in logo_cells:
                cell.walls["South"] = False
            if x > 0 and (y, x - 1) in logo_cells:
                cell.walls["West"] = False

