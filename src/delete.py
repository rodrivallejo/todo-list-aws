import todoList

# Borra elemento del todo list pasado por parametro


def delete(event, context):
    todoList.delete_item(event['pathParameters']['id'])

    # create a response
    return {
        "statusCode": 200
    }
    