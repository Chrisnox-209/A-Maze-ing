from enum import Enum

class Draw(Enum):
    TOP_WALL = "█▀▀"
    TOP_PATH = "█  "
    MID_WALL = "█  "
    MID_PATH = "   "
    V_LINE = "█"
    CORNER = "█"
    BOTTOM = "▀▀"
    CORNER_BOT = "▀"


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