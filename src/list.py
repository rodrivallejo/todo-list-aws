import json
import decimalencoder
import todoList

# Devuelve todos los elementos del todo list


def list(event, context):
    # fetch all todos from the database
    result = todoList.get_items()
    # create a response
    return {
        "statusCode": 200,
        "body": json.dumps(result, cls=decimalencoder.DecimalEncoder)
    }
