import json
def load(file):
    with open(file) as f:
        data = json.load(f)
        return data
