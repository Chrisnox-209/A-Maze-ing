import readchar
from maze.utils_enum import Theme
from utils.parser import clear


def resize(maze) -> None:
    from maze.maze import Cell
    while True:
        key = readchar.readkey()
        if key in ['q', readchar.key.ENTER]:
            break

        moved = False
        cell_id = (maze.height * maze.width) - 1
        row = maze.width
        col = maze.height
        x = maze.width - 1
        y = maze.height -1

        if key in [readchar.key.DOWN]:
            list_cell = []
            y += 1
            for i in range(row):
                cell_id = (y * row) + i
                list_cell.append(Cell(i, y, cell_id))
            maze.height += 1
            maze.generate_grid()
            moved = True

        if key in [readchar.key.UP]:
            maze.height -= 1
            maze.generate_grid()
            moved = True

        if moved:

            clear()
            print("-----")
            for i, line in enumerate(maze.grid):
                print(f"{i}-----")
                for cell in line:
                    print(cell)


            maze.draw_maze(False)
            moved = False


def edit_door(maze, door: str) -> None:

    if door == "entry":
        x = maze.entry[0]
        y = maze.entry[1]
        name = "ENTRY"
    else:
        x = maze.exit[0]
        y = maze.exit[1]
        name = "EXIT"

    print("\033[H", end="", flush=True)
    maze.draw_maze(False)
    print(f"\n[ MOVEMENT {name} ] Use the arrow keys. Press ENTER to confirm.")

    while True:
        key = readchar.readkey()
        if key in ['q', readchar.key.ENTER]:
            break

        moved = False
        old_x = x
        old_y = y

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
            maze.draw_maze(False)


def play_game_func(maze) -> None:
    x = maze.entry[0]
    y = maze.entry[1]
    i = 0
    cell = maze.grid[y][x]
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
            maze.draw_path()
            return
        key = readchar.readkey()
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
