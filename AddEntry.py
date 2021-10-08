import uuid
import json
import datetime

def addOrder(manufacturer, model, totalPrice):
    newOrder = {
        "uuid": uuid.uuid4().hex,
        "manufacturer": manufacturer,
        "model": model,
        "total price": totalPrice,
        "datePlaced": str(datetime.datetime.now())
        }
    with open('./orders.json', "r") as json_file:
        data = json.load(json_file)

    data.append(newOrder)

    with open('./orders.json', "w") as json_file:
        json.dump(data, json_file)

    return newOrder["uuid"]
