import sys
from typing import Any, Literal
from maze.utils_enum import Color, Draw

class Cell:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = int(x)
        self.y: int = int(y)
        self.walls: dict = {
            "North": True,
            "East": False,
            "South": True,
            "West": True
        }
        self.visitee = False
        self.id: int = 0

    def __repr__(self) -> str:
        return f"{self.x}:{self.y}, id={self.id}"


class Maze:
    def __init__(self, data: dict) -> None:
        self.width: int = data["WIDTH"]
        self.height: int = data["HEIGHT"]
        self.grid: list[list[Cell]] = [[Cell(x_idx, y_idx)
                                        for x_idx in range(self.width)]
                                       for y_idx in range(self.height)]

    def set_color() -> None:
        pass

    def draw_maze(self) -> None:
        self.grid[5][4].walls["North"] = False
        self.grid[0][0].walls["North"] = False
        for y in range(self.height):
            for x in range(self.width):
                data_cell = self.grid[y][x]
                if data_cell.walls["North"]:
                    print(Draw.TOP_WALL.value, end="")
                else:
                    print(Draw.TOP_PATH.value, end="")
            print(Draw.CORNER.value)

            for _ in range(1):
                for x in range(self.width):
                    data_cell: Cell = self.grid[y][x]
                    if data_cell.walls["West"]:
                        print(Draw.MID_WALL.value, end="")
                    else:
                        print(Draw.MID_PATH.value, end="")
                print(Draw.V_LINE.value)

        for x in range(self.width):
            print(Draw.CORNER_BOT.value + Draw.BOTTOM.value, end="")
        print(Draw.CORNER_BOT.value)
