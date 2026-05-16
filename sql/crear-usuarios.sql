create table if not exists usuarios (
  cedula varchar(20) primary key not null,
  nombre text not null,
  apellido text not null,
  telefono varchar(20),
  correo text,
  direccion text not null
);

INSERT INTO usuarios (cedula, nombre, apellido, telefono, correo, direccion)
VALUES ('123456', 'Ana', 'García', '3001234567', 'ana@correo.com', 'Calle 10 #20-30, Medellín');

INSERT INTO usuarios (cedula, nombre, apellido, telefono, correo, direccion)
VALUES ('654321', 'Carlos', 'López', '3107654321', 'carlos@correo.com', 'Carrera 5 #15-20, Medellín');