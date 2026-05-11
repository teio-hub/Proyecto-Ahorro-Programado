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
            float(self.meta) == float(otro.meta) and
            round(float(self.tasa_interes), 4) == round(float(otro.tasa_interes), 4) and
            int(self.plazo) == int(otro.plazo) and
            round(float(self.cuota_mensual), 2) == round(float(otro.cuota_mensual), 2))