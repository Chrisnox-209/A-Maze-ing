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


if __name__ == "__main__":
    main()
