from utils.parser import clear, parsing_data
from maze_core.mazegen.maze.maze import Maze, Theme
from options.menu import Menu
import sys


def main() -> None:
    """Point d'entrée principal du programme.
    Parse la configuration, initialise le labyrinthe et lance l'affichage.
    Démarre ensuite le menu interactif pour l'utilisateur.
    """
    Theme.animation_algo = True
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".txt"):
        print(
            "[ERROR] -> Usage: python a_maze_ing.py <config_file.txt> "
        )
        sys.exit(1)
    file_config: str = sys.argv[1]
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
