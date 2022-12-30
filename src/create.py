import json
import logging
import todoList

# Funcion que agrega un item al todoList, 
# primero valida que tenga contenido para agregarlo,
# devolviendo el estado y el item
def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation failed")
        raise Exception("Couldn't create the todo item.")
    item = todoList.put_item(data['text'])
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    return response
