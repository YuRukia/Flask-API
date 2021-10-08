import json
def find(data, uuid):
    for i in data:
        if i["uuid"] == uuid:
            return i
        else:
            return False

