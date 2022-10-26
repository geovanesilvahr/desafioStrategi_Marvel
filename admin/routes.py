from flask import render_template, Blueprint
from server.apiMarvel import herois

app_heroi = Blueprint('heroi', __name__, url_prefix='/', template_folder='templates')

@app_heroi.route('/')
def heroi_index():

    lista_herois = herois()

    return render_template('admin/index.html', lista_herois=lista_herois)
