from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf import CSRFProtect

app=Flask(__name__)

csrf= CSRFProtect()
db=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    
    # print(request.method)
    # print(request.form['usuario'])
    # print(request.form['password'])
    # CSRF (Cross-site Request Forgery): Solicitud de falsificacion entre sitios.
    if request.method=='POST':
        #print(request.form['usuario'])
        #print(request.form['password'])
        if request.form['usuario']=='admin' and request.form['password']=='123':
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/libros')
def listar_libros():
    try:
        cursor=db.connection.cursor()
        sql='SELECT isbn, titulo, anoedicion FROM libro ORDER BY titulo ASC'
        cursor.execute(sql)
        data=cursor.fetchall()
        print(data)
        return "OK"
    except Exception as ex:
        raise Exception(ex)

def pagina_no_encontrada(error):
    return render_template('errores/404.html'),404

def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    return app
    