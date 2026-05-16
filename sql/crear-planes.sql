create table if not exists planes_ahorro (
  id_plan serial primary key not null,
  cedula varchar(20) not null,
  meta decimal not null,
  tasa_interes decimal not null,
  plazo int not null,
  cuota_mensual decimal not null,
  fecha_creacion date not null
);

