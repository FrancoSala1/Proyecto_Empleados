-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS gestion_empleados;

-- Usar la base de datos
USE gestion_empleados;

-- Crear tabla Tipo_empleado
CREATE TABLE IF NOT EXISTS Tipo_empleado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(20) NOT NULL,
    detalle TEXT
);

-- Crear tabla Departamento
CREATE TABLE IF NOT EXISTS Departamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    telefono VARCHAR(15) NOT NULL
);

-- Crear tabla Empleados
CREATE TABLE IF NOT EXISTS Empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    direccion VARCHAR(20) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    correo VARCHAR(25) NOT NULL,
    fecha_inicio DATE NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    id_tipo INT,
    rut VARCHAR(20) NOT NULL,
    contraseña VARCHAR(30) NOT NULL,
    FOREIGN KEY (id_tipo) REFERENCES Tipo_empleado(id)
);

-- Crear tabla Proyecto
CREATE TABLE IF NOT EXISTS Proyecto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE
);

-- Crear tabla Proyecto_empleado
CREATE TABLE IF NOT EXISTS Proyecto_empleado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_proyecto INT,
    id_empleado INT,
    FOREIGN KEY (id_proyecto) REFERENCES Proyecto(id),
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id)
);

-- Crear tabla Departamento_empleado
CREATE TABLE IF NOT EXISTS Departamento_empleado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_depto INT,
    id_empleado INT,
    FOREIGN KEY (id_depto) REFERENCES Departamento(id),
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id)
);

-- Crear tabla Registro_tiempo
CREATE TABLE IF NOT EXISTS Registro_tiempo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    tareas TEXT,
    id_asignacion INT,
    observacion TEXT,
    FOREIGN KEY (id_asignacion) REFERENCES Proyecto_empleado(id)
);
