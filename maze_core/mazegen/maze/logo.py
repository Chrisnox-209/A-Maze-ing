from typing import Literal, Any

try:
    import random
    from ..maze.utils_enum import Color, Theme
    import time
except Exception as e:
    print(e)


def number_zero() -> list[list[int]]:
    """Génère la matrice représentant le chiffre zéro.
    """
    pattern: list[list[int]] = [
        [1, 1, 1],
        [1, 2, 1],
        [1, 2, 1],
        [1, 2, 1],
        [1, 1, 1],
    ]
    return pattern


def number_one() -> list[list[int]]:
    """Génère la matrice représentant le chiffre un.
    """
    pattern: list[list[int]] = [
        [2, 1, 2],
        [1, 1, 2],
        [2, 1, 2],
        [2, 1, 2],
        [1, 1, 1],
    ]
    return pattern


def number_two() -> list[list[int]]:
    """Génère la matrice représentant le chiffre deux.
    """
    pattern: list[list[int]] = [
        [1, 1, 1],
        [2, 2, 1],
        [1, 1, 1],
        [1, 2, 2],
        [1, 1, 1]
    ]
    return pattern


def number_tree() -> list[list[int]]:
    """Génère la matrice représentant le chiffre trois.
    """
    pattern: list[list[int]] = [
        [1, 1, 1],
        [2, 2, 1],
        [1, 1, 1],
        [2, 2, 1],
        [1, 1, 1]
    ]
    return pattern


def number_fourth() -> list[list[int]]:
    """Génère la matrice représentant le chiffre quatre.
    """
    pattern: list[list[int]] = [
        [1, 2, 1,],
        [1, 2, 1,],
        [1, 1, 1,],
        [2, 2, 1,],
        [2, 2, 1,]
    ]
    return pattern


def number_five() -> list[list[int]]:
    """Génère la matrice représentant le chiffre cinq.
    """
    pattern: list[list[int]] = [
        [1, 1, 1,],
        [1, 2, 2,],
        [1, 1, 1,],
        [2, 2, 1,],
        [1, 1, 1,]
    ]
    return pattern


def number_six() -> list[list[int]]:
    """Génère la matrice représentant le chiffre six.
    """
    pattern: list[list[int]] = [
        [1, 1, 1,],
        [1, 2, 2,],
        [1, 1, 1,],
        [1, 2, 1,],
        [1, 1, 1,]
    ]
    return pattern


def number_seven() -> list[list[int]]:
    """Génère la matrice représentant le chiffre sept.
    Construit le motif géométrique du chiffre sept.
    Sert pour l'horloge ou les indications visuelles.
    """
    pattern: list[list[int]] = [
        [1, 1, 1,],
        [2, 2, 1,],
        [2, 2, 1,],
        [2, 2, 1,],
        [2, 2, 1,]
    ]
    return pattern


def number_eighth() -> list[list[int]]:
    """Génère la matrice représentant le chiffre huit.
    """
    pattern: list[list[int]] = [
        [1, 1, 1,],
        [1, 2, 1,],
        [1, 1, 1,],
        [1, 2, 1,],
        [1, 1, 1,]
    ]
    return pattern


def number_ninth() -> list[list[int]]:
    """Génère la matrice représentant le chiffre neuf.
    """
    pattern: list[list[int]] = [
        [1, 1, 1,],
        [1, 2, 1,],
        [1, 1, 1,],
        [2, 2, 1,],
        [1, 1, 1,]
    ]
    return pattern


def reset_logo_func() -> list[list[int]]:
    """Réinitialise l'état et les cellules occupées par le logo.
    Libère l'espace au centre pour pouvoir redessiner ou nettoyer.
    Assure que l'ancien logo n'interfère pas avec le nouveau.
    """
    pattern: list[list[int]] = [
        [2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2,],
    ]
    return pattern


def choice_number(number: str) -> list[list[int]]:
    """Sélectionne et retourne la matrice correspondant à un chiffre donné en
    string.
    Associe le caractère '0'-'9' à sa fonction génératrice respective.
    """
    if number == "0":
        return number_zero()
    if number == "1":
        return number_one()
    if number == "2":
        return number_two()
    if number == "3":
        return number_tree()
    if number == "4":
        return number_fourth()
    if number == "5":
        return number_five()
    if number == "6":
        return number_six()
    if number == "7":
        return number_seven()
    if number == "8":
        return number_eighth()
    if number == "9":
        return number_ninth()
    return number_zero()


def combine_twoo_number(number_one: str, number_twoo: str) -> list:
    """Combine les matrices de deux chiffres pour former un nombre (ex: '42').
    Gère l'espacement et l'alignement entre les deux formes.
    Retourne le motif global prêt à être intégré.
    """
    res_number: list = []
    res_ligne_fusion: list = []
    res_choice_one: list[list[int]] = choice_number(number_one)
    res_choice_twoo: list[list[int]] = choice_number(number_twoo)
    len_number_one: int = len(res_choice_one[0])
    len_number_twoo: int = len(res_choice_twoo[0])
    for a in range(5):
        for i in range(len_number_one + len_number_twoo + 1):
            if i < len_number_one:
                res_ligne_fusion.append(res_choice_one[a][i])
            if i == (len_number_one + 1):
                res_ligne_fusion.append(2)
            if i > len_number_one:
                res_ligne_fusion.append(
                    res_choice_twoo[a][i - (len_number_one + 1)])
        res_number.append(res_ligne_fusion)
        res_ligne_fusion = []
    return res_number


def create_number(number: str) -> list:
    """Analyse une chaîne de caractères et génère la matrice visuelle associée.
    """
    for i in range(len(number)):
        number_res: list = combine_twoo_number(number[i - 1], number[i])
    return number_res


class Logo:
    """Enumération des identifiants ou types de logos disponibles.
    Gère les différentes formes qui peuvent être affichées (42, Timer, etc.).
    Facilite la sélection du motif central.
    """
    def __init__(self, maze: Any) -> None:
        """Initialise l'instance avec ses attributs par défaut.
        Met en place l'état initial requis pour le fonctionnement.
        Configure les variables internes de l'objet.
        """
        self.maze: Any = maze
        self.color: str = Theme.color_case_logo
        if Theme.color_case_logo == "random":
            self.color = Color.random_color()

    def random_color_2(self) -> None:
        """Méthode alternative pour changer la couleur de manière aléatoire.
        Modifie les attributs de l'instance pour appliquer la nouvelle couleur.
        Crée un effet de clignotement ou de variation.
        """
        valid_colors: list[str] = [
            c.value for c in Color if c not in (
                Color.RESET, Color.DEFAULT)]
        self.color = random.choice(valid_colors)
        self.select_logo()

    def select_logo(self) -> None | Literal[False]:
        """Identifie et sélectionne le type de logo à dessiner selon le thème
        actuel.
        Gère les options comme l'icône Home, l'Invader, ou un
        chronomètre dynamique.
        Retourne l'état ou False si l'espace est insuffisant.
        """
        self.reset_logo()
        if Theme.logo_midile == "LOGO_42":
            self.logo_42()
        if Theme.logo_midile == "GRID":
            self.logo_checkerboardr()
        if Theme.logo_midile == "INVADER":
            self.logo_invader()
        if Theme.logo_midile == "HOME":
            self.logo_home()
        if Theme.logo_midile == "HEART":
            self.logo_heart()
        if Theme.logo_midile == "STING":
            self.logo_sting()
        try:
            int(Theme.logo_midile)
            self.pattern: list = create_number(Theme.logo_midile)
        except BaseException:
            pass
        return self.make_logo()

    def change_color_logo(self) -> None:
        """Modifie aléatoirement ou spécifiquement la couleur du logo affiché.
        Permet des effets de clignotement ou des transitions de couleurs
        animées.
        Met à jour l'état visuel des cellules concernées.
        """
        self.color = Theme.color_case_logo
        if Theme.color_case_logo == "random":
            self.color = Color.random_color()

    def logo_invader(self) -> None:
        """Génère la matrice pour le logo en forme de Space Invader.
        Positionne les blocs pour dessiner le motif rétro.
        Ajoute une touche ludique au centre du labyrinthe.
        """
        self.pattern = [
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 1, 1, 0, 0, 0]
        ]

    def logo_home(self) -> None:
        """Génère la matrice pour le logo en forme de petite maison.
        Calcule les coordonnées de la structure de base et du toit.
        Option décorative pour le générateur.
        """
        self.pattern = [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0]
        ]

    def logo_42(self) -> None:
        """Dessine le logo officiel de l'école 42 dans la grille.
        Combine les chiffres '4' et '2' avec l'espacement correct.
        Satisfait la contrainte visuelle du sujet.
        """
        self.pattern = [
            [1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 1, 1]
        ]

    def logo_42_start(self) -> None:
        """Dessine la version initiale ou alternative du logo 42.
        Affiche le motif au moment du démarrage ou dans des menus spécifiques.
        Contribue à l'identité visuelle de l'application.
        """
        self.pattern = [
            ["A", 0, "E", 0, "J", "K", "L"],
            ["B", 0, "F", 0, 0, 0, "M"],
            ["C", "D", "G", 0, "P", "O", "N"],
            [0, 0, "H", 0, "Q", 0, 0],
            [0, 0, "I", 0, "R", "S", "T"]
        ]

    def logo_heart(self) -> None:
        """Génère les coordonnées pour dessiner un motif en forme de cœur.
        Option cosmétique pour personnaliser l'affichage central.
        Utilise la grille pour former l'image pixélisée.
        """
        self.pattern = [
            [0, 1, 1, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0]
        ]

    def logo_checkerboardr(self) -> None:
        """Crée un motif en damier (checkerboard) pour le centre du labyrinthe.
        Alterne les cellules pleines et vides sur la zone cible.
        Offre un effet visuel texturé.
        """
        self.pattern = [
            [1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1]
        ]

    def logo_sting(self) -> None:
        """Dessine un motif stylisé (sting) au centre de la grille.
        Ajoute une variante graphique supplémentaire pour l'utilisateur.
        Calculé dynamiquement selon la taille disponible.
        """
        self.pattern = [
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0]
        ]

    def reset_logo(self) -> None:
        """Nettoie le logo actuel en réinitialisant les couleurs des cellules
        cibles.
        Permet de préparer la zone pour un nouveau dessin.
        Évite les chevauchements visuels indésirables.
        """
        self.pattern = reset_logo_func()
        self.make_logo()

    def make_logo(self) -> None | Literal[False]:
        """Applique les couleurs et les propriétés de murs pour former le logo.
        Transforme les matrices de coordonnées abstraites en affichage réel.
        Appelle les fonctions de dessin spécifiques selon le choix.
        """
        self.maze.logo_ids = set()
        if Theme.logo_midile is None:
            return False
        width_logo: int = len(self.pattern[0])
        height_logo: int = len(self.pattern)
        if self.maze.width <= width_logo + 4 \
                or self.maze.height < height_logo + 4:
            return False
        start_x: Any = (self.maze.width - width_logo) // 2
        start_y: Any = (self.maze.height - height_logo) // 2

        for row in range(height_logo):
            for col in range(width_logo):
                if self.pattern[row][col] == 2 and Theme.logo_chrono:
                    grid_y: Any = start_y + row
                    grid_x: Any = start_x + col
                    cell: Any = self.maze.grid[grid_y][grid_x]
                    cell.color_case = Color.DEFAULT.value
                    self.maze.logo_ids.add(cell.cell_id)
                    cell.visit = True
                    cell.walls["North"] = True
                    cell.walls["East"] = True
                    cell.walls["South"] = True
                    cell.walls["West"] = True

                if self.pattern[row][col] == 1:
                    grid_y = start_y + row
                    grid_x = start_x + col
                    cell = self.maze.grid[grid_y][grid_x]
                    self.maze.logo_ids.add(cell.cell_id)
                    cell.color_case = self.color
                    cell.visit = True
                    if row > 0 and self.pattern[row - 1][col] == 1:
                        cell.walls["North"] = False
                    if row < height_logo - \
                            1 and self.pattern[row + 1][col] == 1:
                        cell.walls["South"] = False
                    if col > 0 and self.pattern[row][col - 1] == 1:
                        cell.walls["West"] = False
                    if col < width_logo - \
                            1 and self.pattern[row][col + 1] == 1:
                        cell.walls["East"] = False
        """ Verifie si l'entree et la sortie de sont pas sur le logo"""
        exit_id: int = self.maze.exit[1] * self.maze.width + self.maze.exit[0]
        entry_id: int = self.maze.entry[1] * self.maze.width + self.maze.entry[0]
        if exit_id in self.maze.logo_ids or entry_id in self.maze.logo_ids:
            raise ValueError("the entrance or exit is located inside the logo")
        return None

    def make_logo_start(self) -> None:
        """Dessine l'animation ou le logo de départ avec un effet visuel.
        S'assure que l'affichage d'accueil est correctement rendu.
        Marque le début de l'exécution du programme.
        """
        self.maze.logo_ids = set()
        self.logo_42_start()
        list_cell: list = []
        width_logo: int = len(self.pattern[0])
        height_logo: int = len(self.pattern)

        start_x: Any = (self.maze.width - width_logo) // 2
        start_y: Any = (self.maze.height - height_logo) // 2

        for row in range(height_logo):
            for col in range(width_logo):
                if self.pattern[row][col] != 0:
                    grid_y: Any = start_y + row
                    grid_x: Any = start_x + col
                    cell: Any = self.maze.grid[grid_y][grid_x]
                    list_cell.append((cell, self.pattern[row][col]))

                    cell_id: Any = grid_y * self.maze.width + grid_x
                    self.maze.logo_ids.add(cell_id)

                    if row > 0 and self.pattern[row - 1][col] != 0:
                        cell.walls["North"] = False
                        self.maze.grid[grid_y -
                                       1][grid_x].walls["South"] = False
                    if row < height_logo - \
                            1 and self.pattern[row + 1][col] != 0:
                        cell.walls["South"] = False
                        self.maze.grid[grid_y +
                                       1][grid_x].walls["North"] = False
                    if col > 0 and self.pattern[row][col - 1] != 0:
                        cell.walls["West"] = False
                        self.maze.grid[grid_y][grid_x -
                                               1].walls["East"] = False
                    if col < width_logo - \
                            1 and self.pattern[row][col + 1] != 0:
                        cell.walls["East"] = False
                        self.maze.grid[grid_y][grid_x +
                                               1].walls["West"] = False
            time.sleep(0.09)
            self.maze.draw_maze(False)

        list_cell.sort(key=lambda letter: letter[1])

        for c in list_cell:
            cell = c[0]
            cell.color_case = self.color
            time.sleep(0.07)
            self.maze.draw_maze(False)
