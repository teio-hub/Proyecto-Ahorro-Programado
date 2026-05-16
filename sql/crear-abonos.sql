create table if not exists abonos (
  id_abono serial primary key not null,
  id_plan int not null,
  mes_abono int not null,
  valor_abono decimal not null,
  nueva_cuota decimal not null
);

INSERT INTO abonos (id_plan, mes_abono, valor_abono, nueva_cuota)
VALUES (1, 3, 500000, 215000.00);

INSERT INTO abonos (id_plan, mes_abono, valor_abono, nueva_cuota)
VALUES (2, 1, 200000, 380000.00);