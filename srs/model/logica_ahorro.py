"""
 ===== logica_ahorro.py =====
 CLAVE 1 APLICADA: Nombres que revelan intención
   - "meta"      → "meta_ahorro"
   - "interes"   → "tasa_interes"
   - "abono"     → "abono_extra"
   - "mes_abono" → "mes_del_abono"

 CLAVE 2 APLICADA: Funciones pequeñas con una sola responsabilidad
   - _validar_parametros() agrupa todas las validaciones
   - calcular_cuota() solo se encarga del cálculo
"""

class MetaInvalida(Exception):
    """Se dispara cuando la meta de ahorro es menor o igual a cero."""

class PlazoInvalido(Exception):
    """Se dispara cuando el plazo es cero o negativo."""

class InteresInvalido(Exception):
    """Se dispara cuando la tasa de interés es negativa."""

class MesAbonoInvalido(Exception):
    """Se dispara cuando el mes del abono está fuera del rango del plazo."""


def _validar_parametros(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono):
    """Valida que los parámetros de entrada sean correctos antes del cálculo."""
    if meta_ahorro <= 0:
        raise MetaInvalida(
            f"ERROR: La meta debe ser mayor que cero. "
            f"Se recibió meta_ahorro={meta_ahorro}. Ingrese un valor positivo."
        )
    if plazo <= 0:
        raise PlazoInvalido(
            f"ERROR: El plazo debe ser mayor que cero. "
            f"Se recibió plazo={plazo}. Ingrese un plazo de al menos 1 mes."
        )
    if tasa_interes < 0:
        raise InteresInvalido(
            f"ERROR: La tasa de interés no puede ser negativa. "
            f"Se recibió tasa_interes={tasa_interes}. Ingrese una tasa mayor o igual a cero."
        )
    if abono_extra > 0 and mes_del_abono is not None:
        if mes_del_abono < 1 or mes_del_abono > plazo:
            raise MesAbonoInvalido(
                f"ERROR: El mes del abono no es válido. "
                f"Se recibió mes_del_abono={mes_del_abono} con plazo={plazo}. "
                f"El mes debe estar entre 1 y {plazo}."
            )


def calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra=0, mes_del_abono=None):
    """
    Calcula la cuota periódica necesaria para alcanzar una meta de ahorro.

    Utiliza la fórmula de anualidad ordinaria. Permite aplicar un abono
    adicional en un mes específico, lo que reduce la cuota mensual.

    Args:
        meta_ahorro (float): Cantidad objetivo a ahorrar.
        tasa_interes (float): Tasa de interés periódica en decimal.
        plazo (int): Número de períodos en meses.
        abono_extra (float, optional): Abono adicional. Por defecto es 0.
        mes_del_abono (int, optional): Mes del abono. Por defecto es None.

    Returns:
        float: Cuota periódica necesaria para alcanzar la meta.

    Raises:
        MetaInvalida: Si meta_ahorro es menor o igual a cero.
        PlazoInvalido: Si plazo es cero o negativo.
        InteresInvalido: Si tasa_interes es negativa.
        MesAbonoInvalido: Si mes_del_abono está fuera del rango [1, plazo].
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

    Args:
        meta_ahorro (float): Cantidad objetivo a ahorrar.
        tasa_interes (float): Tasa de interés periódica en decimal.
        plazo (int): Número de períodos en meses.
        abono_extra (float, optional): Abono adicional. Por defecto es 0.
        mes_del_abono (int, optional): Mes del abono. Por defecto es None.

    Returns:
        float: Total de intereses generados.
    """
    cuota = calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)
    meta_efectiva = meta_ahorro - abono_extra if (abono_extra > 0 and mes_del_abono is not None) else meta_ahorro
    return meta_efectiva - cuota * plazo
