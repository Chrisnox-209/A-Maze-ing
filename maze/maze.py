from maze.utils_enum import Wall, WallDouble, WallSkinny, WallRetro, WallUgly
from typing import Any
import time
import random


class Cell:
    def __init__(self, x: int, y: int, cell_id: int) -> None:
        self.x: int = int(x)
        self.y: int = int(y)
        self.cell_id: int = int(cell_id)
        self.visitee: bool = False
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

        for y in range(self.height):
            row: list[Cell] = []
            for x in range(self.width):
                cell_id: int = y * self.width + x
                row.append(Cell(x, y, cell_id))
            self.grid.append(row)

    def set_color() -> None:
        pass

    def draw_maze(self) -> None:
        delais = 0.001
        list_style: list[str] = [Wall,
                                 WallDouble,
                                 WallSkinny,
                                 WallRetro,
                                 WallUgly]
        wall: str = random.choice(list_style)

        for y in range(self.height):

            for x in range(self.width):
                if y == 0:
                    inter: Any = wall.TOP_LEFT.value if x == 0 else wall.T_TOP.value
                else:
                    inter = wall.T_LEFT.value if x == 0 else wall.CROSS.value
                time.sleep(delais)
                print(inter, end="")

                if self.grid[y][x].walls["North"]:
                    time.sleep(delais)
                    print(wall.H_LINE.value, end="", flush=True)
                else:
                    time.sleep(delais)
                    print(wall.H_PATH.value, end="", flush=True)

            if y == 0:
                time.sleep(delais)
                print(wall.TOP_RIGHT.value)
            else:
                time.sleep(delais)
                print(wall.T_RIGHT.value)

            for x in range(self.width):
                if self.grid[y][x].walls["West"]:
                    time.sleep(delais)
                    print(wall.V_LINE.value, end="", flush=True)
                else:
                    time.sleep(delais)
                    print(wall.V_PATH.value, end="", flush=True)
            time.sleep(delais)
            print(wall.V_RIGHT.value)

        for x in range(self.width):
            inter = wall.BOT_LEFT.value if x == 0 else wall.T_BOT.value
            time.sleep(delais)
            print(inter + wall.H_LINE.value, end="", flush=True)
        time.sleep(delais)
        print(wall.BOT_RIGHT.value)