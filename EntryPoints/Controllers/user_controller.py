from flask import make_response, jsonify, request, Blueprint

from Models import user_model

app = Blueprint('user_controller', __name__, url_prefix='/api/v1')


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_model.get_user_by_id(user_id)
    if user:
        return jsonify(user)
    else:
        return make_response("User not found", 404)


@app.route('/user', methods=['POST'])
def create_user():
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)

    data = request.json
    if 'username' not in data or 'role' not in data:
        return make_response("Missing required fields", 400)

    try:
        new_user = user_model.create_user(**data)
        return jsonify(new_user), 201
    except Exception as e:
        return make_response(f"Error creating user: {e}", 500)


@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = user_model.update_user_by_id(user_id, **data)
    if user:
        return jsonify(user)
    else:
        return make_response("User not found", 404)


@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_model.delete_user_by_id(user_id):

        return make_response("User deleted", 200)
    else:
        return make_response("User not found", 404)
