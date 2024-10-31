-- Insertar tipos de empleados
INSERT INTO Tipo_empleado (tipo, detalle) VALUES
('Administrativo', 'Empleado que realiza tareas administrativas.'),
('Técnico', 'Empleado que trabaja en soporte técnico.'),
('Gerente', 'Empleado que supervisa varios departamentos.');

-- Insertar departamentos
INSERT INTO Departamento (nombre, telefono) VALUES
('Recursos Humanos', '222334455'),
('Desarrollo', '233445566'),
('Marketing', '244556677');

-- Insertar empleados
INSERT INTO Empleados (nombre, direccion, telefono, correo, fecha_inicio, salario, id_tipo, rut, contraseña) VALUES
('Juan Pérez', 'Calle Falsa 123', '98765432', 'juan.perez@example.com', '2023-01-15', 3000.00, 1, '12.345.678-9', 'contraseña123'),
('Ana Gómez', 'Avenida Siempre Viva 742', '98765433', 'ana.gomez@example.com', '2023-02-01', 4500.00, 2, '23.456.789-0', 'contraseña456'),
('Carlos López', 'Plaza Mayor 456', '98765434', 'carlos.lopez@example.com', '2023-03-10', 6000.00, 3, '34.567.890-1', 'contraseña789');

-- Insertar proyectos
INSERT INTO Proyecto (nombre, descripcion, fecha_inicio, fecha_fin) VALUES
('Proyecto A', 'Descripción del Proyecto A', '2023-03-01', '2023-06-30'),
('Proyecto B', 'Descripción del Proyecto B', '2023-04-15', '2023-09-15'),
('Proyecto C', 'Descripción del Proyecto C', '2023-05-20', '2023-08-20');

-- Insertar asignaciones de empleados a proyectos
INSERT INTO Proyecto_empleado (id_proyecto, id_empleado) VALUES
(1, 1),
(1, 2),
(2, 2),
(2, 3),
(3, 1);

-- Insertar asignaciones de empleados a departamentos
INSERT INTO Departamento_empleado (id_depto, id_empleado) VALUES
(1, 1),
(2, 2),
(3, 3),
(2, 1); -- Juan también trabaja en Desarrollo

-- Insertar registros de tiempo
INSERT INTO Registro_tiempo (fecha, tareas, id_asignacion, observacion) VALUES
('2023-03-05', 'Tarea A1', 1, 'Tarea completada con éxito.'),
('2023-04-10', 'Tarea B1', 2, 'Problemas menores solucionados.'),
('2023-05-25', 'Tarea C1', 3, 'Tarea en progreso.'),
('2023-06-01', 'Tarea A2', 1, 'Segunda parte de la tarea.'),
('2023-07-20', 'Tarea B2', 4, 'Tarea finalizada.');

-- Notas sobre ID:
-- Los ID en las tablas (1, 2, 3, etc.) son auto-incrementales. 
-- Esto significa que se generarán automáticamente por la base de datos al insertar nuevos registros.