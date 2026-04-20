from enum import Enum
import random


class WallRetro(Enum):
    horizontal = '---'
    vertical = '|'
    corner = '+'
    box = '   '
    corner_tl = "+"
    corner_tr = "+"
    corner_bl = "+"
    corner_br = "+"
    corner_tt = "+"
    corner_bt = "+"
    corner_lt = "+"
    corner_rt = "+"
    corner_x = "+"
    cursor = '###'


class WallSkinny(Enum):
    horizontal = '───'
    vertical = '│'
    corner = '┼'
    box = '   '
    corner_tl = "┌"
    corner_tr = "┐"
    corner_bl = "└"
    corner_br = "┘"
    corner_tt = "┬"
    corner_bt = "┴"
    corner_lt = "├"
    corner_rt = "┤"
    corner_x = "┼"
    cursor = '███'


class WallBigBig(Enum):
    horizontal = '███'
    vertical = '█'
    corner = '█'
    box = '   '
    corner_tl = "█"
    corner_tr = "█"
    corner_bl = "█"
    corner_br = "█"
    corner_tt = "█"
    corner_bt = "█"
    corner_lt = "█"
    corner_rt = "█"
    corner_x = "█"
    cursor = '███'


class Wall(Enum):
    horizontal = '━━━'
    vertical = '┃'
    corner = '╋'
    box = '   '
    corner_tl = "┏"
    corner_tr = "┓"
    corner_bl = "┗"
    corner_br = "┛"
    corner_tt = "┳"
    corner_bt = "┻"
    corner_lt = "┣"
    corner_rt = "┫"
    corner_x = "╋"
    cursor = '███'


class WallUgly(Enum):
    horizontal = '···'
    vertical = '┆'
    corner = '+'
    box = '   '
    corner_tl = "+"
    corner_tr = "+"
    corner_bl = "+"
    corner_br = "+"
    corner_tt = "+"
    corner_bt = "+"
    corner_lt = "+"
    corner_rt = "+"
    corner_x = "+"
    cursor = '@@@'


class WallDouble(Enum):
    horizontal = '═══'
    vertical = '║'
    corner = '╬'
    box = '   '
    corner_tl = "╔"
    corner_tr = "╗"
    corner_bl = "╚"
    corner_br = "╝"
    corner_tt = "╦"
    corner_bt = "╩"
    corner_lt = "╠"
    corner_rt = "╣"
    corner_x = "╬"
    cursor = '▓▓▓'


class Color(Enum):
    RESET = "\033[0m"
    DEFAULT = "\033[0m"

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

    DARK_RED = "\033[31m"
    DARK_GREEN = "\033[32m"
    DARK_BLUE = "\033[34m"
    DARK_MAGENTA = "\033[35m"
    GRAY = "\033[90m"

    GOLD = "\033[38;5;214m"
    ORANGE = "\033[38;5;208m"
    PINK = "\033[38;5;206m"
    PURPLE = "\033[38;5;129m"
    SKY_BLUE = "\033[38;5;117m"

    NEON_RED = "\033[38;5;196m"
    NEON_GREEN = "\033[38;5;46m"
    NEON_YELLOW = "\033[38;5;226m"
    NEON_BLUE = "\033[38;5;39m"
    NEON_CYAN = "\033[38;5;51m"
    NEON_MAGENTA = "\033[38;5;201m"
    NEON_ORANGE = "\033[38;5;208m"
    NEON_PURPLE = "\033[38;5;93m"
    NEON_PINK = "\033[38;5;198m"
    SPRING_GREEN = "\033[38;5;48m"

    @classmethod
    def random_color(cls) -> str:
        valid_colors = [
            c.value for c in cls if c not in (
                cls.RESET, cls.DEFAULT)]
        return random.choice(valid_colors)


class Logo(Enum):
    logo_42 = "logo_42"
    caca = "caca"
    logo_surprise = "logo_surprise"


class Theme:
    color_select = Color.MAGENTA.value
    color_case = Color.DEFAULT.value
    # color_case_logo = Color.DARK_MAGENTA.value

    color_wall = Color.WHITE.value
    wall = Wall

    color_case_logo = Color.DARK_RED.value

    delais_draw: float = 0.01
    animation_draw: bool = True
    color_animation_backtraking = None

    animation_draw_path:bool = True
    color_path = Color.BLUE.value

    entry_color_case = Color.WHITE.value
    exit_color_case = Color.RED.value
    logo_midile = "00"
    # logo_midile = "69"
    logo_chrono: bool = True
