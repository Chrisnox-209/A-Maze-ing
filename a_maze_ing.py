from utils.parser import clear, parsing_data, MazeConfig
from maze.maze import Maze
from maze.utils_enum import Wall, WallUgly, WallDouble, WallRetro
from menu import Menu

def main() -> None:
    file_config = "config.txt"
    config = parsing_data(file_config)
    if config is False:
        print(f"[ERROR]: file {file_config}")
        return
    maze = Maze(config)
    maze.generate_logo()
    # maze.imperfect_maze()
    # maze.generate_path()
    # maze.draw_grid()
    maze.draw_maze()
    Menu(maze)


if __name__ == "__main__":
    clear()
    main()
