from utils.parser import clear, parsing_data
from maze_core.mazegen.maze.maze import Maze
from options.menu import Menu


def main() -> None:
    file_config = "config.txt"
    config = parsing_data(file_config)
    if config is False:
        print(f"[ERROR]: file {file_config}")
        return
    maze = Maze(config)

    if maze.width > 11 and maze.height > 8:
        maze.draw_maze(True)
        maze.generate_maze("DEMO")
    else:
        maze.generate_logo()
        maze.draw_maze(True)

    print()
    Menu(maze)


if __name__ == "__main__":
    clear()
    main()
