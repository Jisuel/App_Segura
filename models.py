from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base, UserMixin):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(50), unique=True, nullable=False)
    correo_electronico = Column(String(100), unique=True, nullable=False)
    contraseña_hash = Column(Text, nullable=False)
    contraseñas = relationship("Contraseña", back_populates="usuario")

    def __repr__(self):
        return f"<User(nombre_usuario='{self.nombre_usuario}', correo_electronico='{self.correo_electronico}')>"

    def set_password(self, password):
        self.contraseña_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contraseña_hash, password)
    
class Contraseña(Base):
    __tablename__ = 'contraseñas'
    
    id = Column(Integer, primary_key=True)
    nombre_servicio = Column(String(100), nullable=False)
    contraseña_hash = Column(Text, nullable=False)
    notas = Column(Text, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship("User", back_populates="contraseñas")

    def __repr__(self):
        return f"<Contraseña(sitio='{self.nombre_servicio}', usuario_id='{self.usuario_id}')>"
    
    def set_password(self, password):
        self.contraseña_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contraseña_hash, password)

