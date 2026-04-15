import os
from typing import Self, Callable, Optional
from pydantic import BaseModel, Field, ValidationError, model_validator

clear: Callable[[], int] = lambda: os.system('cls' if os.name == 'nt'
                                             else 'clear')


class MazeConfig(BaseModel):
    WIDTH: int = Field(ge=3)
    HEIGHT: int = Field(ge=3)
    ENTRY_X: int = Field(ge=0)
    ENTRY_Y: int = Field(ge=0)
    EXIT_X: int = Field(ge=0)
    EXIT_Y: int = Field(ge=0)
    OUTPUT_FILE: str = Field(default="exit.txt", max_length=20)
    PERFECT: bool = Field(default=True)
    SEED:  Optional[str] = Field(default=None, min_length=1)

    @model_validator(mode='after')
    def check_entry(self) -> Self:
        if (self.ENTRY_X >= self.WIDTH):
            raise ValueError("ENTRY X is outside the maze.")
        if (self.ENTRY_Y >= self.HEIGHT):
            raise ValueError("ENTRY Y is outside the maze.")
        return self

    @model_validator(mode='after')
    def check_exit(self) -> Self:
        if (self.EXIT_X >= self.WIDTH):
            raise ValueError("EXIT X is outside the maze.")
        if (self.EXIT_Y >= self.HEIGHT):
            raise ValueError("EXIT Y is outside the maze.")
        return self


def parsing_data(file: str) -> MazeConfig | bool:
    data: dict = {}
    key: str
    x: int
    y: int
    value: str
    try:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                key,  value = line.split("=")
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
                elif key == "SEED":
                    data["SEED"] = str(value)
        return MazeConfig(**data)
    except ValidationError as error:
        print(f"[ERROR]: {error.errors()[0]['msg']}")
        return False
    except ValidationError as error:
        print(f"[ERROR]: {error.errors()[0]['msg']}")
        return False
