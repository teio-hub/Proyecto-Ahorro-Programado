class Abono:

    def __init__(self, id_abono, id_plan, mes_abono, valor_abono, nueva_cuota):
        self.id_abono = id_abono
        self.id_plan = id_plan
        self.mes_abono = mes_abono
        self.valor_abono = valor_abono
        self.nueva_cuota = nueva_cuota

    def is_equal(self, otro):
        return (self.id_plan == otro.id_plan and
                self.mes_abono == otro.mes_abono and
                self.valor_abono == otro.valor_abono and
                self.nueva_cuota == otro.nueva_cuota)