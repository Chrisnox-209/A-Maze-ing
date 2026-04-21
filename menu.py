import sys
import readchar
from rich.console import Console, Group
from rich.panel import Panel
from utils.parser import clear
from rich.text import Text
from rich.table import Table
from rich.live import Live
from rich.columns import Columns
from maze.utils_enum import WallDouble, Wall, WallSkinny, WallRetro, WallUgly, Theme
from typing import Literal, Any


def get_menu_content(options, current_index, is_active, menu_type, selected_val=None) -> Group:
    render_opts: list = []

    for i, opt in enumerate(options):
        # --- 1. Déterminer le préfixe ---
        if menu_type == "MAIN":
            prefix_text = "▶ " if (is_active and i == current_index) else "  "
        elif menu_type == "WALLS":
            # Le symbole dépend de la sélection enregistrée, pas du curseur
            prefix_text = "█ " if opt == selected_val else "░ "
        else:
            # Menu ALGO
            mark = "X" if opt == selected_val else " "
            prefix_text = f"[{mark}] "
            
        # --- 2. Construction du texte ---
        if is_active and i == current_index:
            # Option survolée (curseur jaune)
            prefix = Text(prefix_text, style="bold yellow")
            content = Text(f" {opt} ", style="black on yellow")
            render_opts.append(Text.assemble(prefix, content))
        else:
            # Option non survolée
            if menu_type in ["WALLS", "ALGO", "LOGO"] and opt == selected_val:
                style = "bold green"  # L'élément validé ressort en vert
            else:
                # On utilise 'dim cyan' pour assombrir les options non sélectionnées 
                # dans WALLS et ALGO, ce qui fait ressortir le reste.
                style = "dim cyan" if menu_type != "MAIN" else "cyan"
                
            render_opts.append(Text(f"{prefix_text}{opt}", style=style))
            
    return Group(*render_opts)

def Menu(maze) -> None:
    console = Console()
    main_opts: list[str] = ["GENERATE", "SOLVE PATH", "UPDATE", "RESET", "PAKAGE", "EXIT"]
    style_opts: list[str] = ["CLASSIC WALL", "DOUBLE WALL",
                             "SKINNY WALL", "RETRO WALL", "UGLY WALL"]
    list_algo: list[str] = ["DFS", "KRUSKAL", "PRIMS"]
    colors_list: list[str] = ["RED", "GREEN", "YELLOW", "BLUE",
                              "MAGENTA", "CYAN", "WHITE",
                              "ORANGE", "PINK"]
    logos_list: list[str] = ["LOGO 42", "TIMER", "POOH", "SURPRISE"]
    wall_name: str = style_opts[0]
    algo_name: str = list_algo[0]
    logo_name: str = logos_list[0]
    color_wall: str = colors_list[6]
    color_logo: str = colors_list[0]
    color_path: str = colors_list[1]

    current_menu = "MAIN"
    index = 0

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
                if maze.seed is None or maze.seed == "None"
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

            panel_top = Panel(
                status_table,
                title="[bold white] [ SYSTEM CONFIGURATION ] [/]",
                border_style=color_frame,
                width=81,
                height=10,
                padding=(1, 5)
            )

            wall_map: list = [Wall, WallDouble, WallSkinny, WallRetro, WallUgly]
            # --- PANELS DES MENUS ---
            panel_main = Panel(
                get_menu_content(main_opts, index, current_menu == "MAIN", "MAIN"),
                title="[bold cyan] COMMANDS [/]",
                border_style=color_select_frame if current_menu == "MAIN" else color_frame,
                width=22, height=10
            )

            panel_algo = Panel(
                get_menu_content(list_algo, index, current_menu == "ALGO", "ALGO", selected_val=algo_name),
                title="[bold cyan] ALGORITHM [/]",
                border_style=color_select_frame if current_menu == "ALGO" else color_frame,
                width=22, height=10
            )

            panel_styles = Panel(
                get_menu_content(style_opts, index, current_menu == "WALLS", "WALLS", selected_val=wall_name),
                title="[bold cyan] WALL STYLES [/]",
                border_style="cyan" if current_menu == "WALLS" else color_frame,
                width=22, height=10
            )
            
            panel_logos = Panel(
                get_menu_content(logos_list, index, current_menu == "LOGO", "LOGO", selected_val=logo_name),
                title="[bold cyan] WALL STYLES [/]",
                border_style="cyan" if current_menu == "LOGO" else color_frame,
                width=22, height=10
            )
            
            live.update(Group(panel_top, Columns([panel_main, panel_algo, panel_styles, panel_logos])))

            # --- INPUTS ---
            active_options: list[str] = main_opts if current_menu == "MAIN" else style_opts
            key: Any = readchar.readkey()

            if key == readchar.key.UP:
                index: int = (index - 1) % len(active_options)
            elif key == readchar.key.DOWN:
                index = (index + 1) % len(active_options)
            elif key == readchar.key.TAB:
                if current_menu == "MAIN":
                    current_menu = "ALGO"
                elif current_menu == "ALGO":
                    current_menu = "WALLS"
                elif current_menu == "WALLS":
                    current_menu = "LOGO"
                else:
                    current_menu = "MAIN"
                index = 0
            elif key == ' ':
                if current_menu == "WALLS":
                    wall_name = style_opts[index]
                    Theme.wall = wall_map[index % len(wall_map)]
                elif current_menu == "ALGO":
                    algo_name = list_algo[index]
                elif current_menu == "LOGO":
                    logo_name = logos_list[index]
            elif key == readchar.key.ENTER:
                if current_menu == "MAIN":
                    if index == 0:
                        current_menu == "GENERATE"
                        live.stop()
                        maze.generate_grid()
                        maze.generate_logo()
                        maze.generate_maze(algo_name)
                        clear()
                        print("\033[H", end="")
                        maze.draw_maze()
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        live.start()
                    elif index == 1:
                        current_menu == "SOLVE PATH"
                        pass
                    elif index == 2:
                        current_menu == "UPDATE"
                        live.stop()
                        clear()
                        print("\033[H", end="")
                        maze.draw_maze()
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        live.start()                       
                    elif index == 3:
                        current_menu == "RESET"
                        live.stop()
                        clear()
                        print("\033[H", end="")
                        maze.generate_grid()
                        maze.generate_logo()
                        maze.draw_maze()
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        live.start()
                    elif index == 4:
                        current_menu == "PAKAGE"
                        pass
                    elif index == 5:
                        current_menu = "EXIT"
                        sys.exit()
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
                    current_menu = "MAIN"
                    index = 0