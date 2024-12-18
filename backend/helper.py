import json

def read_json():
    with open('data.json', 'r') as f:
        names = json.load(f)
        return names

def write_json(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
