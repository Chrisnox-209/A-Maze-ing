from enum import Enum
import random


class WallRetro(Enum):
    """Enumération définissant l'apparence des murs de style rétro.
    """
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


class WallRounded(Enum):
    """Enumération pour les murs avec des coins arrondis.
    """
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


class WallSkinny(Enum):
    """Enumération pour les murs fins (skinny).
    """
    horizontal = '───'
    vertical = '│'
    corner = '┼'
    box = '   '
    corner_tl = "╭"
    corner_tr = "╮"
    corner_bl = "╰"
    corner_br = "╯"
    corner_tt = "┬"
    corner_bt = "┴"
    corner_lt = "├"
    corner_rt = "┤"
    corner_x = "┼"
    cursor = '███'


class WallBig(Enum):
    """Enumération pour les murs épais (big).
    """
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
    """Enumération standard des murs du labyrinthe.
    """
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
    """Enumération proposant un style de mur délibérément basique.
    """
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
    """Enumération pour les murs représentés par des lignes doubles.
    """
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
    """Enumération des couleurs disponibles pour l'interface.
    Permet de styliser le texte et les murs dans le terminal.
    """
    RESET = "\033[0m"
    DEFAULT = "\033[0m"

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

    ENTRY = "\033[38;5;246m"
    EXIT = "\033[38;5;202m"

    DARK_RED = "\033[31m"
    DARK_GREEN = "\033[32m"
    DARK_BLUE = "\033[34m"
    DARK_MAGENTA = "\033[35m"

    GOLD = "\033[38;5;214m"
    ORANGE = "\033[38;5;208m"
    PINK = "\033[38;5;206m"
    PURPLE = "\033[38;5;129m"
    SKY_BLUE = "\033[38;5;117m"
    LIME = "\033[38;5;118m"

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
        """Retourne une couleur aléatoire parmi celles disponibles.
        Utilisé pour l'animation ou des effets visuels dynamiques.
        """
        valid_colors = [
            c.value for c in cls if c not in (
                cls.RESET, cls.DEFAULT)]
        return random.choice(valid_colors)


class Logo(Enum):
    """Enumération des identifiants ou types de logos disponibles.
    Gère les différentes formes qui peuvent être affichées (42, Timer, etc.).
    Facilite la sélection du motif central.
    """
    logo_42 = "LOGO_42"
    caca = "POOH"
    logo_surprise = "SURPRISE"


class Theme:
    """Classe regroupant la configuration visuelle globale.
    Stocke les couleurs, le style de mur, et l'état des animations.
    Sert de variable globale pour le rendu interactif.
    """
    color_select = Color.MAGENTA.value
    color_case = Color.DEFAULT.value
    color_case_logo = Color.NEON_RED.value
    color_wall = Color.WHITE.value
    wall = Wall

    delais_draw: float = 0.01
    animation_draw: bool = False
    color_animation_backtraking = Color.BLUE.value

    animation_algo: bool = False
    animation_draw_path: bool = False
    color_path = Color.BLUE.value

    entry_color_case = Color.ENTRY.value
    exit_color_case = Color.EXIT.value
    logo_midile: str = "LOGO_42"
    logo_chrono: bool = False
    default = "\033[0m"
