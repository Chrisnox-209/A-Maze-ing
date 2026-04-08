from utils.parser import clear, parsing_data
from maze.maze import Maze


def main() -> None:
    file_config = "config.txt"
    data: dict = {}
    if parsing_data(file_config) is not False:
        data = parsing_data(file_config)
        clear()
        maze = Maze(data)
        maze.draw_maze()
        print(data)
        print(f"L'ID de la cellule (x=0, y=0) est : {maze.grid[0][0].cell_id}")
        print(f"L'ID de la cellule (x=0, y=10) est : {maze.grid[0][9].cell_id}")
        print(f"L'ID de la cellule (x=2, y=1) est : {maze.grid[1][2].cell_id}")


if __name__ == "__main__":
    main()
