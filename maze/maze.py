from maze.utils_enum import Color
import time


class Cell:
    def __init__(self, x: int, y: int, cell_id: int) -> None:
        self.x: int = int(x)
        self.y: int = int(y)
        self.cell_id: int = int(cell_id)
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
        self.is_logo = False

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

        # pour casser les mur il faut les casser sur
        # les deux cellules
        # sa evite de visiter la prochaine
        # chaque cellules a ses propres mur
        # chaque cellule possède son propre dictionnaire de murs

        # Super demo ici :
        # declaratiuon des cellules
        c1 = self.grid[1][1]
        c2 = self.grid[1][2]
        c3 = self.grid[1][3]

        # on casse les murs
        c1.walls["East"] = False
        c2.walls["West"] = False

        c2.walls["East"] = False
        c3.walls["West"] = False

        # on rempli les cases en couleur or 
        c1.color_case = Color.OR.value
        c2.color_case = Color.OR.value
        c3.color_case = Color.OR.value
        # ## fin de la super demo

        for y in range(self.height):

            # La ligne du haut
            line_top = ""
            for x in range(self.width):
                cell = self.grid[y][x]
                cc = self.color_wall

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
                    h_char = self.color_wall + w.horizontal.value

                line_top += f"{cc}{inter}{h_char}"

            last_inter = w.corner_tr.value if y == 0 else w.corner_rt.value
            print(f"{line_top}{self.color_wall}{last_inter}"
                  f"{Color.DEFAULT.value}", flush=True)
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

            inter = w.corner_bl.value if x == 0 else w.corner_bt.value

            if not cell.walls["South"]:
                if cell.color_case != Color.DEFAULT.value:
                    h_char = cell.color_case + w.cursor.value
                    h_char = w.box.value
            else:
                h_char = self.color_wall + w.horizontal.value

            line_bot += f"{self.color_wall}{inter}{h_char}"

        print(f"{line_bot}{self.color_wall}{w.corner_br.value}"
              f"{Color.DEFAULT.value}", flush=True)

    def logo(self):
        pattern = [
            [1, 0, 1, 0, 0, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 1]
        ]

        # ici on calcul le centrage
        # il faut rajouter un if else au nombre de cellules min
        # comme j'avais fait au debut dans le old
        # je pense WIDTH=12 et HEIGHT=9 c'est bien pour laisser deux case
        # j'ai aussi laissé deux cases entre le 4 et 2 pour faire passer
        # le labyrinthe
        start_x = (self.width - 8) // 2
        start_y = (self.height - 5) // 2

        for row in range(5):
            for col in range(8):
                if pattern[row][col] == 1:
                    grid_y = start_y + row
                    grid_x = start_x + col
                    cell = self.grid[grid_y][grid_x]
                    cell.color_case = Color.OR.value

                    if row > 0 and pattern[row - 1][col] == 1:
                        cell.walls["North"] = False
                    if row < 4 and pattern[row + 1][col] == 1:
                        cell.walls["South"] = False
                    if col > 0 and pattern[row][col - 1] == 1:
                        cell.walls["West"] = False
                    if col < 7 and pattern[row][col + 1] == 1:
                        cell.walls["East"] = False
