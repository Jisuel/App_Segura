from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Contraseña

app = Flask(__name__)
app.secret_key = ''  # Clave secreta requerida por Flask-Login

# Formato de la URL de conexión para PostgreSQL
# postgresql://<usuario>:<contraseña>@<host>:<puerto>/<nombre_base_de_datos>

DATABASE_URL = ''
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Configuración Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('perfil'))  # Redirecciona al usuario si ya está autenticado

    # Lógica para procesar el formulario de inicio de sesión

    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']

        user = session.query(User).filter_by(nombre_usuario=nombre).first()

        if user and user.check_password(contraseña):  # Validación de contraseña
            login_user(user)
            return redirect(url_for('perfil'))
        else:
            mensaje = "** Usuario no encontrado o contraseña incorrecta **"
            flash(mensaje)

    return render_template('login.html')


@app.route('/index.html')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))  # Redirecciona al usuario al cerrar sesión

@app.route('/perfil.html', methods=['GET', 'POST'])
@login_required
def perfil():
    nombre_usuario = current_user.nombre_usuario
    correo_electronico = current_user.correo_electronico

    # Obtener las contraseñas del usuario actual
    contraseñas = session.query(Contraseña).filter(Contraseña.usuario_id == current_user.id).all()

    return render_template('perfil.html', nombre_usuario=nombre_usuario, correo_electronico=correo_electronico, contraseñas=contraseñas)

@app.route('/registrar_contraseña.html', methods=['GET' , 'POST'])
@login_required
def registrar_contraseña():
    if request.method == 'POST':
        nombre_servicio = request.form['nombre_servicio']
        contraseña_hash = request.form['contraseña']
        notas = request.form['notas']

        nueva_contraseña = Contraseña(nombre_servicio=nombre_servicio, notas=notas, usuario=current_user, contraseña_hash=contraseña_hash)
        
        session.add(nueva_contraseña)
        session.commit()

        mensaje = '¡Contraseña agregada correctamente!'
        flash(mensaje)
    
    return render_template('registrar_contraseña.html')

@app.route('/registro.html', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        correo_electronico = request.form['correo_electronico']
        contraseña = request.form['contraseña']

        # Verificar si el nombre de usuario o correo electrónico ya están en uso
        if session.query(User).filter((User.nombre_usuario == nombre_usuario) | (User.correo_electronico == correo_electronico)).first():
            mensaje1 = '** El nombre de usuario o correo electrónico ya están en uso **'
            flash(mensaje1)
            return redirect(url_for('registro'))  # Redirigir de nuevo al formulario de registro
        
        # Crear un nuevo usuario
        nuevo_usuario = User(nombre_usuario=nombre_usuario, correo_electronico=correo_electronico)
        nuevo_usuario.set_password(contraseña)  # Hash de la contraseña

        # Guardar el nuevo usuario en la base de datos
        session.add(nuevo_usuario)
        session.commit()

        mensaje = '¡Usuario registrado correctamente!'
        flash(mensaje)
    
    return render_template('registro.html')


if __name__ == "__main__":
    app.run(debug=True)
