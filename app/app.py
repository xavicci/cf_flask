# CURSO INICIADO EL 14/11/2022

# HTTP HYperText Transfer Protocol
# GET, POST, PUT, DELETE
from flask import Flask, render_template, request

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


@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"Bienvenido {nombre}!"


@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1, valor2):
    return f"La suma es: {valor1+valor2}"


@app.route('/perfil/<nombre>/<int:edad>')
def perfil(nombre, edad):
    return f"Tu nombre es: {nombre} y edad {edad}"


@app.route('/lenguajes')
def fun_lenguajes():
    datos = {
        'hay_lenguajes': True,
        'data_Lenguajes': ['PHP', 'Python', 'Kotlin', 'SQL', 'Java', 'C#', 'JavaScript']
    }
    return render_template('lenguajes.html', data=datos)


@app.route('/contacto')
def contacto():
    data = {
        'titulo': 'Contacto',
        'encabezado': 'Bienvenidos a contacto'
    }
    return render_template('contacto.html', data=data)


@app.route('/datos')
def http_datos():
    return f'Estos son los datos: {request.args.get("item")}'


if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True, port=5500)
