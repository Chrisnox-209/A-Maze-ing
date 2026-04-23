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
    maze.draw_maze(True)
    maze.generate_maze("DEMO")
    print()
    Menu(maze)


if __name__ == "__main__":
    clear()
    main()
