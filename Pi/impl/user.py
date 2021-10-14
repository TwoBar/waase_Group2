import json


def ListUser(options):
    """
    :param options: A dictionary containing all the paramters for the Operations
        options["id"]: ID of the user

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "id": "<int64>",
        "name": "<string>",
        "tag": "<string>",
    }), 200



