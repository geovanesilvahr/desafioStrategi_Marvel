from flask import render_template

from ma import ma
from db import db
from controllers.heroi import Heroi, HeroiList
from models.herois import HeroiModel

from server.instante import server

api = server.api
app = server.app
herois = HeroiModel
print(herois)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html', herois=herois) 

api.add_resource(Heroi, '/herois/<int:id>')
api.add_resource(HeroiList, '/herois')


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    server.run()
