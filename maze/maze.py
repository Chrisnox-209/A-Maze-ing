from maze.utils_enum import Wall, WallDouble, WallSkinny, WallRetro, WallUgly, Color
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
    def __init__(self, data: dict) -> None:
        self.width: int = data["WIDTH"]
        self.height: int = data["HEIGHT"]
        self.grid: list[list[Cell]] = []
        self.color_select = Color.DEFAULT.value
        for y in range(self.height):
            row: list[Cell] = []
            for x in range(self.width):
                cell_id: int = y * self.width + x
                row.append(Cell(x, y, cell_id))
            self.grid.append(row)

    def set_color() -> None:
        pass

    def create_logo(self):
        x = int(self.width / 2) - 3
        y = int(self.height / 2) - 1
        self.grid[y][x].walls["North"] = False
        self.grid[y + 1][x].walls["North"] = False
        self.grid[y + 1][x + 1].walls["West"] = False
        self.grid[y + 1][x + 2].walls["West"] = False
        self.grid[y + 2][x + 2].walls["North"] = False
        self.grid[y + 3][x + 2].walls["North"] = False
        self.grid[y][x].color_case = Color.BG_YELLOW.value
        self.grid[y + 1][x].color_case = Color.BG_YELLOW.value


        self.grid[y - 1][x + 4].walls["West"] = False
        self.grid[y - 1][x + 5].walls["West"] = False
        self.grid[y][x + 5].walls["North"] = False
        self.grid[y + 1][x + 5].walls["North"] = False
        self.grid[y + 1][x + 4].walls["West"] = False
        self.grid[y + 1][x + 5].walls["West"] = False
        self.grid[y + 2][x + 3].walls["North"] = False
        self.grid[y + 3][x + 3].walls["North"] = False
        self.grid[y + 3][x + 4].walls["West"] = False
        self.grid[y + 3][x + 5].walls["West"] = False

    def draw_maze(self, wall) -> None:
        delais = 0.001
        if wall is None:
            wall = Wall
        if wall == "random":
            list_style = [
                Wall,
                WallDouble,
                WallSkinny,
                WallRetro,
                WallUgly
            ]
            wall = random.choice(list_style)
        for y in range(self.height):
            for x in range(self.width):
                if y == 0:
                    inter = (
                        wall.TOP_LEFT.value if x == 0 else wall.T_TOP.value
                    )
                else:
                    inter = (
                        wall.T_LEFT.value if x == 0 else wall.CROSS.value
                    )
                time.sleep(delais)
                print(
                    f"{self.color_select}{inter}{Color.DEFAULT.value}",
                    end="",
                    flush=True
                )

                if self.grid[y][x].walls["North"]:
                    time.sleep(delais)
                    print(
                        f"{self.grid[y][x].color_case}{wall.H_LINE.value}"
                        f"{Color.DEFAULT.value}",
                        end="",
                        flush=True
                    )
                else:
                    time.sleep(delais)
                    print(
                        f"{self.grid[y][x].color_case}{wall.H_PATH.value}"
                        f"{Color.DEFAULT.value}",
                        end="",
                        flush=True
                    )
            if y == 0:
                time.sleep(delais)
                print(
                    f"{Color.DEFAULT.value}{wall.TOP_RIGHT.value}"
                    f"{Color.DEFAULT.value}"
                )
            else:
                time.sleep(delais)
                print(
                    f"{Color.DEFAULT.value}{wall.T_RIGHT.value}"
                    f"{Color.DEFAULT.value}"
                )

            for x in range(self.width):
                if self.grid[y][x].walls["West"]:
                    time.sleep(delais)
                    print(
                        f"{Color.DEFAULT.value}{wall.V_LINE.value}"
                        f"{Color.DEFAULT.value}",
                        end="",
                        flush=True
                    )
                else:
                    time.sleep(delais)
                    print(
                        f"{self.grid[y][x].color_case}{wall.V_PATH.value}"
                        f"{Color.DEFAULT.value}",
                        end="",
                        flush=True
                    )
            time.sleep(delais)
            print(
                f"{self.grid[y][x].color_case}{wall.V_RIGHT.value}"
                f"{Color.DEFAULT.value}"
            )

        for x in range(self.width):
            inter = wall.BOT_LEFT.value if x == 0 else wall.T_BOT.value
            time.sleep(delais)
            print(
                f"{self.grid[y][x].color_case}{inter}{wall.H_LINE.value}"
                f"{Color.DEFAULT.value}",
                end="",
                flush=True
            )
        time.sleep(delais)
        print(
            f"{self.grid[y][x].color_case}{wall.BOT_RIGHT.value}"
            f"{Color.DEFAULT.value}"
        )
