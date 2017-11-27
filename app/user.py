from flask import Blueprint, request, jsonify

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/')
def root():
    return 'Hello, user!'


@user_blueprint.route('/login', methods=['POST'])
def login():
    m = request.values["message"]
    return jsonify(m)


@user_blueprint.route('/signup', methods=['POST'])
def signup():
    m = '123123' if request.values['userNo'] is None else request.values['userNo']
    return jsonify(m)


@user_blueprint.route('/already', methods=['GET'])
def already():
    m = '123123' if request.values['userNo'] is None else request.values['userNo']
    return jsonify(m)
