from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from flask_restful import Api


from config import Config

db = MongoAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    api = Api(app, prefix="")

    from app.classes import Keys, Funds, Common
    from .user import user_blueprint
    from .loan import loan_blueprint

    api.add_resource(Keys, '/keys')
    api.add_resource(Funds, '/funds')
    api.add_resource(Common, '/common')

    app.register_blueprint(loan_blueprint, url_prefix='/loan')
    app.register_blueprint(user_blueprint, url_prefix='/user')

    return app
