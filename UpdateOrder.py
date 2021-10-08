import uuid
import json

def update(requestForm):
    
    uuid = requestForm['uuid']
    manufacturer = requestForm['manufacturer']
    model = requestForm['model']
    totalPrice = requestForm['totalPrice']
    
    with open('./orders.json', "r") as json_file:
        data = json.load(json_file)

    i = 0
    foundEntry = False
    for x in data:
        if x["uuid"] == uuid:
            data[i]["manufacturer"] = manufacturer
            data[i]["model"] = model
            data[i]["total price"] = totalPrice
            foundEntry = True
        i = i + 1

    with open('./orders.json', "w") as json_file:
        json.dump(data, json_file)

    return foundEntry
