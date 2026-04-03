import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def parsing_data(file: str):
    data: dict = {}
    try:
        with open(file, "r", encoding="utf-8") as content:
            for line in content:
                if "WIDTH" in line:
                    data["WIDTH"] = int(line.split("=")[-1].strip())
                elif "HEIGHT" in line:
                    data["HEIGHT"] = int(line.split("=")[-1].strip())
                elif "ENTRY" in line:
                    value = line.split("=")[-1].strip()
                    value = value.replace(",", '.')
                    data["ENTRY"] = float(value)
                elif "EXIT" in line:
                    value = line.split("=")[-1].strip()
                    value = value.replace(",", '.')
                    data["EXIT"] = float(value)
                elif "OUTPUT_FILE" in line:
                    value = line.split("=")[-1].strip()
                    if value == "":
                        raise ValueError("Error OUTPUT_FILE: add a filename")
                    data["OUTPUT_FILE"] = str(value)
                elif "PERFECT" in line:
                    value = line.split("=")[-1].strip()
                    if value not in ("True", "False"):
                        raise ValueError(f"Error PERFECT : {value}")
                    data["PERFECT"] = value
            return data
    except Exception as error:
        print(error)
        return False
