*This project has been created as part of the 42 curriculum by cpietrza, papilaz*



# 🧩 A-Maze-ing — Générateur de Labyrinthe

<p align="center">
  <img src="./maze.gif" alt="Demo" />
</p>


## 📖 Description



A-Maze-ing est un projet Python qui génère un labyrinthe aléatoire à partir d’un fichier de configuration.

Le programme construit une structure valide, éventuellement parfaite (un seul chemin entre l’entrée et la sortie),

sauvegarde le résultat dans un format hexadécimal et propose une représentation visuelle.



### Objectifs

- Génération de labyrinthes
- Algorithmes et graphes
- Génération aléatoire reproductible
- Architecture Python propre et réutilisable
- Interface CLI + affichage



---



# ⚙️ Installation



## Installation

```bash
make install
```



## Démarrage

```bash
make run
```



---



# 📂 Structure du Projet

```bash
.
├── maze_core
│   ├── __init__.py
│   ├── LICENSE
│   ├── mazegen
│   │   ├── algos
│   │   │   ├── algo_bfs.py
│   │   │   ├── algo_dfs.py
│   │   │   ├── imperfect_maze.py
│   │   │   ├── __init__.py
│   │   │   └── kruskal.py
│   │   ├── maze
│   │   │   ├── __init__.py
│   │   │   ├── logo.py
│   │   │   ├── maze.py
│   │   │   ├── output_maze.py
│   │   │   └── utils_enum.py
│   │   ├── options
│   │   │   ├── __init__.py
│   │   │   └── timer.py
│   │   └── test.py
│   ├── pyproject.toml
│   └── README.md
├── options
│   ├── __init__.py
│   ├── menu.py
│   └── options.py
├── utils
│   ├── __init__.py
│   └── parser.py
├── pyproject.toml
├── a_maze_ing.py
├── config.txt
├── Makefile
└── README.md
```



---



# 🧠 Algorithmes utilisés



## DFS — Depth First Search

L’algorithme DFS (Depth First Search) est utilisé pour générer un labyrinthe parfait.

Le principe consiste à :

1. Partir du point de depart 
2. Explorer récursivement une direction
3. Supprimer les murs entre cellules voisines
4. Revenir en arrière lorsqu’aucun chemin n’est disponible



### Avantages

- Rapide
- Facile à implémenter
- Génère des labyrinthes très organiques



---



## BFS — Breadth First Search

Le BFS est utilisé pour :

- la recherche de chemin
- l’affichage du chemin de sortie
- certaines vérifications de connectivité



Le parcours se fait niveau par niveau afin de garantir le chemin le plus court.



---



## Kruskal

L’algorithme de Kruskal permet également de générer des labyrinthes parfaits.

Chaque cellule est considérée comme un ensemble indépendant.

On casse ensuite les murs aléatoirement uniquement si cela ne crée pas de cycle.



### Avantages

- Génération équilibrée
- Structure plus homogène
- Basé sur les graphes et Union-Find



---



# 🛠️ Configuration du Labyrinthe



Le fichier `config.txt` permet de personnaliser entièrement la génération du labyrinthe.



## Exemple

```txt
WIDTH=25
HEIGHT=15
ENTRY=0,1
EXIT=24,13
OUTPUT_FILE=maze.txt
PERFECT=true
SEED=42
```



---



# 📋 Tableau de Configuration (`config.txt`)



| Clé | Type | Description | Valeurs autorisées |
|------|------|------|------|
| `WIDTH` | `int` | Largeur du labyrinthe | Minimum `3` |
| `HEIGHT` | `int` | Hauteur du labyrinthe | Minimum `3` |
| `ENTRY` | `x,y` | Coordonnées d’entrée | Doit être dans la grille |
| `EXIT` | `x,y` | Coordonnées de sortie | Doit être dans la grille |
| `OUTPUT_FILE` | `str` | Nom du fichier de sortie | Doit finir par `.txt` |
| `PERFECT` | `bool` | Génère un labyrinthe parfait | `true` / `false` |
| `SEED` | `str / None` | Seed pour génération reproductible | Texte ou `None` |



---



# ✅ Validations automatiques



Le parser vérifie automatiquement :



| Vérification | Description |
|------|------|
| Taille minimale | `WIDTH` et `HEIGHT` ≥ 3 |
| Entrée valide | L’entrée doit être dans les limites |
| Sortie valide | La sortie doit être dans les limites |
| Entrée ≠ Sortie | Les coordonnées doivent être différentes |
| Extension fichier | Le fichier doit finir par `.txt` |
| Seed valide | Peut être vide ou définie |



---



# 🎨 Configuration du Thème



Le rendu visuel du labyrinthe est configurable via la classe `Theme`.

Certaines valeurs sont modifiables depuis le menu interactif.

⚠️ Si vous ne passez pas par le menu, les valeurs restent celles définies en hard coding dans la classe.



## Configuration actuelle



| Variable | Description |
|------|------|
| `color_select` | Couleur des éléments sélectionnés |
| `color_case` | Couleur des cellules normales |
| `color_case_logo` | Couleur du logo |
| `color_wall` | Couleur des murs |
| `wall` | Style de mur utilisé |
| `delais_draw` | Délai d’animation du dessin |
| `animation_draw` | Active l’animation de génération |
| `color_animation_backtraking` | Couleur du backtracking |
| `animation_algo` | Active l’animation des algorithmes |
| `animation_draw_path` | Animation du chemin final |
| `color_path` | Couleur du chemin solution |
| `entry_color_case` | Couleur de l’entrée |
| `exit_color_case` | Couleur de la sortie |
| `logo_midile` | Logo affiché au centre |
| `logo_chrono` | Active le chrono du logo |




---



# 🖥️ Interface CLI



Le projet propose un menu interactif basé sur la librairie `rich`.

Fonctionnalités :

- Navigation interactive
- Affichage dynamique
- Personnalisation du thème
- Personnalisation des couleur
- Personnalisation du logo
- Lancement des algorithmes
- Animations algorithmes
- Parametrage du labyrinthe depuis le menu



---


# 📦 Format de sortie



Le labyrinthe est sauvegardé dans un fichier `.txt`.

Le contenu est exporté sous forme :

- de structure lisible
- de données exploitables
- d’encodage hexadécimal selon le mode choisi



---

# 🚀 Commandes de bases


### Utilisation
```bash
make install
make run
```

### Creer le package
```bash
make build
```

### Nettoyer
```bash
make clean
```

### Tester les types hints et pep8
```bash
make lint
```
---

# 📚 Sources & Documentation



## DFS / BFS

- https://favtutor.com/blogs/depth-first-search-python
- https://www.geeksforgeeks.org/python/python-program-for-breadth-first-search-or-bfs-for-a-graph/
- https://reeborg.ca/docs/en/reference/mazes.html



## Kruskal

- https://weblog.jamisbuck.org/2011/1/3/maze-generation-kruskal-s-algorithm
- https://www.youtube.com/watch?v=71UQH7Pr9kU



## Interface / Menu

- https://rich.readthedocs.io/en/latest/layout.html
- https://www.youtube.com/watch?v=vr375zT8PFE



---


## ⚠️ Disclaimer (Note Pédagogique 42)

Ce dépôt est rendu **public uniquement à titre pédagogique**.

Conformément à l'esprit et aux règles de l'école 42, l'utilisation de ce code (copie, plagiat, ou soumission) est **strictement interdite** et peut entraîner la disqualification ou l'échec de votre propre projet. Il est destiné à servir d'exemple de structure et de logique, mais ne doit en aucun cas être utilisé pour valider votre propre progression.

**Apprenez par vous-même !**

---

## 👤 Auteur



Projet réalisé dans le cadre du cursus 42 par :

- cpietrza
- papilaz