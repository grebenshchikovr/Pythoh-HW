def list_to_string(data):
    return "\n".join(map(str, data))


def write_dict_to_files(data: dict):
    for filename, values in data.items():
        with open(f"{filename}.txt", "w") as f:
            f.write(list_to_string(values))


data = {
    "Name": [3, 1, 2, 3, 4],
    "Surname": [3, 4, 5, 6, 7, 8],
    "Fathername": [3, 4, 5, 6, 7, 8]
    }


write_dict_to_files(data)