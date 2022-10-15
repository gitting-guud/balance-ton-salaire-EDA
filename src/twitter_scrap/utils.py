import json


def write_jsonlines(data, path):
    with open(path, "w") as f:
        for line in data:
            json.dump(line, f)
            f.write("\n")


def read_jsonlines(path):
    data = []
    with open(path, "r") as f:
        for line in f:
            data.append(json.load(line))
    return data
