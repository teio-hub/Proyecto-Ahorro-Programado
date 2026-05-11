create table if not exists abonos (
  id_abono serial primary key not null,
  id_plan int not null,
  mes_abono int not null,
  valor_abono decimal not null,
  nueva_cuota decimal not null
);