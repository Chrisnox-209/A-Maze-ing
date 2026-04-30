from typing import Any, LiteralString


def binToHexa(a: str | int) -> str:
    """Convertit une valeur binaire (chaîne) en caractère hexadécimal.
    Prend 4 bits et retourne l'équivalent de '0' à 'F'.
    Utilisé pour formater l'état des murs de chaque cellule.
    """

    n = str(a)
    num = int(n, 2)

    hex_num: str = format(num, 'X')
    return (hex_num)


def output_path(maze: Any) -> LiteralString:
    """Convertit une séquence de coordonnées en directions cardinales.
    Parcourt le chemin et associe chaque pas à N, S, E, ou W.
    """
    maze.generate_path()

    coords = {}
    for y in range(maze.height):
        for x in range(maze.width):
            val = maze.grid[y][x].path_id + 1
            if val > 0:
                coords[val] = (x, y)
    res = ""
    len_cords = len(coords)
    coords[len_cords + 1] = maze.entry
    for i in range(1, len(coords)):
        x2, y2 = coords[i + 1]
        x1, y1 = coords[i]
        if x2 > x1:
            res += "W"
        elif x2 < x1:
            res += "E"
        elif y2 > y1:
            res += "N"
        elif y2 < y1:
            res += "S"
    rev = res[::-1]
    return rev


def output_maze_func(maze: Any) -> None:
    """Sauvegarde le labyrinthe complet dans le fichier de configuration.
    Génère l'encodage hexadécimal ligne par ligne.
    Ajoute ensuite les coordonnées et la solution à la fin.
    """
    name_files = maze.file
    try:
        with open(name_files, "w", encoding="utf-8") as f:
            for height in range(maze.height):
                for width in range(maze.width):
                    cell_bin = []
                    cell = maze.grid[height][width]
                    north = int(cell.walls["North"])
                    south = int(cell.walls["South"])
                    east = int(cell.walls["East"])
                    west = int(cell.walls["West"])
                    cell_bin.append(west)
                    cell_bin.append(south)
                    cell_bin.append(east)
                    cell_bin.append(north)
                    bin_result = int(''.join(map(str, cell_bin)))
                    f.write(binToHexa(bin_result))
                f.write("\n")
            f.write("\n")
            f.write(str(maze.entry[0]))
            f.write(",")
            f.write(str(maze.entry[1]))
            f.write("\n")
            f.write(str(maze.exit[0]))
            f.write(",")
            f.write(str(maze.exit[1]))
            f.write("\n")
            f.write(output_path(maze))
    except Exception as e:
        print(e)
