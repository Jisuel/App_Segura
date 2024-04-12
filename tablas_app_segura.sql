CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    correo_electronico VARCHAR(100) UNIQUE NOT NULL,
    contraseña_hash TEXT NOT NULL, -- Almacenar el hash de la contraseña
    autenticacion_dos_factores BOOLEAN DEFAULT FALSE, -- Estado de autenticación de dos factores
    es_administrador BOOLEAN DEFAULT FALSE -- Indicador de si el usuario es administrador
);

CREATE TABLE contraseñas (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES Usuarios(id) ON DELETE CASCADE,
    nombre_servicio VARCHAR(100) NOT NULL,
    contraseña_hash TEXT NOT NULL, -- Almacenar el hash de la contraseña
    notas TEXT,
    CONSTRAINT fk_usuario_id FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
);
