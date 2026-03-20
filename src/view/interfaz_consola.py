import sys
sys.path.append("src")
from model import logica_ahorro

def pedir_float(mensaje):
    """Solicita un número decimal al usuario."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")


def pedir_int(mensaje):
    """Solicita un número entero al usuario."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("ERROR: Debe ingresar un número entero válido.")


def preguntar_abono():
    """Pregunta si desea agregar abono extra y retorna sus valores."""
    opcion_abono = input("¿Desea agregar un abono extra? (si/no): ").strip().lower()
    if opcion_abono == "si":
        abono_extra = pedir_float("Ingrese el valor del abono extra: ")
        mes_del_abono = pedir_int("Ingrese el mes en que realizará el abono: ")
        return abono_extra, mes_del_abono
    return 0, None


def mostrar_menu():
    """Imprime las opciones disponibles del programa."""
    print("\n====== AHORRO PROGRAMADO ======")
    print("1. Calcular cuota mensual")
    print("2. Calcular total intereses")
    print("3. Salir")


def pedir_datos_ahorro():
    """Solicita al usuario todos los datos necesarios para el cálculo."""
    print("\nIngrese los datos del ahorro")
    meta_ahorro = pedir_float("Meta de ahorro: ")
    tasa_interes = pedir_float("Tasa de interés (ej: 1 para 1%, 0.75 para 0.75%): ") / 100
    plazo = pedir_int("Plazo en meses: ")
    abono_extra, mes_del_abono = preguntar_abono()
    return meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono


def ejecutar_opcion(opcion_menu, meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono):
    """Llama a la lógica correspondiente según la opción del menú y muestra el resultado."""
    print("\n===== RESULTADO =====")
    if opcion_menu == "1":
        cuota = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)
        print(f"Cuota mensual necesaria: ${cuota:,.2f}")
    elif opcion_menu == "2":
        total_interes = logica_ahorro.calcular_total_interes(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)
        print(f"Total intereses generados: ${total_interes:,.2f}")


def interfaz():
    """Coordina el flujo principal del programa: menú, entrada y ejecución."""
    while True:
        mostrar_menu()
        opcion_menu = input("Seleccione una opción: ").strip()

        if opcion_menu == "3":
            print("Saliendo del programa...")
            break

        if opcion_menu not in ["1", "2"]:
            print("Opción inválida.")
            continue

        meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono = pedir_datos_ahorro()

        try:
            ejecutar_opcion(opcion_menu, meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)
        except Exception as error:
            print("\nSe produjo un error:")
            print(error)


if __name__ == "__main__":
    interfaz()
