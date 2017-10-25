from flask import Flask, jsonify
from flask_restful import  Api
from classes import Keys, Funds

app = Flask(__name__)
api = Api(app)


api.add_resource(Keys, '/keys')
api.add_resource(Funds, '/funds')

if __name__ == '__main__':
    app.run(debug=True)