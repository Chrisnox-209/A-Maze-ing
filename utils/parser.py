import os
from typing import Self, Callable, Optional
import sys
try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except Exception as e:
    print(e)
    sys.exit(1)

clear: Callable[[], int] = lambda: os.system('cls' if os.name == 'nt'
                                             else 'clear')


class MazeConfig(BaseModel):
    """Modèle de validation pour la configuration du labyrinthe.
    Vérifie les types et les valeurs (hauteur, largeur, seed, etc.).
    Utilise Pydantic pour s'assurer que les données sont conformes.
    """
    WIDTH: int = Field(ge=3)
    HEIGHT: int = Field(ge=3)
    ENTRY_X: int = Field(ge=0)
    ENTRY_Y: int = Field(ge=0)
    EXIT_X: int = Field(ge=0)
    EXIT_Y: int = Field(ge=0)
    OUTPUT_FILE: str = Field(default="exit.txt", max_length=20)
    PERFECT: bool = Field(default=True)
    SEED: Optional[str] = Field(default=None, min_length=1)

    @model_validator(mode='after')
    def check_entry(self) -> Self:
        """Vérifie la validité des coordonnées d'entrée du labyrinthe.
        Lève une erreur si l'entrée est en dehors des limites.
        S'assure que l'entrée est bien sur un bord du labyrinthe.
        """
        if (self.ENTRY_X >= self.WIDTH):
            raise ValueError("ENTRY X is outside the maze.")
        if (self.ENTRY_Y >= self.HEIGHT):
            raise ValueError("ENTRY Y is outside the maze.")
        return self

    @model_validator(mode='after')
    def check_exit(self) -> Self:
        """Vérifie la validité des coordonnées de sortie du labyrinthe.
        Lève une erreur si la sortie est hors limites ou identique à l'entrée.
        S'assure que la sortie se trouve bien sur un bord externe.
        """
        if (self.EXIT_X >= self.WIDTH):
            raise ValueError("EXIT X is outside the maze.")
        if (self.EXIT_Y >= self.HEIGHT):
            raise ValueError("EXIT Y is outside the maze.")
        return self

    @model_validator(mode='after')
    def check_door(self) -> Self:
        """Applique les vérifications complètes sur l'entrée et la sortie.
        S'assure que ces deux portes respectent les dimensions de la grille.
        Valide la cohérence globale des accès au labyrinthe.
        """
        if (self.ENTRY_Y == self.EXIT_Y and self.ENTRY_X == self.EXIT_X):
            raise ValueError("ENTRY is in the same place as the EXIT")
        return self


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
                    data["PERFECT"] = value.lower() == "true"
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
