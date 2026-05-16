import sys
sys.path.append("src")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
from controller.planes_controller import PlanesController
from model.PlanAhorro import PlanAhorro

Window.size = (600, 700)
Window.clearcolor = (0.15, 0.35, 0.2, 1)

class PlanesGUI(App):

    def build(self):
        self.title = "Ahorro Programado - Planes"
        main = BoxLayout(orientation='vertical', padding=40, spacing=20)

        main.add_widget(Label(
            text="[b]GESTIÓN DE PLANES DE AHORRO[/b]",
            markup=True, halign="center", size_hint_y=0.08
        ))

        main.add_widget(Label(
            text="Sección: Insertar, Buscar y Modificar planes\n"
                 "Ingrese los datos del plan y use los botones para cada acción.",
            halign="center", size_hint_y=0.08
        ))

        form = GridLayout(cols=2, spacing=10, size_hint_y=0.6)

        form.add_widget(Label(text="ID Plan (solo para buscar/modificar):"))
        self.in_id = TextInput(multiline=False, input_filter='int', hint_text="Ej: 1")
        form.add_widget(self.in_id)

        form.add_widget(Label(text="Cédula:"))
        self.in_cedula = TextInput(multiline=False, hint_text="Ej: 123456")
        form.add_widget(self.in_cedula)

        form.add_widget(Label(text="Meta ($):"))
        self.in_meta = TextInput(multiline=False, input_filter='float', hint_text="Ej: 10000000")
        form.add_widget(self.in_meta)

        form.add_widget(Label(text="Tasa de interés mensual (Ej: 0.01):"))
        self.in_tasa = TextInput(multiline=False, input_filter='float', hint_text="Ej: 0.01")
        form.add_widget(self.in_tasa)

        form.add_widget(Label(text="Plazo (meses):"))
        self.in_plazo = TextInput(multiline=False, input_filter='int', hint_text="Ej: 36")
        form.add_widget(self.in_plazo)

        form.add_widget(Label(text="Cuota mensual ($):"))
        self.in_cuota = TextInput(multiline=False, input_filter='float', hint_text="Ej: 232062.38")
        form.add_widget(self.in_cuota)

        form.add_widget(Label(text="Fecha creación (YYYY-MM-DD):"))
        self.in_fecha = TextInput(multiline=False, hint_text="Ej: 2026-01-01")
        form.add_widget(self.in_fecha)

        main.add_widget(form)

        botones = GridLayout(cols=3, spacing=10, size_hint_y=0.1)

        btn_insertar = Button(text="Insertar", background_color=(0.4, 0.75, 0.5, 1))
        btn_insertar.bind(on_press=self.insertar)
        botones.add_widget(btn_insertar)

        btn_buscar = Button(text="Buscar por ID", background_color=(0.3, 0.65, 0.45, 1))
        btn_buscar.bind(on_press=self.buscar)
        botones.add_widget(btn_buscar)

        btn_modificar = Button(text="Modificar", background_color=(0.5, 0.8, 0.55, 1))
        btn_modificar.bind(on_press=self.modificar)
        botones.add_widget(btn_modificar)

        main.add_widget(botones)

        self.resultado = Label(
            text="Esperando acción...",
            halign="center", color=(0.8, 0.8, 0.8, 1),
            size_hint_y=0.14
        )
        main.add_widget(self.resultado)

        Clock.schedule_once(lambda dt: self.mostrar_bienvenida(), 0.5)
        return main

    def mostrar_bienvenida(self):
        contenido = BoxLayout(orientation='vertical', padding=20, spacing=15)
        contenido.add_widget(Label(
            text="[b]BIENVENIDO A GESTIÓN DE PLANES DE AHORRO[/b]",
            markup=True, halign="center", size_hint_y=0.2
        ))
        contenido.add_widget(Label(
            text="Con esta aplicación puedes:\n\n"
                 "• Insertar: Llena todos los campos y presiona Insertar.\n"
                 "• Buscar: Ingresa el ID del plan y presiona Buscar por ID.\n"
                 "• Modificar: Busca el plan, cambia los datos y presiona Modificar.\n\n"
                 "El campo ID Plan solo es necesario para Buscar y Modificar.",
            halign="left", size_hint_y=0.6
        ))
        btn = Button(text="Continuar", size_hint_y=0.2, background_color=(0.4, 0.75, 0.5, 1))
        contenido.add_widget(btn)
        self.popup = Popup(title="Instrucciones", content=contenido, size_hint=(0.85, 0.6))
        btn.bind(on_press=self.popup.dismiss)
        self.popup.open()

    def mostrar_resultado(self, texto, color=(0.2, 1, 0.2, 1)):
        self.resultado.color = color
        self.resultado.text = texto

    def mostrar_error(self, mensaje):
        self.mostrar_resultado(
            f"ERROR: {mensaje}\n\n¿Necesitas ayuda? Consulta el README en:\ngithub.com/manolo-restrepo/Proyecto-Ahorro-Programado",
            color=(1, 0.3, 0.3, 1)
        )

    def insertar(self, instance):
        try:
            plan = PlanAhorro(
                id_plan=None,
                cedula=self.in_cedula.text,
                meta=float(self.in_meta.text),
                tasa_interes=float(self.in_tasa.text),
                plazo=int(self.in_plazo.text),
                cuota_mensual=float(self.in_cuota.text),
                fecha_creacion=self.in_fecha.text
            )
            PlanesController.insertar(plan)
            self.mostrar_resultado("¡Plan insertado correctamente!")
        except Exception as e:
            self.mostrar_error(str(e))

    def buscar(self, instance):
        try:
            id_plan = int(self.in_id.text)
            plan = PlanesController.buscar(id_plan)
            self.in_cedula.text = plan.cedula
            self.in_meta.text = str(plan.meta)
            self.in_tasa.text = str(plan.tasa_interes)
            self.in_plazo.text = str(plan.plazo)
            self.in_cuota.text = str(plan.cuota_mensual)
            self.in_fecha.text = str(plan.fecha_creacion)
            self.mostrar_resultado(f"Plan encontrado: ID {id_plan}")
        except Exception as e:
            self.mostrar_error(str(e))

    def modificar(self, instance):
        try:
            plan = PlanAhorro(
                id_plan=int(self.in_id.text),
                cedula=self.in_cedula.text,
                meta=float(self.in_meta.text),
                tasa_interes=float(self.in_tasa.text),
                plazo=int(self.in_plazo.text),
                cuota_mensual=float(self.in_cuota.text),
                fecha_creacion=self.in_fecha.text
            )
            PlanesController.modificar(plan)
            self.mostrar_resultado("¡Plan modificado correctamente!")
        except Exception as e:
            self.mostrar_error(str(e))

if __name__ == '__main__':
    PlanesGUI().run()