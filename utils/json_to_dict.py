import json

def json_to_dict(path):
    with open(path, 'r') as archivo:
        dictionary = json.load(archivo)
    return dictionary
