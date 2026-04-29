# Mazegen

`mazegen` is a standalone Python package for generating, solving, and exporting mazes. It was designed to extract the core maze-generation logic from the “A-Maze-ing” project.

## 🚀 Features

#### Maze generation algorithms:
  - BFS
  - DFS
  - Kruskal
  - Imperfect maze generation
#### option:
  - maze display
  - stopwatch display
  - startup animation
  - animation algorithm

## 📦 Package Structure

```
maze_core/
├── LICENSE
├── README.md
├── pyproject.toml
├── test.py
└── mazegen/
    ├── algos/
    │   ├── algo_bfs.py
    │   ├── algo_dfs.py
    │   ├── imperfect_maze.py
    │   └── kruskal.py
    │
    ├── maze/
    │   ├── maze.py
    │   ├── logo.py
    │   ├── output_maze.py
    │   └── utils_enum.py
    │
    └── options/
        └── timer.py
```

## Usage Example


### install package
```python
# install pip
pip install mazegen-1.0.0-py3-none-any.whl
```

### import & initialization
```python
# import
from mazegen.maze.maze import Maze

# Create dict
dict_data = {
	"WIDTH": 18,
 	"HEIGHT": 18,
 	"ENTRY_X":1, 
 	"ENTRY_Y":1, 
 	"EXIT_X": 18, 
 	"EXIT_Y": 19, 
}

# Initialize a new maze
maze = Maze(dict_data)
```

### grid generation
```python
#grid generation
maze.generate_grid()

#logo generation
maze.generate_logo()

```
### algorithm generation
To generate the maze you can choose between "DFS" and "KRUSKAL"
exemple with kruskal
```python
maze.generate_maze("KRUSKAL")

or 

maze.generate_maze("DFS")
```
### inperfect Maze
to generate an imperfect maze you must call the imperfect_maze() function after generating the algorithm
```python
maze.generate_path()
```

### grid display
```python
#True to display the grid change demo
maze.draw_maze(False)

#path visualization
maze.draw_path("basic")
```

### Activate animation:
```python


# first import
from mazegen.maze.maze import Theme

Theme.animation_algo = True
```


# Parameters

## Maze parameters
| Parameter    | Type              | Description                                     | Constraints / Default        |
|--------------|------------------|-------------------------------------------------|------------------------------|
| WIDTH        | int              | Number of columns in the maze                   | ≥ 3                          |
| HEIGHT       | int              | Number of rows in the maze                      | ≥ 3                          |
| ENTRY_X      | int              | X coordinate of the entry cell                  | 0 ≤ ENTRY_X < WIDTH          |
| ENTRY_Y      | int              | Y coordinate of the entry cell                  | 0 ≤ ENTRY_Y < HEIGHT         |
| EXIT_X       | int              | X coordinate of the exit cell                   | 0 ≤ EXIT_X < WIDTH           |
| EXIT_Y       | int              | Y coordinate of the exit cell                   | 0 ≤ EXIT_Y < HEIGHT          |
| OUTPUT_FILE  | str              | Output file path                                | max 20 chars, default: "exit.txt" |
| PERFECT      | bool             | If True, generates a perfect maze (no loops)    | default: True                |
| SEED         | str \| None      | Random seed for reproducibility                 | optional, default: None      |

## Theme configuration

The `Theme` class allows you to customize the visual appearance and animation behavior of the maze rendering system.

It defines colors, animation settings, and UI rendering options.

You can modify it directly in the source code to change how the maze is displayed.


| Parameter                      | Type      | Description |
|--------------------------------|----------|-------------|
| color_select                  | str      | Color used for selected cells |
| color_case                    | str      | Default color for maze cells |
| color_case_logo               | str      | Color used for logo cells |
| color_wall                    | str      | Color used for walls |
| wall                          | any      | Wall rendering style / class |
| delais_draw                   | float    | Delay between each draw frame (animation speed) |
| animation_draw                | bool     | Enable/disable drawing animation |
| color_animation_backtraking   | str      | Color used during backtracking animation |
| animation_algo                | bool     | Enable/disable algorithm step animation |
| animation_draw_path           | bool     | Enable/disable path drawing animation |
| color_path                    | str      | Color used to display the final path |
| entry_color_case              | str      | Color of the entry cell |
| exit_color_case               | str      | Color of the exit cell |
| logo_midile                   | str      | Logo displayed in the maze center |
| logo_chrono                   | bool     | Enable/disable chrono display |
| default                       | str      | Reset terminal color code |


## License

This package is distributed under the MIT License. See the `LICENSE` file for more information.
