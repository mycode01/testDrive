# app = Flask(__name__)
# api = Api(app, prefix="")
# app.config['MONGOALCHEMY_DATABASE'] = 'tdb'
# # tdb = MongoAlchemy(app)
#
#
# api.add_resource(Keys, '/keys')
# api.add_resource(Funds, '/funds')
# api.add_resource(Common, '/common')
# app.register_blueprint(loan_blueprint, url_prefix='/loan')
# app.register_blueprint(user_blueprint, url_prefix='/user')
from app import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)