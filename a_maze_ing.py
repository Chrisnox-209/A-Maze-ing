from parsing import clear, parsing_data
from labyrinth import labyrinth_generation


if __name__ == "__main__":
    file_config = "config.txt"
    data = {}
    if parsing_data(file_config) is not False:
        data = parsing_data(file_config)
        clear()
        labyrinth_generation(data)
        print(data)
