# inport
from mazegen.maze.maze import Maze, Theme

def main() -> None:
	# dictionary declaration
	dict_data: dict[str, int] = {
	    "WIDTH": 18,
	 	"HEIGHT": 18,
	 	"ENTRY_X":1, 
	 	"ENTRY_Y":1, 
	 	"EXIT_X": 18, 
	 	"EXIT_Y": 19, 
	}

	# activate animation
	Theme.animation_algo = True

	try:
		# Initialize a new maze
		maze = Maze(dict_data)

		# grid generation
		maze.generate_grid()
		# logo generation
		maze.generate_logo()

		# generate maze
		maze.generate_maze("KRUSKAL")
	except Exception as e:
		print(e)


if __name__ == "__main__":
    main()

