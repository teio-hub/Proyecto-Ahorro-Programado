create table if not exists usuarios (
  cedula varchar(20) primary key not null,
  nombre text not null,
  apellido text not null,
  telefono varchar(20),
  correo text,
  direccion text not null
);