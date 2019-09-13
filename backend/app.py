from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

# @app.route("/contacts", methods=['GET'])
# def get_all_contacts():
#     return create_response({"contacts": db.get('contacts')})

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('contacts', int(id)) is None:
        return create_response(status=404, message="No contact with this id exists")
    db.deleteById('contacts', int(id))
    return create_response(message="Contact deleted")


# TODO: Implement the rest of the API here!

@app.route("/contacts/<id>", methods=['GET'])
def get_contact_by_id(id):
    contact = db.getById('contacts', int(id))
    if (contact):
        return create_response(contact)
    else:
        return create_response(status=404, message="No contact with this id exists")

@app.route("/contacts", methods=['GET'])
def get_contacts():
    hobby = request.args.get('hobby')
    if (hobby):
        contacts = [c for c in db.get('contacts') if c['hobby'] == hobby]
        if (contacts):
            return create_response({"contacts": contacts})
        else:
            return create_response(status=404, message="No contact with this hobby exists")
    else:
        return create_response({"contacts": db.get('contacts')})

@app.route("/contacts", methods=['POST'])
def create_contact():
    parameters = ['name', 'nickname', 'hobby']
    missing_params = []
    body = request.get_json()
    new_person = {}

    for param in parameters:
        if (param in body):
            new_person[param] = body[param]
        else:
            missing_params.append(param)
    if (missing_params):
        return create_response(status=422, message="Missing {} parameters".format(', '.join(missing_params)))
    else:
        payload = db.create('contacts', new_person)
        return create_response(data=payload, status=201)

@app.route("/contacts/<id>", methods=['PUT'])
def update_contact(id):
    params = ['name', 'hobby']
    body = request.get_json()
    updates = {}
    if (db.getById('contacts', int(id))):
        for param in params:
            if (param in body):
                updates[param] = body[param]
        updated = db.updateById('contacts', int(id), updates)
        return create_response(data=updated)
    else:
        return create_response(status=404, message="No contact with this id exists")


"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
