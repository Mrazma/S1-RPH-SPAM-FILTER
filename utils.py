def read_classification_from_file(filename: str):
    clsf = dict()

    with open(filename, "rt", encoding="utf-8") as file:
        clsf = {
            parts[0]: parts[1]
            for line in file.readlines()
            if (parts := line.split())
        }

    return clsf


def write_classification_to_file(filename: str, clsf: dict):
    with open(filename, "wt", encoding="utf-8") as file:
        file.writelines([f"{name} {status}\n" for name, status in clsf.items()])

