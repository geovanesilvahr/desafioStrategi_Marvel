from flask import Flask, Blueprint
from flask_restplus import Api

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/doc', title="Desafio STRATEGI Marvel API")
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
    
        self.heroi_ns = self.heroi_ns()    

    def heroi_ns(self):
        return self.api.namespace(name="Herois", description='Herois related operations', path='/')

    def run(self):
        self.app.run(debug=True)

server = Server()
