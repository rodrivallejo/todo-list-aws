import json
import decimalencoder
import todoList

# devuelve un elemento de la todo list,
# dependiendo del evento pasado por parametro.


def get(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
