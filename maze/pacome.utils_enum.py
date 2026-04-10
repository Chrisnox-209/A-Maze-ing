from enum import Enum


class WallDouble(Enum):
    H_LINE = "═══"
    H_PATH = "   "
    V_LINE = "║   "
    V_PATH = "    "
    V_RIGHT = "║"
    CROSS = "╬"
    TOP_LEFT = "╔"
    TOP_RIGHT = "╗"
    BOT_LEFT = "╚"
    BOT_RIGHT = "╝"
    T_TOP = "╦"
    T_BOT = "╩"
    T_LEFT = "╠"
    T_RIGHT = "╣"


# class Wall(Enum):
#     H_LINE = "━━━"
#     H_PATH = "   "
#     V_LINE = "┃   "
#     V_PATH = "    "
#     V_RIGHT = "┃"
#     CROSS = "╋"
#     TOP_LEFT = "┏"
#     TOP_RIGHT = "┓"
#     BOT_LEFT = "┗"
#     BOT_RIGHT = "┛"
#     T_TOP = "┳"
#     T_BOT = "┻"
#     T_LEFT = "┣"
#     T_RIGHT = "┃"


class Wall(Enum):
    H_LINE = "━━━"
    H_PATH = "   "
    V_LINE = "┃   "
    V_PATH = "    "
    V_RIGHT = "┃"
    CROSS = "╋"
    TOP_LEFT = "┏"
    TOP_RIGHT = "┓"
    BOT_LEFT = "┗"
    BOT_RIGHT = "┛"
    T_TOP = "┳"
    T_BOT = "┻"
    T_LEFT = "┃"
    T_RIGHT = "┃"
    MIDDLE = "██"


class WallSkinny(Enum):
    H_LINE = "───"
    H_PATH = "   "
    V_LINE = "│   "
    V_PATH = "    "
    V_RIGHT = "│"
    CROSS = "┼"
    TOP_LEFT = "╭"
    TOP_RIGHT = "╮"
    BOT_LEFT = "╰"
    BOT_RIGHT = "╯"
    T_TOP = "┬"
    T_BOT = "┴"
    T_LEFT = "├"
    T_RIGHT = "┤"


class WallRetro(Enum):
    H_LINE = "---"
    H_PATH = "   "
    V_LINE = "|   "
    V_PATH = "    "
    V_RIGHT = "|"
    CROSS = "+"
    TOP_LEFT = "+"
    TOP_RIGHT = "+"
    BOT_LEFT = "+"
    BOT_RIGHT = "+"
    T_TOP = "+"
    T_BOT = "+"
    T_LEFT = "+"
    T_RIGHT = "+"


class WallUgly(Enum):
    H_LINE = "···"
    H_PATH = "   "
    V_LINE = "∶   "
    V_PATH = "    "
    V_RIGHT = "∶"
    CROSS = "⊹"
    TOP_LEFT = "┌"
    TOP_RIGHT = "┐"
    BOT_LEFT = "└"
    BOT_RIGHT = "┘"
    T_TOP = "┮"
    T_BOT = "┶"
    T_LEFT = "┟"
    T_RIGHT = "┧"


class Color(Enum):
    RESET = '\033[0m'
    DEFAULT = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    BG_YELLOW = '\033[43m'

