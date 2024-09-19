from flask import Blueprint, request, jsonify

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/search", methods=['GET'])
def search_user():
    args = request.args
    return jsonify(args), 200