# CURSO INICIADO EL 14/11/2022
from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def index():
#     return "CodigoFacilito1234"

def index():
    # return "CodigoFacilito 14/11/2022! desde cero"
    # return render_template('index.html', titulo='Pagina principal')
    data = {
        'titulo': 'Pagina Main',
        'encabezado': 'Curso de FLASK'
    }
    return render_template('index.html', data=data)


@app.route('/hola')
def hola_mundo():
    return "Bienvenidos hola mundo"


if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True, port=5500)
