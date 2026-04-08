import sys
import readchar
from rich.console import Console, Group
from rich.panel import Panel
from utils.parser import clear
from rich.align import Align
from art import text2art
from rich.text import Text
from rich import box
from rich.live import Live
from maze.maze import Maze
from maze.utils_enum import WallDouble, Wall, WallSkinny, WallRetro, WallUgly
import random


def Menu(maze: Maze) -> None:
    console = Console()
    amaze = text2art("A-Maze-ing")
    title_centered = Align.center(f"[bold bright_magenta]{amaze}[/]")

    main_options = [
        "01. REGENERATE",
        "02. SOLVE PATH",
        "03. CHANGE WALL",
        "04. EXIT SYSTEM"]
    style_options = [
        "Wall Clasique",
        "Wall Double",
        "Wall Skinny",
        "Wall Retro",
        "Wall Ugly",
        "Random",
        "BACK TO MENU"]

    current_menu = "MAIN"
    options = main_options
    index = 0
    wall_select = Wall
    list_style: list[str] = [Wall,
                             WallDouble,
                             WallSkinny,
                             WallRetro,
                             WallUgly]

    with Live(console=console, screen=False, auto_refresh=True) as live:
        while True:
            render_opts = []
            for i, opt in enumerate(options):
                if i == index:
                    render_opts.append(
                        Text(
                            f" ▶ 「 {opt} 」",
                            style="black on bright_magenta"))
                else:
                    is_last = (i == len(options) - 1)
                    style = "bold bright_red" if (
                        current_menu == "MAIN" and is_last) or (
                        current_menu == "COLORS" and is_last) else "white"
                    render_opts.append(Text(f"   「 {opt} 」", style=style))

            menu_content = Group(title_centered, *render_opts)
            live.update(
                Panel(
                    menu_content,
                    title=current_menu,
                    width=90,
                    box=box.DOUBLE_EDGE,
                    border_style="cyan",
                    padding=(
                        1,
                        2)))

            key = readchar.readkey()
            if key == readchar.key.UP:
                index = (index - 1) % len(options)
            elif key in (readchar.key.DOWN, readchar.key.TAB):
                index = (index + 1) % len(options)
            elif key == readchar.key.ENTER:
                if current_menu == "MAIN":
                    if index == 0:
                        live.stop()
                        clear()
                        maze.draw_maze(wall_select)
                        console.print(
                            "\n[dim]Appuie sur une touche pour revenir au menu...[/]")
                        readchar.readkey()
                        clear()
                        live.start()
                    elif index == 2:
                        current_menu = "COLORS"
                        options = style_options
                        index = 0
                    elif index == len(main_options) - 1:
                        sys.exit()
                elif current_menu == "COLORS":
                    if index == 0:
                        current_menu = "MAIN"
                        options = main_options
                        wall_select = Wall
                        index = 0
                    if index == 1:
                        current_menu = "MAIN"
                        options = main_options
                        wall_select = WallDouble
                        index = 0
                    if index == 2:
                        current_menu = "MAIN"
                        options = main_options
                        wall_select = WallSkinny
                        index = 0
                    if index == 3:
                        current_menu = "MAIN"
                        options = main_options
                        wall_select = WallRetro
                        index = 0
                    if index == 4:
                        current_menu = "MAIN"
                        options = main_options
                        wall_select = WallUgly
                        index = 0
                    if index == 5:
                        current_menu = "MAIN"
                        options = main_options
                        wall_select = "random"
                        index = 0
                    if index == len(style_options) - 1:
                        current_menu = "MAIN"
                        options = main_options
                        index = 2
