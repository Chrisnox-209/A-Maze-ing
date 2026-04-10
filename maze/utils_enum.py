from enum import Enum


class WallRetro(Enum):
    horizontal = '---'
    vertical = '|'
    corner = '+'
    box = '   '
    corners_tl = "+"
    corners_tr = "+"
    corners_bl = "+"
    corners_br = "+"
    corners_tt = "+"
    corners_bt = "+"
    corners_lt = "+"
    corners_rt = "+"
    corners_x = "+"
    cursor = '###'


class Wall(Enum):
    horizontal = '───'
    vertical = '│'
    corner = '┼'
    box = '   '
    corners_tl = "┌"
    corners_tr = "┐"
    corners_bl = "└"
    corners_br = "┘"
    corners_tt = "┬"
    corners_bt = "┴"
    corners_lt = "├"
    corners_rt = "┤"
    corners_x = "┼"
    cursor = '███'


class WallUgly(Enum):
    horizontal = '···'
    vertical = '┆'
    corner = '+'
    box = '   '
    corners_tl = "+"
    corners_tr = "+"
    corners_bl = "+"
    corners_br = "+"
    corners_tt = "+"
    corners_bt = "+"
    corners_lt = "+"
    corners_rt = "+"
    corners_x = "+"
    cursor = '@@@'


class WallDouble(Enum):
    horizontal = '═══'
    vertical = '║'
    corner = '╬'
    box = '   '
    corners_tl = "╔"
    corners_tr = "╗"
    corners_bl = "╚"
    corners_br = "╝"
    corners_tt = "╦"
    corners_bt = "╩"
    corners_lt = "╠"
    corners_rt = "╣"
    corners_x = "╬"
    cursor = '▓▓▓'


class Color(Enum):
    DEFAULT = "\033[0m"
    BLEU  = "\033[94m"
    ROUGE = "\033[91m"
    VERT  = "\033[92m"
    JAUNE = "\033[93m"
    CYAN  = "\033[96m"
    BLANC = "\033[97m"
    OR    = "\033[38;5;214m"
