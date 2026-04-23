import sys
import readchar
from rich.console import Console, Group
from rich.panel import Panel
from utils.parser import clear
from rich.text import Text
from rich.table import Table
from rich.live import Live
from rich.align import Align
from rich.columns import Columns
from typing import Literal, Any, Optional
from options import edit_door
from maze.utils_enum import (
    WallDouble,
    Wall,
    WallSkinny,
    WallRetro,
    WallUgly,
    WallBig,
    Theme,
    Color
)


def get_menu_content(
        options,
        current_index,
        is_active,
        menu_type,
        selected_val=None,
        checked_dict=None) -> Group:
    render_opts: list = []

    if checked_dict is None:
        checked_dict = {}

    for i, opt in enumerate(options):
        if menu_type in ["MAIN", "CONFIG"]:
            prefix_text = "▶ " if (
                is_active and i == current_index) else "  "

            if menu_type == "CONFIG" and i in checked_dict:
                mark: Literal['X'] | Literal[' '] = (
                    "X" if checked_dict[i] else " ")
                prefix_text += f"[{mark}] "

        elif menu_type == "WALLS":
            prefix_text = "█ " if opt == selected_val else "░ "
        elif menu_type in ("COLOR_W", "COLOR_L", "COLOR_P"):
            prefix_text = "● " if opt == selected_val else "○ "
        else:
            mark = "X" if opt == selected_val else " "
            prefix_text = f"[{mark}] "

        if is_active and i == current_index:
            if opt == "EXIT PROGRAM":
                prefix: Any = Text(prefix_text, style="bold red")
                content: Any = Text(f" {opt} ", style="bold white on red")
            else:
                prefix = Text(prefix_text, style="bold yellow")
                content = Text(f" {opt} ", style="black on yellow")

            render_opts.append(Text.assemble(prefix, content))
        else:

            is_checked_config: Optional[bool] = (
                menu_type == (
                    "CONFIG" and i in checked_dict and checked_dict[i])
            )

            if opt == "EXIT PROGRAM":
                style = "light_coral"
            elif (menu_type in ["WALLS",
                                "ALGO",
                                "LOGO",
                                "COLOR_W",
                                "COLOR_L",
                                "COLOR_P"]
                  and opt == selected_val) or is_checked_config:
                style = "bold green"
            else:
                style = (
                    "dim cyan" if menu_type not in [
                        "MAIN", "CONFIG"] else "cyan")

            render_opts.append(Text(f"{prefix_text}{opt}", style=style))

    return Group(*render_opts)


def Menu(maze) -> None:
    console: Any = Console()
    main_opts: list[str] = ["GENERATE", "SOLVE PATH", "UPDATE", "RESET",
                            "PAKAGE","PLAY GAME" ,"EXIT PROGRAM"]
    config_opts: list[str] = ["PERFECT", "DESIGN", "ENTRY", "EXIT", "SIZE"]
    style_opts: list[str] = ["CLASSIC WALL", "DOUBLE WALL",
                             "SKINNY WALL", "RETRO WALL",
                             "UGLY WALL", "BIG WALL"]
    list_algo: list[str] = ["DFS", "KRUSKAL", "PRIMS"]
    colors_list: list[str] = ["RED", "GREEN", "YELLOW", "BLUE",
                              "MAGENTA", "CYAN", "WHITE",
                              "ORANGE", "PINK"]
    logos_list: list[str] = ["LOGO_42", "TIMER", "POOH", "HEART", "SURPRISE"]

    wall_name: str = style_opts[0]
    algo_name: str = list_algo[0]
    logo_name: str = logos_list[0]
    color_wall: str = colors_list[6]
    color_case_logo: str = colors_list[0]
    color_path: str = colors_list[1]

    current_menu = "MAIN"
    index = 0

    show_advanced = False
    is_perfect = maze.perfect

    color_text_top = "bold bright_blue"
    color_frame = "white"
    color_select_frame = "cyan"

    with Live(console=console, refresh_per_second=10, transient=False) as live:
        while True:

            status_table: Table = Table.grid(expand=False)
            status_table.add_column(justify="right", width=20)
            status_table.add_column(justify="left", width=20)
            status_table.add_column(justify="center", width=3)
            status_table.add_column(justify="right", width=20)
            status_table.add_column(justify="left", width=20)

            seed_style: Literal['bold red'] | Literal['white'] = (
                "bold red"
                if maze.seed is None or maze.seed == "None"
                else "white"
            )
            status_table.add_row(
                Text("DIMENSIONS   :", style=color_text_top),
                Text(f" {maze.width} x {maze.height}", style="white"),
                "",
                Text("SEED         :", style=color_text_top),
                Text(f" {maze.seed}", style=seed_style)

            )
            perfect_style: Literal['bold green'] | Literal['bold red'] = (
                "bold green"
                if maze.perfect is not False
                else "bold red"
            )
            status_table.add_row(
                Text("ENTRY(X, Y)  :", style=color_text_top),
                Text(f" {maze.entry}", style="white"),
                "",
                Text("PERFECT      :", style=color_text_top),
                Text(f" {maze.perfect}", style=perfect_style)
            )

            status_table.add_row(
                Text("EXIT(X, Y)   :", style=color_text_top),
                Text(f" {maze.exit}", style="white"),
                "",
                Text("FILE         :", style=color_text_top),
                Text(f" {maze.file}", style="bold magenta")
            )

            status_table.add_row(
                Text("ALGORITHM    :", style=color_text_top),
                Text(f" {algo_name}", style="white"),
                "",
                Text("WALL TYPE    :", style=color_text_top),
                Text(f" {wall_name}", style="white")
            )
            if maze.generate_logo() is False:
                logo_message = Align.center(
                    Text(
                        "LOGO GENERATION ABORTED: SIZE TOO SMALL",
                        style="bold red"))
            else:
                logo_message = Align.center(
                    Text(
                        "SYSTEM STATUS: CONFIGURATION OPTIMAL",
                        style="bold green"))

            panel_content: Any = Group(
                status_table,
                "",
                logo_message
            )

            panel_top: Any = Panel(
                panel_content,
                title="[bold white] [ SYSTEM CONFIGURATION ] [/]",
                border_style=color_frame,
                width=94,
                height=10,
                padding=(1, 5)
            )

            wall_map: list = [Wall, WallDouble, WallSkinny,
                              WallRetro, WallUgly, WallBig]
            color_map: list = [Color.NEON_RED.value, Color.NEON_GREEN.value,
                               Color.NEON_YELLOW.value, Color.NEON_BLUE.value,
                               Color.NEON_MAGENTA.value, Color.NEON_CYAN.value,
                               Color.WHITE.value, Color.NEON_ORANGE.value,
                               Color.NEON_PINK.value]

            config_checked_states: dict[int, Any] = {
                0: is_perfect,
                1: show_advanced
            }

            style_p = (
                color_select_frame
                if current_menu == "MAIN"
                else color_frame)
            panel_main: Any = Panel(
                get_menu_content(
                    main_opts,
                    index,
                    current_menu == "MAIN",
                    "MAIN"),
                title="[bold cyan] MENU [/]",
                border_style=style_p,
                width=30,
                height=9,
                padding=(
                    0,
                    2))

            style_pa = (
                color_select_frame
                if current_menu == "ALGO"
                else color_frame)
            panel_algo: Any = Panel(
                get_menu_content(
                    list_algo,
                    index,
                    current_menu == "ALGO",
                    "ALGO",
                    selected_val=algo_name),
                title="[bold cyan] ALGORITHM [/]",
                border_style=style_pa,
                width=30,
                height=9,
                padding=(
                    0,
                    2))

            style_c = (
                color_select_frame
                if current_menu == "CONFIG"
                else color_frame)
            panel_config: Any = Panel(
                get_menu_content(
                    config_opts,
                    index,
                    current_menu == "CONFIG",
                    "CONFIG",
                    checked_dict=config_checked_states),
                title="[bold cyan] CONFIGURATION [/]",
                border_style=style_c,
                width=30,
                height=9,
                padding=(
                    0,
                    2))

            style_s = (
                "cyan" if current_menu == "WALLS" else color_frame)
            panel_styles: Any = Panel(
                get_menu_content(
                    style_opts,
                    index,
                    current_menu == "WALLS",
                    "WALLS",
                    selected_val=wall_name),
                title="[bold cyan] WALL STYLES [/]",
                border_style=style_s,
                width=19,
                height=11)

            panel_logos: Any = Panel(
                get_menu_content(
                    logos_list,
                    index,
                    current_menu == "LOGO",
                    "LOGO",
                    selected_val=logo_name),
                title="[bold cyan] LOGOS [/]",
                border_style="cyan" if current_menu == "LOGO" else color_frame,
                width=17,
                height=11)

            style_co = (
                "cyan" if current_menu == "COLOR_W" else color_frame)
            panel_colorw: Any = Panel(
                get_menu_content(
                    colors_list,
                    index,
                    current_menu == "COLOR_W",
                    "COLOR_W",
                    selected_val=color_wall),
                title="[bold cyan] COLOR WALL [/]",
                border_style=style_co,
                width=18,
                height=11)

            style_col = (
                "cyan" if current_menu == "COLOR_L" else color_frame)
            panel_colorl: Any = Panel(
                get_menu_content(
                    colors_list,
                    index,
                    current_menu == "COLOR_L",
                    "COLOR_L",
                    selected_val=color_case_logo),
                title="[bold cyan] COLOR LOGO [/]",
                border_style=style_col,
                width=18,
                height=11)

            style_cop = (
                "cyan" if current_menu == "COLOR_P"
                else color_frame)
            panel_colorp: Any = Panel(
                get_menu_content(
                    colors_list,
                    index,
                    current_menu == "COLOR_P",
                    "COLOR_P",
                    selected_val=color_path),
                title="[bold cyan] COLOR PATH [/]",
                border_style=style_cop,
                width=18,
                height=11)
            row_1: Any = Columns(
                [panel_main, panel_algo, panel_config], padding=(0, 2))
            row_2: Any = Columns([panel_colorw, panel_colorl,
                                  panel_colorp, panel_logos,
                                  panel_styles], padding=(0, 1))

            if show_advanced:
                live.update(Group(panel_top, row_1, row_2))
            else:
                live.update(Group(panel_top, row_1))

            menus_map: dict[str, list[str]] = {
                "MAIN": main_opts,
                "ALGO": list_algo,
                "CONFIG": config_opts,
                "WALLS": style_opts,
                "LOGO": logos_list,
                "COLOR_W": colors_list,
                "COLOR_L": colors_list,
                "COLOR_P": colors_list
            }

            active_options: list[str] = menus_map.get(current_menu, main_opts)

            key: Any = readchar.readkey()

            if key == readchar.key.UP:
                index = (index - 1) % len(active_options)
            elif key == readchar.key.DOWN:
                index = (index + 1) % len(active_options)
            elif key == readchar.key.TAB:
                if current_menu == "MAIN":
                    current_menu = "ALGO"
                elif current_menu == "ALGO":
                    current_menu = "CONFIG"
                elif current_menu == "CONFIG":
                    current_menu = (
                        "COLOR_W" if show_advanced else "MAIN")
                elif current_menu == "COLOR_W":
                    current_menu = "COLOR_L"
                elif current_menu == "COLOR_L":
                    current_menu = "COLOR_P"
                elif current_menu == "COLOR_P":
                    current_menu = "LOGO"
                elif current_menu == "LOGO":
                    current_menu = "WALLS"
                else:
                    current_menu = "MAIN"
                index = 0
            elif key == ' ':
                if current_menu == "CONFIG":
                    if index == 0:
                        is_perfect = not is_perfect
                        maze.perfect = is_perfect
                    elif index == 1:
                        show_advanced = not show_advanced
                    elif index == 2:
                        # --- MODIFICATION DE L'ENTRÉE ---
                        live.stop()  # On met l'affichage du menu en pause
                        print("\n" * 2)  # On dégage un peu d'espace dans le terminal
                        try:
                            print(f"[CONFIGURATION DE L'ENTRÉE]")
                            new_x = int(input(f"Nouveau X (0 à {maze.width - 1}) : "))
                            new_y = int(input(f"Nouveau Y (0 à {maze.height - 1}) : "))

                            # On vérifie que les coordonnées ne sortent pas du labyrinthe
                            if 0 <= new_x < maze.width and 0 <= new_y < maze.height:
                                maze.entry = (new_x, new_y)
                            else:
                                print("Coordonnées hors limites ! Appuyez sur Entrée pour revenir au menu...")
                                input()
                        except ValueError:
                            print("Saisie invalide (nombres entiers attendus). Appuyez sur Entrée pour revenir au menu...")
                            input()

                        clear() # On nettoie l'écran avant de relancer
                        print("\033[H", end="")
                        live.start() # On relance l'affichage du menu

                elif current_menu == "WALLS":
                    wall_name = style_opts[index]
                    Theme.wall = wall_map[index % len(wall_map)]
                elif current_menu == "ALGO":
                    algo_name = list_algo[index]
                elif current_menu == "LOGO":
                    logo_name = logos_list[index]
                    if logo_name == "TIMER":
                        Theme.logo_midile = "00"
                        Theme.logo_chrono = True
                    else:
                        Theme.logo_midile = logo_name
                        Theme.logo_chrono = False
                elif current_menu == "COLOR_W":
                    color_wall = colors_list[index % len(color_map)]
                    Theme.color_wall = color_map[index % len(color_map)]
                elif current_menu == "COLOR_L":
                    color_case_logo = colors_list[index % len(color_map)]
                    Theme.color_case_logo = color_map[index % len(color_map)]
                elif current_menu == "COLOR_P":
                    color_path = colors_list[index % len(color_map)]
                    Theme.color_path = color_map[index % len(color_map)]
            elif key == readchar.key.ENTER:
                if current_menu == "MAIN":
                    if index == 0:
                        current_menu = "GENERATE"
                        live.stop()
                        maze.generate_grid()
                        maze.generate_logo()
                        maze.generate_maze(algo_name)
                        clear()
                        print("\033[H", end="")
                        maze.draw_maze(False)
                        if show_advanced:
                            print("\n" * 29)
                        else:
                            print("\n" * 18)
                        live.start()
                    elif index == 1:
                        current_menu = "SOLVE PATH"
                        live.stop()
                        maze.generate_path()
                        clear()
                        print("\033[H", end="")
                        maze.draw_path()
                        maze.draw_maze(False)
                        if show_advanced:
                            print("\n" * 29)
                        else:
                            print("\n" * 18)
                        live.start()
                    elif index == 2:
                        current_menu = "UPDATE"
                        live.stop()
                        clear()
                        print("\033[H", end="")
                        maze.draw_maze(False)
                        if show_advanced:
                            print("\n" * 29)
                        else:
                            print("\n" * 18)
                        live.start()
                    elif index == 3:
                        current_menu = "RESET"
                        live.stop()
                        clear()
                        print("\033[H", end="")
                        clear()
                        maze.generate_grid()
                        maze.generate_logo()
                        maze.draw_maze(True)
                        if show_advanced:
                            print("\n" * 29)
                        else:
                            print("\n" * 18)
                        live.start()
                    elif index == 4:
                        current_menu = "PAKAGE"
                        pass
                    elif index == 5:
                        current_menu = "PLAY GAME"
                        live.stop()
                        maze.play_game()
                        if show_advanced:
                            print("\n" * 29)
                        else:
                            print("\n" * 18)
                        live.start()
                    elif index == 6:
                        current_menu = "EXIT"
                        sys.exit()
                elif current_menu == "CONFIG":
                    if index == 0:
                        is_perfect = not is_perfect
                        maze.perfect = is_perfect
                    elif index == 1:
                        show_advanced = not show_advanced
                    elif index == 2:
                        live.stop()
                        clear()
                        edit_door(maze, "entry")
                        clear()
                        print("\033[H", end="")
                        maze.draw_maze(False)
                        print("\n" * (29 if show_advanced else 18))
                        live.start()
                    elif index == 3:
                        live.stop()
                        clear()
                        edit_door(maze, "exit")
                        clear()
                        print("\033[H", end="")
                        maze.draw_maze(False)
                        print("\n" * (29 if show_advanced else 18))
                        live.start()
                elif current_menu == "ALGO":
                    algo_name = list_algo[index]
                    current_menu = "MAIN"
                    index = 0
                elif current_menu == "WALLS":
                    wall_name = style_opts[index]
                    Theme.wall = wall_map[index % len(wall_map)]
                    current_menu = "MAIN"
                    index = 0
                elif current_menu == "LOGO":
                    logo_name = logos_list[index]
                    if logo_name == "TIMER":
                        Theme.logo_midile = "00"
                        Theme.logo_chrono = True
                        maze.generate_logo()
                    else:
                        Theme.logo_midile = logo_name
                        Theme.logo_chrono = False
                        maze.generate_logo()
                    current_menu = "MAIN"
                    index = 0
                elif current_menu == "COLOR_W":
                    color_wall = colors_list[index]
                    Theme.color_wall = color_map[index % len(color_map)]
                    current_menu = "MAIN"
                    index = 0
                elif current_menu == "COLOR_L":
                    color_case_logo = colors_list[index]
                    Theme.color_case_logo = color_map[index % len(color_map)]
                    print("\033[H", end="")
                    maze.generate_logo()
                    current_menu = "MAIN"
                    index = 0
                elif current_menu == "COLOR_P":
                    color_path = colors_list[index]
                    Theme.color_path = color_map[index % len(color_map)]
                    current_menu = "MAIN"
                    index = 0
