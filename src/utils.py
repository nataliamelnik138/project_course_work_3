import json


def loads_from_file(file):
    with open(file, 'rt', encoding='utf-8') as f:
        return json.load(f)
