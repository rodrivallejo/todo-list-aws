import json
import logging
import todoList

# Funcion que crea un evento en el todolist

def create(event, context):

    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation failed")
        raise Exception("Couldn't create the todo item.")
    item = todoList.put_item(data['text'])
    # create a response
    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }
