import readchar
from maze_core.mazegen.maze.utils_enum import Theme
from utils.parser import clear
from typing import Any


def resize(maze: Any) -> None:
    """Modifie dynamiquement les dimensions du labyrinthe depuis le menu.
    Demande à l'utilisateur de nouvelles valeurs et met à jour
    la configuration.
    Gère les erreurs de saisie.
    """
    print("╔═════════════════════════╗\n"
          "║      ✦ EDIT MODE ✦      ║\n"
          "╚═════════════════════════╝")
    print("[ MAZE RESIZING ] Use the arrow keys. Press ENTER to confirm.")

    while True:
        key: Any = readchar.readkey()

        if key in ['q', readchar.key.ENTER]:
            break

        moved = False
        if key in [readchar.key.DOWN]:
            maze.height += 1
            maze.generate_logo()
            maze.generate_grid()
            moved = True

        if key in [readchar.key.UP]:
            if maze.height > maze.entry[1] + \
                    1 and maze.height > maze.exit[1] + 1:
                if maze.height > 3:
                    maze.height -= 1
                    maze.generate_logo()
                    maze.generate_grid()
                    moved = True
                else:
                    print("\033[1;31m"
                          "⚠️  [ERROR]: RESIZING NOT POSSIBLE - "
                          "Minimum size has been reached ")
            else:
                print("\033[1;31m"
                      "⚠️  [ERROR]: RESIZING NOT POSSIBLE - "
                      "An element is blocking the resize")

        if key in [readchar.key.RIGHT]:
            maze.width += 1
            maze.generate_logo()
            maze.generate_grid()
            moved = True

        if key in [readchar.key.LEFT]:
            if maze.width > maze.entry[0] + \
                    1 and maze.width > maze.exit[0] + 1:
                if maze.width > 3:
                    maze.width -= 1
                    maze.generate_logo()
                    maze.generate_grid()
                    moved = True
                else:
                    print("\033[1;31m"
                          "⚠️  [ERROR]: RESIZING NOT POSSIBLE - "
                          "Minimum size has been reached ")
            else:
                print("\033[1;31m"
                      "⚠️  [ERROR]: RESIZING NOT POSSIBLE - "
                      "An element is blocking the resize")

        if moved:
            clear()
            maze.generate_logo()
            maze.draw_maze(False)
            moved = False
            print("╔═════════════════════════╗\n"
                  "║      ✦ EDIT MODE ✦      ║\n"
                  "╚═════════════════════════╝")
            print("[ MAZE RESIZING ] Use the arrow keys. "
                  "Press ENTER to confirm.")
            exit_id: int = maze.exit[1] * maze.width + maze.exit[0]
            entry_id: int = maze.entry[1] * maze.width + maze.entry[0]
            if exit_id in maze.logo_ids or entry_id in maze.logo_ids:
                print("\033[1;33m"
                      "⚠️  [WARNIN]: MAZE GENERATION ISSUE - "
                      "the entrance or exit is located inside the logo.")


def edit_door(maze: Any, door: str) -> None:
    """Permet de redéfinir manuellement les coordonnées de l'entrée ou de la
    sortie.
    Vérifie la validité des nouvelles coordonnées fournies.
    Met à jour l'instance du labyrinthe.
    """

    if door == "entry":
        x: Any = maze.entry[0]
        y: Any = maze.entry[1]
        name = "ENTRY"
    else:
        x = maze.exit[0]
        y = maze.exit[1]
        name = "EXIT"

    print("\033[H", end="", flush=True)
    maze.draw_maze(False)
    print("╔═════════════════════════╗\n"
          "║      ✦ EDIT MODE ✦      ║\n"
          "╚═════════════════════════╝")
    print(f"\n[ MOVEMENT {name} ] Use the arrow keys. Press ENTER to confirm.")

    while True:
        key: Any = readchar.readkey()
        if key in ['q', readchar.key.ENTER]:
            break

        moved = False
        old_x: Any = x
        old_y: Any = y

        if key in [readchar.key.RIGHT] and x < maze.width - 1:
            if maze.grid[y][x + 1].cell_id not in maze.logo_ids:
                if name == "ENTRY" and (x + 1, y) != maze.exit:
                    x += 1
                    moved = True
                elif name == "EXIT" and (x + 1, y) != maze.entry:
                    x += 1
                    moved = True

        elif key in [readchar.key.LEFT] and x > 0:
            if maze.grid[y][x - 1].cell_id not in maze.logo_ids:
                if name == "ENTRY" and (x - 1, y) != maze.exit:
                    x -= 1
                    moved = True
                elif name == "EXIT" and (x - 1, y) != maze.entry:
                    x -= 1
                    moved = True

        elif key in [readchar.key.UP] and y > 0:
            if maze.grid[y - 1][x].cell_id not in maze.logo_ids:
                if name == "ENTRY" and (x, y - 1) != maze.exit:
                    y -= 1
                    moved = True
                elif name == "EXIT" and (x, y - 1) != maze.entry:
                    y -= 1
                    moved = True

        elif key in [readchar.key.DOWN] and y < maze.height - 1:
            if maze.grid[y + 1][x].cell_id not in maze.logo_ids:
                if name == "ENTRY" and (x, y + 1) != maze.exit:
                    y += 1
                    moved = True
                elif name == "EXIT" and (x, y + 1) != maze.entry:
                    y += 1
                    moved = True

        if moved:
            maze.grid[old_y][old_x].color_case = Theme.color_case

            if door == "entry":
                maze.entry = (x, y)
            else:
                maze.exit = (x, y)

            print("\033[H", end="", flush=True)
            print("╔═════════════════════════╗\n"
                  "║      ✦ EDIT MODE ✦      ║\n"
                  "╚═════════════════════════╝")
            print(f"[ MOVEMENT {name} ] Use the arrow keys. "
                  "Press ENTER to confirm.")
            maze.draw_maze(False)


def play_game_func(maze: Any) -> None:
    """Lance le mode de jeu interactif où le joueur déplace un curseur.
    Gère les entrées clavier (flèches) pour naviguer dans le labyrinthe.
    Détecte les collisions avec les murs et la condition de victoire.
    """
    x: Any = maze.entry[0]
    y: Any = maze.entry[1]
    i = 0
    cell: Any = maze.grid[y][x]
    cell.path_active = True
    cell.path_content = "(S)"
    maze.logo.reset_logo()
    if Theme.logo_chrono:
        Theme.logo_midile = "0" + str(i)
        maze.generate_logo()
    maze.draw_maze(False)
    while True:
        if maze.exit[0] == x and maze.exit[1] == y:
            Theme.animation_draw_path = False
            maze.generate_path()
            maze.draw_path("basic")
            return
        key: Any = readchar.readkey()
        if key == 'q' or key == 'Q' or key == readchar.key.CTRL_C:
            break
        moved = False
        new_content = ""
        if key == readchar.key.RIGHT and cell.walls["East"] is not True:
            if maze.grid[y][x + 1].cell_id not in maze.logo_ids:
                x += 1
                new_content = "(>)"
                moved = True
        elif key == readchar.key.LEFT and cell.walls["West"] is not True:
            if maze.grid[y][x - 1].cell_id not in maze.logo_ids:
                x -= 1
                new_content = "(<)"
                moved = True
        elif key == readchar.key.UP and cell.walls["North"] is not True:
            if maze.grid[y - 1][x].cell_id not in maze.logo_ids:
                y -= 1
                new_content = "(^)"
                moved = True
        elif key == readchar.key.DOWN and cell.walls["South"] is not True:
            if maze.grid[y + 1][x].cell_id not in maze.logo_ids:
                y += 1
                new_content = "(v)"
                moved = True
        if moved:
            i += 1
            cell = maze.grid[y][x]
            cell.path_active = True
            cell.path_content = new_content
            maze.logo.reset_logo()
            if Theme.logo_chrono:
                Theme.logo_midile = "0" + str(i)
            maze.generate_logo()
            maze.draw_maze(False)
            maze.all_path_false()
