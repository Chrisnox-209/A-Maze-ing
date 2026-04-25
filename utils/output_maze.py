from maze.maze import Maze
def binToHexa(a):
    
    n = str(a)
    num = int(n, 2)
    
    hex_num = format(num, 'X')
    return(hex_num)

def output_maze(maze):
    res_files = []
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
            res_files.append(binToHexa(bin_result))
            print(binToHexa(bin_result), end= "")
        print()
        res_files.append("\n")
        res_files.append(maze.entry[0])
        res_files.append(maze.entry[1])
        res_files.append("\n")
        res_files.append(maze.exit[0])
        res_files.append(maze.exit[1])
        # print(res_files)



