from maze.parsing import clear, parsing_data
from maze.labyrinth import labyrinth_generation

def main() -> None:
     file_config = "config.txt"
     data: dict = {}
     if parsing_data(file_config) is not False:
        data = parsing_data(file_config)
        clear()
        labyrinth_generation(data)
        print(data)

if __name__ == "__main__":
	main()