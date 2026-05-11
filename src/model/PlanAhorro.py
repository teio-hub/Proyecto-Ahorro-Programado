class PlanAhorro:

    def __init__(self, id_plan, cedula, meta, tasa_interes, plazo, cuota_mensual, fecha_creacion):
        self.id_plan = id_plan
        self.cedula = cedula
        self.meta = meta
        self.tasa_interes = tasa_interes
        self.plazo = plazo
        self.cuota_mensual = cuota_mensual
        self.fecha_creacion = fecha_creacion

    def is_equal(self, otro):
        return (self.cedula == otro.cedula and
                self.meta == otro.meta and
                self.tasa_interes == otro.tasa_interes and
                self.plazo == otro.plazo and
                self.cuota_mensual == otro.cuota_mensual)