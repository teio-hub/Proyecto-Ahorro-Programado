create table if not exists planes_ahorro (
  id_plan serial primary key not null,
  cedula varchar(20) not null,
  meta decimal not null,
  tasa_interes decimal not null,
  plazo int not null,
  cuota_mensual decimal not null,
  fecha_creacion date not null
);

INSERT INTO planes_ahorro (cedula, meta, tasa_interes, plazo, cuota_mensual, fecha_creacion)
VALUES ('123456', 10000000, 0.01, 36, 232062.38, '2026-01-01');

INSERT INTO planes_ahorro (cedula, meta, tasa_interes, plazo, cuota_mensual, fecha_creacion)
VALUES ('654321', 5000000, 0.0075, 12, 399757.38, '2026-01-01');