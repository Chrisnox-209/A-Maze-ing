from utils.parser import clear, parsing_data
from maze.maze import Maze
from maze.utils_enum import Wall, WallUgly, WallDouble, WallRetro


def main() -> None:
    file_config = "config.txt"
    data: dict = {}
    data = parsing_data(file_config)

    if data is not False:
        maze = Maze(data, Wall)
        maze.logo()
        clear()
        maze.draw_maze()

        # maze.create_logo()
        # Menu(maze)
      #   maze.draw_maze(None)
      #   print(data)
      #   print(f"L'ID de la cellule (x=0, y=0) est : {print")
      #   print(f"L'ID de la cellule (x=0, y=10) est : {maze.grid[0][9].cell_id}")
      #   print(f"L'ID de la cellule (x=2, y=1) est : {maze.grid[1][2].cell_id}")


if __name__ == "__main__":
    clear()
    main()
