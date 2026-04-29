import sys
import random
import time
from typing import Any, Literal, Optional, Self
try:
    from ..algos import (
        find_path_bfs,
        dfs,
        kruskal,
        imperfect_maze_func,
    )
    from ..maze import (
        Logo,
        output_maze_func,
        Color,
        Theme,
    )
    from ..options import Timer
    from pydantic import BaseModel, Field, ValidationError, model_validator

except ImportError as e:
    raise SystemExit(f"Import error: {e}")
    sys.exit(1)


class Cell:
    """Représente une cellule individuelle dans la grille du labyrinthe.
    Stocke l'état de ses murs, ses couleurs et ses flags de visite.
    Gère aussi son appartenance potentielle à un chemin ou un logo.
    """
    def __init__(self, x: int, y: int, cell_id: int) -> None:
        """Initialise l'instance avec ses attributs par défaut.
        Met en place l'état initial requis pour le fonctionnement.
        Configure les variables internes de l'objet.
        """
        self.x: int = int(x)
        self.y: int = int(y)
        self.cell_id = int(cell_id)
        self.color_case: str = Theme.color_case
        self.visit = False
        self.path_id = -1
        self.path_active = False
        self.path_content = "   "
        self.walls: dict = {
            "North": True,
            "East": True,
            "South": True,
            "West": True
        }

    def __repr__(self) -> str:
        """Fournit une représentation textuelle de la cellule pour le débogage.
        Affiche l'identifiant de la cellule de manière claire.
        Facilite le traçage lors de l'exécution.
        """
        return f"{self.x}:{self.y}, id={self.cell_id}"


class MazeConfig(BaseModel):
    """Modèle de validation pour la configuration du labyrinthe.
    Vérifie les types et les valeurs (hauteur, largeur, seed, etc.).
    Utilise Pydantic pour s'assurer que les données sont conformes.
    """
    WIDTH: int = Field(ge=3)
    HEIGHT: int = Field(ge=3)
    ENTRY_X: int = Field(ge=0)
    ENTRY_Y: int = Field(ge=0)
    EXIT_X: int = Field(ge=0)
    EXIT_Y: int = Field(ge=0)
    OUTPUT_FILE: str = Field(default="exit.txt", max_length=20)
    PERFECT: bool = Field(default=True)
    SEED: Optional[str] = Field(default=None, min_length=1)

    @model_validator(mode='after')
    def check_entry(self) -> Self:
        """Vérifie la validité des coordonnées d'entrée du labyrinthe.
        Lève une erreur si l'entrée est en dehors des limites.
        S'assure que l'entrée est bien sur un bord du labyrinthe.
        """
        if (self.ENTRY_X >= self.WIDTH):
            raise ValueError("ENTRY X is outside the maze.")
        if (self.ENTRY_Y >= self.HEIGHT):
            raise ValueError("ENTRY Y is outside the maze.")
        return self

    @model_validator(mode='after')
    def check_file(self) -> Self:
        """Vérifie la validité des coordonnées d'entrée du labyrinthe.
        Lève une erreur si l'entrée est en dehors des limites.
        S'assure que l'entrée est bien sur un bord du labyrinthe.
        """
        if not self.OUTPUT_FILE.endswith(".txt"):
            raise ValueError("OUTPUT FILE The extension is not valid.")
        return self

    @model_validator(mode='after')
    def check_exit(self) -> Self:
        """Vérifie la validité des coordonnées de sortie du labyrinthe.
        Lève une erreur si la sortie est hors limites ou identique à l'entrée.
        S'assure que la sortie se trouve bien sur un bord externe.
        """
        if (self.EXIT_X >= self.WIDTH):
            raise ValueError("EXIT X is outside the maze.")
        if (self.EXIT_Y >= self.HEIGHT):
            raise ValueError("EXIT Y is outside the maze.")
        return self

    @model_validator(mode='after')
    def check_door(self) -> Self:
        """Applique les vérifications complètes sur l'entrée et la sortie.
        S'assure que ces deux portes respectent les dimensions de la grille.
        Valide la cohérence globale des accès au labyrinthe.
        """
        if (self.ENTRY_Y == self.EXIT_Y and self.ENTRY_X == self.EXIT_X):
            raise ValueError("ENTRY is in the same place as the EXIT")
        return self


class Maze:
    """Classe principale représentant la grille du labyrinthe.
    Gère la structure de données interne, les dimensions et les cellules.
    Orchestre la génération, la résolution et l'affichage.
    """
    def __init__(self, data: Any) -> None:
        """Initialise l'instance avec ses attributs par défaut.
        Met en place l'état initial requis pour le fonctionnement.
        Configure les variables internes de l'objet.
        """
        if isinstance(data, dict):
            data = MazeConfig(**data)
        self.width: int = data.WIDTH
        self.height: int = data.HEIGHT
        self.entry: tuple[int, int] = (data.ENTRY_X, data.ENTRY_Y)
        self.exit: tuple[int, int] = (data.EXIT_X, data.EXIT_Y)
        self.logo: Logo = Logo(self)
        self.seed: str | None = data.SEED
        self.file: str = data.OUTPUT_FILE
        self.perfect: bool = data.PERFECT
        self.delay = 0.08
        self.generate_grid()

    def generate_grid(self) -> None:
        """Crée la grille vide du labyrinthe en initialisant chaque cellule.
        Met en place les objets Cell avec leurs propriétés par défaut.
        Prépare la structure avant d'appliquer l'algorithme.
        """
        self.grid: list[list[Cell]] = []
        for y in range(self.height):
            row: list[Cell] = []
            for x in range(self.width):
                cell_id: int = y * self.width + x
                row.append(Cell(x, y, cell_id))
            self.grid.append(row)

    def output_maze(self) -> None:
        """Délègue l'écriture du labyrinthe vers le fichier de sortie
        configuré.
        Appelle la classe spécialisée pour gérer l'encodage hexadécimal.
        Finalise le processus de génération du projet.
        """
        output_maze_func(self)

    def generate_logo(self) -> None | Literal[False]:
        """Place et intègre le motif central (logo) dans la structure du
        labyrinthe.
        Verrouille les cellules concernées pour empêcher la destruction de
        leurs murs.
        Vérifie que la taille permet son insertion.
        """
        self.logo = Logo(self)
        return self.logo.select_logo()

    def generate_maze(self, algo_name: str) -> None:
        """Lance l'algorithme de génération sélectionné (DFS ou Kruskal).
        Coordonne la création des murs et l'animation éventuelle.
        Constitue la fonction maîtresse de création.
        """
        algorithms: list[str] = ["DFS", "KRUSKAL", "PRIMS", "DEMO"]
        if algo_name not in algorithms:
            raise ValueError(f"Unknown algorithm: {algo_name}")
        if algo_name == "DFS":
            dfs(self)
            self.output_maze()
        elif algo_name == "KRUSKAL":
            kruskal(self)
            self.output_maze()

        elif algo_name == "DEMO":
            self.logo.make_logo_start()

    def imperfect_maze(self) -> None:
        """Transforme un labyrinthe parfait en labyrinthe imparfait.
        Brise des murs supplémentaires au hasard pour créer de
        multiples chemins.
        Ajoute de la complexité ou facilite le jeu selon la densité.
        """
        imperfect_maze_func(self)

    def generate_path(self) -> None:
        """Déclenche l'algorithme de résolution BFS pour trouver le chemin
        optimal.
        Associe la recherche de solution à l'état actuel de la grille.
        Prépare les données pour la fonction draw_path.
        """
        find_path_bfs(self)

    def draw_grid(self) -> None:
        """Dessine les éléments bruts de la grille sur l'affichage console.
        Fonction de debug
        """
        for data in self.grid:
            for visited in data:
                if not visited.visit:
                    print("0 ", end='')
                else:
                    print("1 ", end='')
            print()

    def all_cell_false(self) -> None:
        """Réinitialise le statut de visite de toutes les cellules de la
        grille.
        Permet de relancer un algorithme de parcours (comme BFS) sur un
        terrain vierge.
        Efface les traces d'anciens chemins.
        """
        for height in self.grid:
            for width in height:
                width.visit = False
        if Theme.logo_midile:
            self.generate_logo()

    def draw_path(self, type: str) -> None:
        """Affiche visuellement le chemin résolu sur le labyrinthe.
        Colore les cellules appartenant au tracé du BFS.
        Rend la solution facilement lisible pour l'utilisateur.
        """
        max_id_path = 0
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                if cell.path_id > max_id_path:
                    max_id_path = cell.path_id

        if type == "game":
            i = max_id_path
            old_x = 0
            old_y = 0
            while i != 0:
                for y in range(self.height):
                    for x in range(self.width):
                        cell = self.grid[y][x]
                        if cell.path_id != -1 and cell.path_id == i:
                            self.logo.reset_logo()
                            self.generate_logo()
                            if Theme.logo_chrono:
                                Theme.logo_midile = "0" + str(i)
                                self.generate_logo()
                            cell.path_active = True
                            if old_x < x:
                                cell.path_content = "(>)"
                                old_x = x
                            elif old_x > x:
                                cell.path_content = "(<)"
                                old_x = x
                            elif old_y > y:
                                cell.path_content = "(^)"
                                old_y = y
                            elif old_y < y:
                                cell.path_content = "(v)"
                                old_y = y
                            self.draw_maze(False)
                            cell.path_active = False
                            time.sleep(0.1)
                            i -= 1
                            break
        elif type == "basic":
            valid_colors = [
                c.value for c in Color
                if c not in (Color.RESET, Color.DEFAULT)]
            self.color = random.choice(valid_colors)
            time_start = Timer()
            b = 0
            while b <= max_id_path:
                i = max_id_path
                while i >= b:
                    for y in range(self.height):
                        for x in range(self.width):
                            cell = self.grid[y][x]
                            if cell.path_id == i:
                                if Theme.logo_chrono:
                                    self.logo.reset_logo()
                                    self.generate_logo()
                                    timestr = f"{time_start.get_time(): .0f}"
                                    Theme.logo_midile = str(timestr)
                                    self.generate_logo()
                                cell.color_case = Theme.color_path
                                if Theme.animation_draw:
                                    self.draw_maze(False)
                                if i > b:
                                    cell.color_case = Color.DEFAULT.value
                                break
                    i -= 1
                b += 1

    def all_path_false(self) -> None:
        """Efface les identifiants de chemins résolus de toutes les cellules.
        Remet à zéro l'état visuel du labyrinthe après une résolution.
        Prépare la grille pour une nouvelle recherche.
        """
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                cell.path_active = False

    def draw_maze(self, start: bool) -> None:
        """Génère et affiche le rendu ASCII/Unicode du labyrinthe dans le terminal.
        Parcourt la grille et dessine les murs, l'entrée, la sortie et le logo.
        Prend en compte les thèmes et couleurs configurés.
        """
        print("\033[H", end="")
        w = Theme.wall
        res = Color.DEFAULT.value
        entry = self.grid[self.entry[1]][self.entry[0]]
        exit_cel = self.grid[self.exit[1]][self.exit[0]]
        entry.color_case = Theme.entry_color_case
        exit_cel.color_case = Theme.exit_color_case

        for y in range(self.height):
            line_top = ""
            for x in range(self.width):
                cell = self.grid[y][x]
                cc = Theme.color_wall

                if y == 0:
                    inter = w.corner_tl.value if x == 0 else w.corner_tt.value
                else:
                    inter = w.corner_lt.value if x == 0 else w.corner_x.value

                if not cell.walls["North"]:
                    top_cell = self.grid[y-1][x] if y > 0 else None
                    if (cell.color_case != Color.DEFAULT.value and
                       top_cell and
                       top_cell.color_case != Color.DEFAULT.value):
                        h_char = cell.color_case + w.cursor.value
                    else:
                        h_char = w.box.value
                else:
                    h_char = Theme.color_wall + w.horizontal.value

                line_top += f"{cc}{inter}{h_char}{Color.DEFAULT.value}"

            last_inter = w.corner_tr.value if y == 0 else w.corner_rt.value
            print(
                f"{line_top}{Theme.color_wall}{last_inter}{res}\033[K",
                flush=True)

            line_mid = ""
            for x in range(self.width):
                cell = self.grid[y][x]

                if not cell.walls["West"]:
                    left_cell = self.grid[y][x-1] if x > 0 else None
                    if (cell.color_case != Color.DEFAULT.value and
                       left_cell and
                       left_cell.color_case != Color.DEFAULT.value):
                        v_char = cell.color_case + w.cursor.value[0]
                    else:
                        v_char = " "
                else:
                    v_char = Theme.color_wall + w.vertical.value

                if cell.path_active is not True:
                    content = (
                        cell.color_case + w.cursor.value
                        if cell.color_case != Color.DEFAULT.value
                        else w.box.value
                    )
                else:
                    content = (
                        cell.color_case + w.cursor.value
                        if cell.color_case != Color.DEFAULT.value
                        else cell.path_content
                    )

                line_mid += f"{v_char}{content}{Color.DEFAULT.value}"
            print(
                f"{line_mid}{Theme.color_wall}{w.vertical.value}{res}\033[K",
                flush=True)

            if start:
                time.sleep(self.delay)

        line_bot = ""
        for x in range(self.width):
            cell = self.grid[self.height - 1][x]
            inter = w.corner_bl.value if x == 0 else w.corner_bt.value
            
            if not cell.walls["South"]:
                h_char = w.box.value
            else:
                h_char = Theme.color_wall + w.horizontal.value

            line_bot += (
                f"{Theme.color_wall}{inter}{h_char}{Color.DEFAULT.value}")

        print(
            f"{line_bot}{Theme.color_wall}{w.corner_br.value}{res}\033[K",
            flush=True)
