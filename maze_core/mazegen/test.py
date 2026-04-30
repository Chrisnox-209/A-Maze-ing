# import
from mazegen.maze.maze import Maze, Theme
import os


def test() -> None:
    # dictionary declaration
    dict_data: dict[str, int] = {
        "WIDTH": 10,
        "HEIGHT": 10,
        "ENTRY_X": 1,
        "ENTRY_Y": 1,
        "EXIT_X": 9,
        "EXIT_Y": 9,
    }

    # activate animation
    Theme.animation_algo = True

    try:
        # Initialize a new maze
        maze = Maze(dict_data)

        # grid generation
        maze.generate_grid()
        # logo generation
        maze.generate_logo()

        # generate maze
        maze.generate_maze("KRUSKAL")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    test()
    try:
        with open("exit.txt", "r", encoding="utf-8") as f:
            contenu: str = f.read()

        print(contenu)
    except FileNotFoundError:
        print("The file does not exist")

    except Exception as e:
        print(f"[error]: {e}")
