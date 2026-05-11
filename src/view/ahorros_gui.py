import sys

sys.path.append("src")
try:
    from model import logica_ahorro
except ModuleNotFoundError:
    ""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Hacemos la ventana un poco más grande para que quepa todo
Window.size = (600, 650)

class AhorrosGUI(App):
    def build(self):
        self.title = "Ahorro Programado"

        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        header_label = Label(
            text="[b]APLICACIÓN DE AHORRO PROGRAMADO[/b]\nMódulo: Calculadora de Cuotas e Intereses",
            markup=True, size_hint_y=None, height=60, halign="center"
        )
        main_layout.add_widget(header_label)

        instructions = Label(
            text="Propósito: Calcule la cuota mensual necesaria o los intereses de su meta de ahorro.\n\n"
                 "Instrucciones:\n"
                 "1. Ingrese su Meta de ahorro ($) y el Plazo (meses) [Deben ser mayores a 0].\n"
                 "2. Ingrese la Tasa de interés mensual (Ej: escriba 1 para referirse al 1%).\n"
                 "3. Los campos de Abono Extra son opcionales. Déjelos en 0 si no aplican.",
            size_hint_y=None, height=120, halign="center"
        )
        main_layout.add_widget(instructions)

        form_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=220)

        form_layout.add_widget(Label(text="Meta de ahorro ($):", halign="right"))
        self.in_meta = TextInput(multiline=False, input_filter='float')
        form_layout.add_widget(self.in_meta)

        form_layout.add_widget(Label(text="Tasa de interés mensual (%):", halign="right"))
        self.in_tasa = TextInput(multiline=False, input_filter='float')
        form_layout.add_widget(self.in_tasa)

        form_layout.add_widget(Label(text="Plazo (meses):", halign="right"))
        self.in_plazo = TextInput(multiline=False, input_filter='int')
        form_layout.add_widget(self.in_plazo)

        form_layout.add_widget(Label(text="Abono extra ($) [Opcional]:", halign="right"))
        self.in_abono = TextInput(multiline=False, input_filter='float', text="0")
        form_layout.add_widget(self.in_abono)

        form_layout.add_widget(Label(text="Mes del abono [Opcional]:", halign="right"))
        self.in_mes_abono = TextInput(multiline=False, input_filter='int', text="0")
        form_layout.add_widget(self.in_mes_abono)

        main_layout.add_widget(form_layout)

        btn_layout = BoxLayout(spacing=15, size_hint_y=None, height=50)

        btn_cuota = Button(text="Calcular Cuota Mensual", background_color=(0.2, 0.6, 0.8, 1))
        btn_cuota.bind(on_press=self.btn_calcular_cuota)
        btn_layout.add_widget(btn_cuota)

        btn_interes = Button(text="Calcular Total Intereses", background_color=(0.2, 0.8, 0.4, 1))
        btn_interes.bind(on_press=self.btn_calcular_interes)
        btn_layout.add_widget(btn_interes)

        main_layout.add_widget(btn_layout)

        self.resultado_label = Label(
            text="Esperando datos...\nSi tiene dudas sobre cómo llenar el formulario, presione para ver sugerencias.",
            halign="center", color=(0.8, 0.8, 0.8, 1) # Gris claro
        )
        main_layout.add_widget(self.resultado_label)

        return main_layout

    def obtener_datos(self):
        try:
            meta = float(self.in_meta.text) if self.in_meta.text else 0.0
            # Dividimos la tasa por 100 porque en tu consola pides "1 para 1%"
            tasa = float(self.in_tasa.text) / 100 if self.in_tasa.text else 0.0
            plazo = int(self.in_plazo.text) if self.in_plazo.text else 0
            abono = float(self.in_abono.text) if self.in_abono.text else 0.0
            
            # Manejo del mes del abono (si es 0 o vacío, pasa a ser None para tu lógica)
            mes_abono_txt = self.in_mes_abono.text
            mes_abono = int(mes_abono_txt) if mes_abono_txt and int(mes_abono_txt) > 0 else None
            
            return meta, tasa, plazo, abono, mes_abono
        except ValueError:
            raise Exception("Debe ingresar números válidos. Revise que no haya letras.")

    def btn_calcular_cuota(self, instance):
        try:
            meta, tasa, plazo, abono, mes_abono = self.obtener_datos()
            cuota = logica_ahorro.calcular_cuota(meta, tasa, plazo, abono, mes_abono)
            self.resultado_label.color = (0.2, 1, 0.2, 1) # Verde
            self.resultado_label.text = f"¡Cálculo Exitoso!\nLa cuota mensual necesaria es de: ${cuota:,.2f}"
        except Exception as e:
            self.mostrar_error(e)

    def btn_calcular_interes(self, instance):
        try:
            meta, tasa, plazo, abono, mes_abono = self.obtener_datos()
            interes = logica_ahorro.calcular_total_interes(meta, tasa, plazo, abono, mes_abono)
            self.resultado_label.color = (0.2, 1, 0.2, 1) # Verde
            self.resultado_label.text = f"¡Cálculo Exitoso!\nEl total de intereses generados será de: ${interes:,.2f}"
        except Exception as e:
            self.mostrar_error(e)

    def mostrar_error(self, excepcion):
        self.resultado_label.color = (1, 0.3, 0.3, 1) # Rojo
        mensaje = (
            f"ERROR: {str(excepcion)}\n\n"
            "Ayuda"
        )
        self.resultado_label.text = mensaje

if __name__ == '__main__':
    AhorrosGUI().run()
