import os
from typing import Callable
from pydantic import BaseModel, Field, ValidationError

clear: Callable[[], int] = lambda: os.system('cls' if os.name == 'nt'
                                             else 'clear')


class MazeConfig(BaseModel):
    WIDTH: int = Field(ge=3)
    HEIGHT: int = Field(ge=3)
    ENTRY_X: int = Field(ge=0, le=100)
    ENTRY_Y: int = Field(ge=0, le=100)
    EXIT_X: int = Field(ge=0, le=100)
    EXIT_Y: int = Field(ge=0, le=100)
    OUTPUT_FILE: str = Field(default="exit.txt", max_length=20)
    PERFECT: bool = Field(default=True)


def parsing_data(file: str) -> MazeConfig | bool:
    data = {}
    try:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
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
                    data["PERFECT"] = value.lower() == "true"
        return MazeConfig(**data)
    except (Exception, ValidationError) as error:
        print(f"[ERROR]: {error.errors()[0]['msg']}")
        return False
