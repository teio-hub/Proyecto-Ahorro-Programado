TASA_MAXIMA = 0  # Se valida solo que no sea negativa


class MetaInvalida(Exception):
    """
    Excepción personalizada para indicar que la meta de ahorro
    es menor o igual a cero.
    """
    def __init__(self, meta_ahorro):
        """
        Para usar esta excepción, indique la meta recibida como parámetro.
        """
        super().__init__(
            f"La meta de ahorro debe ser mayor que cero. "
            f"Se recibió meta_ahorro={meta_ahorro}."
        )


class PlazoInvalido(Exception):
    """
    Excepción personalizada para indicar que el plazo
    es cero o negativo.
    """
    def __init__(self, plazo):
        """
        Para usar esta excepción, indique el plazo recibido como parámetro.
        """
        super().__init__(
            f"El plazo debe ser mayor que cero. "
            f"Se recibió plazo={plazo}."
        )


class InteresInvalido(Exception):
    """
    Excepción personalizada para indicar que la tasa de interés
    es negativa.
    """
    def __init__(self, tasa_interes):
        """
        Para usar esta excepción, indique la tasa recibida como parámetro.
        """
        super().__init__(
            f"La tasa de interés no puede ser negativa. "
            f"Se recibió tasa_interes={tasa_interes}."
        )


class MesAbonoInvalido(Exception):
    """
    Excepción personalizada para indicar que el mes del abono
    está fuera del rango del plazo.
    """
    def __init__(self, mes_del_abono, plazo):
        """
        Para usar esta excepción, indique el mes del abono y el plazo como parámetros.
        """
        super().__init__(
            f"El mes del abono debe estar entre 1 y {plazo}. "
            f"Se recibió mes_del_abono={mes_del_abono}."
        )


def _validar_parametros(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono):
    """Valida que los parámetros de entrada sean correctos antes del cálculo."""
    if meta_ahorro <= 0:
        raise MetaInvalida(meta_ahorro)

    if plazo <= 0:
        raise PlazoInvalido(plazo)

    if tasa_interes < 0:
        raise InteresInvalido(tasa_interes)

    if abono_extra > 0 and mes_del_abono is not None:
        if mes_del_abono < 1 or mes_del_abono > plazo:
            raise MesAbonoInvalido(mes_del_abono, plazo)


def calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra=0, mes_del_abono=None):
    """
    Calcula la cuota periódica necesaria para alcanzar una meta de ahorro.
    Utiliza la fórmula de anualidad ordinaria. Permite aplicar un abono
    adicional en un mes específico, lo que reduce la cuota mensual.

    Parametros
    ----------
    meta_ahorro : float
        Cantidad objetivo a ahorrar.
    tasa_interes : float
        Tasa de interés periódica en decimal.
    plazo : int
        Número de períodos en meses.
    abono_extra : float, optional
        Abono adicional. Por defecto es 0.
    mes_del_abono : int, optional
        Mes en que se realiza el abono. Por defecto es None.

    Returns
    -------
    float
        Cuota periódica necesaria para alcanzar la meta.

    Raises
    ------
    MetaInvalida
        Si meta_ahorro es menor o igual a cero.
    PlazoInvalido
        Si plazo es cero o negativo.
    InteresInvalido
        Si tasa_interes es negativa.
    MesAbonoInvalido
        Si mes_del_abono está fuera del rango [1, plazo].
    """
    _validar_parametros(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

    if abono_extra > 0 and mes_del_abono is not None:
        meta_ahorro = meta_ahorro - abono_extra

    if tasa_interes == 0:
        return meta_ahorro / plazo

    return meta_ahorro * (tasa_interes / ((1 + tasa_interes) ** plazo - 1))


def calcular_total_interes(meta_ahorro, tasa_interes, plazo, abono_extra=0, mes_del_abono=None):
    """
    Calcula el total de intereses generados durante el período de ahorro.

    Parametros
    ----------
    meta_ahorro : float
        Cantidad objetivo a ahorrar.
    tasa_interes : float
        Tasa de interés periódica en decimal.
    plazo : int
        Número de períodos en meses.
    abono_extra : float, optional
        Abono adicional. Por defecto es 0.
    mes_del_abono : int, optional
        Mes en que se realiza el abono. Por defecto es None.

    Returns
    -------
    float
        Total de intereses generados.
    """
    cuota = calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)
    meta_efectiva = meta_ahorro - abono_extra if (abono_extra > 0 and mes_del_abono is not None) else meta_ahorro
    return meta_efectiva - cuota * plazo
