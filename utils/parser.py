import os
from typing import Callable
from maze_core.mazegen.maze.maze import MazeConfig
from pydantic import ValidationError


clear: Callable[[], int] = lambda: os.system('cls' if os.name == 'nt'
                                             else 'clear')


def parsing_data(file: str) -> MazeConfig | bool:
    """Analyse le fichier de configuration fourni en argument.
    Extrait les paires clé-valeur et gère les commentaires.
    Retourne un objet MazeConfig validé ou False en cas d'erreur.
    """
    data: dict = {}
    key: str
    x: int
    y: int
    value: str
    try:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                if not line or "=" not in line:
                    continue
                key, value = line.split("=")
                key = key.strip()
                value = value.strip()
                if key == "WIDTH":
                    data["WIDTH"] = int(value)
                elif key == "HEIGHT":
                    data["HEIGHT"] = int(value)
                elif key == "ENTRY":
                    x, y = map(int, value.split(","))
                    data["ENTRY_X"] = x
                    data["ENTRY_Y"] = y
                elif key == "EXIT":
                    x, y = map(int, value.split(","))
                    data["EXIT_X"] = x
                    data["EXIT_Y"] = y
                elif key == "OUTPUT_FILE":
                    if not value:
                        raise ValueError("OUTPUT_FILE missing")
                    data["OUTPUT_FILE"] = value
                elif key == "PERFECT":
                    if (value == "True" or
                        value == "true" or
                       value == "TRUE"):
                        data["PERFECT"] = True
                    elif (value == "False" or
                          value == "false" or
                          value == "FALSE"):
                        data["PERFECT"] = False
                elif key == "SEED":
                    data["SEED"] = str(value)
                    if data["SEED"] == "None":
                        data["SEED"] = None
        return MazeConfig(**data)
    except ValidationError as error:
        print(f"[ERROR]: {error.errors()[0]['msg']}")
        return False
    except Exception as error:
        print(f"[ERROR] {type(error).__name__}: {error}")
        return False
