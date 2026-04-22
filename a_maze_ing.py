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
    
    #maze.generate_maze2()
    # maze.draw_grid()
    # maze.imperfect_maze()
    # maze.generate_maze("DEMO")
    # maze.generate_logo()
    maze.draw_maze(True)
    maze.generate_maze("DEMO")
    # maze.play_game()
    # maze.draw_path
    print()
    Menu(maze)
    #menu = Menu(maze)
    #menu.run()


if __name__ == "__main__":
    clear()
    main()
