def binToHexa(a):
    
    n = str(a)
    num = int(n, 2)
    
    hex_num = format(num, 'X')
    return(hex_num)

def output_path(maze):
    maze.generate_path()
    
    coords = {}
    for y in range(maze.height):
        for x in range(maze.width):
            val = maze.grid[y][x].path_id
            if val > 0:
                coords[val] = (x, y)
    res = ""
    for i in range(1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[i + 1]
        if x2 > x1: res += "E"
        elif x2 < x1: res += "W"
        elif y2 > y1: res += "S"
        elif y2 < y1: res += "N"
    rev = res[::-1]
    return rev


def output_maze_func(maze):
    res_files = []
    name_files = maze.file
    try:
        with open(name_files, "w") as f:
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



