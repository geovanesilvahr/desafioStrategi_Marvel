from flask import render_template, Blueprint

app_heroi = Blueprint('heroi', __name__, url_prefix='/', template_folder='templates')

@app_heroi.route('/')
def heroi_index():
    return render_template('admin/index.html')