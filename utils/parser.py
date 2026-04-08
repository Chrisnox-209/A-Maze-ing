import os
from typing import Literal


def clear() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def parsing_data(file: str) -> dict | Literal[False]:
    data: dict = {}
    try:
        with open(file, "r", encoding="utf-8") as content:
            for line in content:
                if "WIDTH" in line:
                    data["WIDTH"] = int(line.split("=")[-1].strip())
                elif "HEIGHT" in line:
                    data["HEIGHT"] = int(line.split("=")[-1].strip())
                elif "ENTRY" in line:
                    value_entry: str = line.split("=")[-1].strip()
                    value_entry = value_entry.replace(",", '.')
                    data["ENTRY"] = float(value_entry)
                elif "EXIT" in line:
                    value_exit: str = line.split("=")[-1].strip()
                    value_exit = value_exit.replace(",", '.')
                    data["EXIT"] = float(value_exit)
                elif "OUTPUT_FILE" in line:
                    value_str: str = line.split("=")[-1].strip()
                    if value_str == "":
                        raise ValueError("Error OUTPUT_FILE: add a filename")
                    data["OUTPUT_FILE"] = str(value_str)
                elif "PERFECT" in line:
                    value_bool: str = line.split("=")[-1].strip()
                    if value_bool not in ("True", "False"):
                        raise ValueError(f"Error PERFECT : {value_bool}")
                    data["PERFECT"] = value_bool
            return data
    except Exception as error:
        print(error)
        return False
