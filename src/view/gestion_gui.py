import sys
sys.path.append("src")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.clock import Clock
from kivy.core.window import Window
from controller.planes_controller import PlanesController
from controller.usuarios_controller import UsuariosController
from controller.abonos_controller import AbonosController
from model.PlanAhorro import PlanAhorro
from model.Usuario import Usuario
from model.Abono import Abono

Window.size = (650, 750)
Window.clearcolor = (0.15, 0.35, 0.2, 1)


class AhorroApp(App):
    """Aplicación principal de Ahorro Programado.

    Contiene tres pestañas: Planes, Usuarios y Abonos.
    Cada pestaña permite insertar, buscar y modificar registros en la base de datos.
    """

    def build(self):
        """Construye la interfaz principal con pestañas.

        Returns
        -------
        TabbedPanel
            Panel con las pestañas de Planes, Usuarios y Abonos.
        """
        self.title = "Ahorro Programado"
        panel = TabbedPanel(do_default_tab=False)

        tab_planes = TabbedPanelItem(text="Planes")
        tab_planes.content = self.build_planes()
        panel.add_widget(tab_planes)

        tab_usuarios = TabbedPanelItem(text="Usuarios")
        tab_usuarios.content = self.build_usuarios()
        panel.add_widget(tab_usuarios)

        tab_abonos = TabbedPanelItem(text="Abonos")
        tab_abonos.content = self.build_abonos()
        panel.add_widget(tab_abonos)

        Clock.schedule_once(lambda dt: self.mostrar_bienvenida(), 0.5)
        return panel

    # ─────────────────────────────────────────
    # PLANES
    # ─────────────────────────────────────────
    def build_planes(self):
        """Construye el formulario de gestión de planes de ahorro.

        Returns
        -------
        BoxLayout
            Layout con los campos y botones de la pestaña Planes.
        """
        main = BoxLayout(orientation='vertical', padding=30, spacing=15)

        main.add_widget(Label(text="[b]GESTIÓN DE PLANES DE AHORRO[/b]",
                              markup=True, halign="center", size_hint_y=0.07))
        main.add_widget(Label(text="Ingrese los datos del plan y use los botones.",
                              halign="center", size_hint_y=0.06))

        form = GridLayout(cols=2, spacing=8, size_hint_y=0.6)
        form.add_widget(Label(text="ID Plan (buscar/modificar):"))
        self.p_id = TextInput(multiline=False, input_filter='int', hint_text="Ej: 1")
        form.add_widget(self.p_id)

        form.add_widget(Label(text="Cédula:"))
        self.p_cedula = TextInput(multiline=False, hint_text="Ej: 123456")
        form.add_widget(self.p_cedula)

        form.add_widget(Label(text="Meta ($):"))
        self.p_meta = TextInput(multiline=False, input_filter='float', hint_text="Ej: 10000000")
        form.add_widget(self.p_meta)

        form.add_widget(Label(text="Tasa de interés mensual:"))
        self.p_tasa = TextInput(multiline=False, input_filter='float', hint_text="Ej: 0.01")
        form.add_widget(self.p_tasa)

        form.add_widget(Label(text="Plazo (meses):"))
        self.p_plazo = TextInput(multiline=False, input_filter='int', hint_text="Ej: 36")
        form.add_widget(self.p_plazo)

        form.add_widget(Label(text="Cuota mensual ($):"))
        self.p_cuota = TextInput(multiline=False, input_filter='float', hint_text="Ej: 232062.38")
        form.add_widget(self.p_cuota)

        form.add_widget(Label(text="Fecha creación (YYYY-MM-DD):"))
        self.p_fecha = TextInput(multiline=False, hint_text="Ej: 2026-01-01")
        form.add_widget(self.p_fecha)

        main.add_widget(form)

        botones = GridLayout(cols=3, spacing=8, size_hint_y=0.1)
        b1 = Button(text="Insertar", background_color=(0.4, 0.75, 0.5, 1))
        b1.bind(on_press=self.planes_insertar)
        botones.add_widget(b1)
        b2 = Button(text="Buscar por ID", background_color=(0.3, 0.65, 0.45, 1))
        b2.bind(on_press=self.planes_buscar)
        botones.add_widget(b2)
        b3 = Button(text="Modificar", background_color=(0.5, 0.8, 0.55, 1))
        b3.bind(on_press=self.planes_modificar)
        botones.add_widget(b3)
        main.add_widget(botones)

        self.p_resultado = Label(text="Esperando acción...", halign="center",
                                 color=(0.8, 0.8, 0.8, 1), size_hint_y=0.17)
        main.add_widget(self.p_resultado)
        return main

    def planes_insertar(self, instance):
        """Inserta un nuevo plan de ahorro en la base de datos.

        Parameters
        ----------
        instance : Button
            Botón que disparó el evento.
        """
        try:
            plan = PlanAhorro(id_plan=None, cedula=self.p_cedula.text,
                              meta=float(self.p_meta.text), tasa_interes=float(self.p_tasa.text),
                              plazo=int(self.p_plazo.text), cuota_mensual=float(self.p_cuota.text),
                              fecha_creacion=self.p_fecha.text)
            PlanesController.insertar(plan)
            self.p_resultado.color = (0.2, 1, 0.2, 1)
            self.p_resultado.text = "¡Plan insertado correctamente!"
        except Exception as e:
            self.p_resultado.color = (1, 0.3, 0.3, 1)
            self.p_resultado.text = f"ERROR: {str(e)}\n\n¿Necesitas ayuda? Consulta el README en:\ngithub.com/manolo-restrepo/Proyecto-Ahorro-Programado"

    def planes_buscar(self, instance):
        """Busca un plan de ahorro por ID y rellena los campos del formulario.

        Parameters
        ----------
        instance : Button
            Botón que disparó el evento.
        """
        try:
            plan = PlanesController.buscar(int(self.p_id.text))
            self.p_cedula.text = plan.cedula
            self.p_meta.text = str(plan.meta)
            self.p_tasa.text = str(plan.tasa_interes)
            self.p_plazo.text = str(plan.plazo)
            self.p_cuota.text = str(plan.cuota_mensual)
            self.p_fecha.text = str(plan.fecha_creacion)
            self.p_resultado.color = (0.2, 1, 0.2, 1)
            self.p_resultado.text = f"Plan encontrado: ID {self.p_id.text}"
        except Exception as e:
            self.p_resultado.color = (1, 0.3, 0.3, 1)
            self.p_resultado.text = f"ERROR: {str(e)}\n\n¿Necesitas ayuda? Consulta el README en:\ngithub.com/manolo-restrepo/Proyecto-Ahorro-Programado"

    def planes_modificar(self, instance):
        """Modifica un plan de ahorro existente en la base de datos.

        Parameters
        ----------
        instance : Button
            Botón que disparó el evento.
        """
        try:
            plan = PlanAhorro(id_plan=int(self.p_id.text), cedula=self.p_cedula.text,
                              meta=float(self.p_meta.text), tasa_interes=float(self.p_tasa.text),
                              plazo=int(self.p_plazo.text), cuota_mensual=float(self.p_cuota.text),
                              fecha_creacion=self.p_fecha.text)
            PlanesController.modificar(plan)
            self.p_resultado.color = (0.2, 1, 0.2, 1)
            self.p_resultado.text = "¡Plan modificado correctamente!"
        except Exception as e:
            self.p_resultado.color = (1, 0.3, 0.3, 1)
            self.p_resultado.text = f"ERROR: {str(e)}\n\n¿Necesitas ayuda? Consulta el README en:\ngithub.com/manolo-restrepo/Proyecto-Ahorro-Programado"

    # ─────────────────────────────────────────
    # USUARIOS
    # ─────────────────────────────────────────
    def build_usuarios(self):
        """Construye el formulario de gestión de usuarios.

        Returns
        -------
        BoxLayout
            Layout con los campos y botones de la pestaña Usuarios.
        """
        main = BoxLayout(orientation='vertical', padding=30, spacing=15)

        main.add_widget(Label(text="[b]GESTIÓN DE USUARIOS[/b]",
                              markup=True, halign="center", size_hint_y=0.07))
        main.add_widget(Label(text="Ingrese los datos del usuario y use los botones.",
                              halign="center", size_hint_y=0.06))

        form = GridLayout(cols=2, spacing=8, size_hint_y=0.6)

        form.add_widget(Label(text="Cédula:"))
        self.u_cedula = TextInput(multiline=False, hint_text="Ej: 123456")
        form.add_widget(self.u_cedula)

        form.add_widget(Label(text="Nombre:"))
        self.u_nombre = TextInput(multiline=False, hint_text="Ej: Maria")
        form.add_widget(self.u_nombre)

        form.add_widget(Label(text="Apellido:"))
        self.u_apellido = TextInput(multiline=False, hint_text="Ej: Ospina")
        form.add_widget(self.u_apellido)

        form.add_widget(Label(text="Teléfono:"))
        self.u_telefono = TextInput(multiline=False, hint_text="Ej: 3001234567")
        form.add_widget(self.u_telefono)

        form.add_widget(Label(text="Correo:"))
        self.u_correo = TextInput(multiline=False, hint_text="Ej: maria@correo.com")
        form.add_widget(self.u_correo)

        form.add_widget(Label(text="Dirección:"))
        self.u_direccion = TextInput(multiline=False, hint_text="Ej: Calle 1 #2-3")
        form.add_widget(self.u_direccion)

        main.add_widget(form)

        botones = GridLayout(cols=3, spacing=8, size_hint_y=0.1)
        b1 = Button(text="Insertar", background_color=(0.4, 0.75, 0.5, 1))
        b1.bind(on_press=self.usuarios_insertar)
        botones.add_widget(b1)
        b2 = Button(text="Buscar por cédula", background_color=(0.3, 0.65, 0.45, 1))
        b2.bind(on_press=self.usuarios_buscar)
        botones.add_widget(b2)
        b3 = Button(text="Modificar", background_color=(0.5, 0.8, 0.55, 1))
        b3.bind(on_press=self.usuarios_modificar)
        botones.add_widget(b3)
        main.add_widget(botones)

        self.u_resultado = Label(text="Esperando acción...", halign="center",
                                 color=(0.8, 0.8, 0.8, 1), size_hint_y=0.17)
        main.add_widget(self.u_resultado)
        return main

    def usuarios_insertar(self, instance):
        """Inserta un nuevo usuario en la base de datos.

        Parameters
        ----------
        instance : Button
            Botón que disparó el evento.
        """
        try:
            usuario = Usuario(cedula=self.u_cedula.text, nombre=self.u_nombre.text,
                              apellido=self.u_apellido.text, telefono=self.u_telefono.text,
                              correo=self.u_correo.text, direccion=self.u_direccion.text)
            UsuariosController.insertar(usuario)
            self.u_resultado.color = (0.2, 1, 0.2, 1)
            self.u_resultado.text = "¡Usuario insertado correctamente!"
        except Exception as e:
            self.u_resultado.color = (1, 0.3, 0.3, 1)
            self.u_resultado.text = f"ERROR: {str(e)}\n\n¿Necesitas ayuda? Consulta el README en:\ngithub.com/manolo-restrepo/Proyecto-Ahorro-Programado"

    def usuarios_buscar(self, instance):
        """Busca un usuario por cédula y rellena los campos del formulario.

        Parameters
        ----------
        instance : Button
            Botón que disparó el evento.
        """
        try:
            usuario = UsuariosController.buscar(self.u_cedula.text)
            self.u_nombre.text = usuario.nombre
            self.u_apellido.text = usuario.apellido
            self.u_telefono.text = usuario.telefono
            self.u_correo.text = usuario.correo
            self.u_direccion.text = usuario.direccion
            self.u_resultado.color = (0.2, 1, 0.2, 1)
            self.u_resultado.text = f"Usuario encontrado: cédula {self.u_cedula.text}"
        except Exception as e:
            self.u_resultado.color = (1, 0.3, 0.3, 1)
            self.u_resultado.text = f"ERROR: {str(e)}\n\n¿Necesitas ayuda? Consulta el README en:\ngithub.com/manolo-restrepo/Proyecto-Ahorro-Programado"

    def usuarios_modificar(self, instance):
        """Modifica un usuario existente en la base de datos.

        Parameters
        ----------
        instance : Button
            Botón que disparó el evento.
        """
        try:
            usuario = Usuario(cedula=self.u_cedula.text, nombre=self.u_nombre.text,
                              apellido=self.u_apellido.text, telefono=self.u_telefono.text,
                              correo=self.u_correo.text, direccion=self.u_direccion.text)
            UsuariosController.modificar(usuario)
            self.u_resultado.color = (0.2, 1, 0.2, 1)
            self.u_resultado.text = "¡Usuario modificado correctamente!"
        except Exception as e:
            self.u_resultado.color = (1, 0.3, 0.3, 1)
            self.u_resultado.text = f"ERROR: {str(e)}\n\n¿Necesitas ayuda? Consulta el README en:\ngithub.com/manolo-restrepo/Proyecto-Ahorro-Programado"

    # ─────────────────────────────────────────
    # ABONOS
    # ─────────────────────────────────────────
    def build_abonos(self):
        """Construye el formulario de gestión de abonos.

        Returns
        -------
        BoxLayout
            Layout con los campos y botones de la pestaña Abonos.
        """
        main = BoxLayout(orientation='vertical', padding=30, spacing=15)

        main.add_widget(Label(text="[b]GESTIÓN DE ABONOS[/b]",
                              markup=True, halign="center", size_hint_y=0.07))
        main.add_widget(Label(text="Ingrese los datos del abono y use los botones.",
                              halign="center", size_hint_y=0.06))

        form = GridLayout(cols=2, spacing=8, size_hint_y=0.6)

        form.add_widget(Label(text="ID Abono (buscar/modificar):"))
        self.a_id = TextInput(multiline=False, input_filter='int', hint_text="Ej: 1")
        form.add_widget(self.a_id)

        form.add_widget(Label(text="ID Plan:"))
        self.a_id_plan = TextInput(multiline=False, input_filter='int', hint_text="Ej: 1")
        form.add_widget(self.a_id_plan)

        form.add_widget(Label(text="Mes del abono:"))
        self.a_mes = TextInput(multiline=False, input_filter='int', hint_text="Ej: 3")
        form.add_widget(self.a_mes)

        form.add_widget(Label(text="Valor abono ($):"))
        self.a_valor = TextInput(multiline=False, input_filter='float', hint_text="Ej: 500000")
        form.add_widget(self.a_valor)

        form.add_widget(Label(text="Nueva cuota ($):"))
        self.a_cuota = TextInput(multiline=False, input_filter='float', hint_text="Ej: 215000")
        form.add_widget(self.a_cuota)

        main.add_widget(form)

        botones = GridLayout(cols=3, spacing=8, size_hint_y=0.1)
        b1 = Button(text="Insertar", background_color=(0.4, 0.75, 0.5, 1))
        b1.bind(on_press=self.abonos_insertar)
        botones.add_widget(b1)
        b2 = Button(text="Buscar por ID", background_color=(0.3, 0.65, 0.45, 1))
        b2.bind(on_press=self.abonos_buscar)
        botones.add_widget(b2)
        b3 = Button(text="Modificar", background_color=(0.5, 0.8, 0.55, 1))
        b3.bind(on_press=self.abonos_modificar)
        botones.add_widget(b3)
        main.add_widget(botones)

        self.a_resultado = Label(text="Esperando acción...", halign="center",
                                 color=(0.8, 0.8, 0.8, 1), size_hint_y=0.17)
        main.add_widget(self.a_resultado)
        return main

    def abonos_insertar(self, instance):
        """Inserta un nuevo abono en la base de datos.

        Parameters
        ----------
        instance : Button
            Botón que disparó el evento.
        """
        try:
            abono = Abono(id_abono=None, id_plan=int(self.a_id_plan.text),
                          mes_abono=int(self.a_mes.text), valor_abono=float(self.a_valor.text),
                          nueva_cuota=float(self.a_cuota.text))
            AbonosController.insertar(abono)
            self.a_resultado.color = (0.2, 1, 0.2, 1)
            self.a_resultado.text = "¡Abono insertado correctamente!"
        except Exception as e:
            self.a_resultado.color = (1, 0.3, 0.3, 1)
            self.a_resultado.text = f"ERROR: {str(e)}\n\n¿Necesitas ayuda? Consulta el README en:\ngithub.com/manolo-restrepo/Proyecto-Ahorro-Programado"

    def abonos_buscar(self, instance):
        """Busca un abono por ID y rellena los campos del formulario.

        Parameters
        ----------
        instance : Button
            Botón que disparó el evento.
        """
        try:
            abono = AbonosController.buscar(int(self.a_id.text))
            self.a_id_plan.text = str(abono.id_plan)
            self.a_mes.text = str(abono.mes_abono)
            self.a_valor.text = str(abono.valor_abono)
            self.a_cuota.text = str(abono.nueva_cuota)
            self.a_resultado.color = (0.2, 1, 0.2, 1)
            self.a_resultado.text = f"Abono encontrado: ID {self.a_id.text}"
        except Exception as e:
            self.a_resultado.color = (1, 0.3, 0.3, 1)
            self.a_resultado.text = f"ERROR: {str(e)}\n\n¿Necesitas ayuda? Consulta el README en:\ngithub.com/manolo-restrepo/Proyecto-Ahorro-Programado"

    def abonos_modificar(self, instance):
        """Modifica un abono existente en la base de datos.

        Parameters
        ----------
        instance : Button
            Botón que disparó el evento.
        """
        try:
            abono = Abono(id_abono=int(self.a_id.text), id_plan=int(self.a_id_plan.text),
                          mes_abono=int(self.a_mes.text), valor_abono=float(self.a_valor.text),
                          nueva_cuota=float(self.a_cuota.text))
            AbonosController.modificar(abono)
            self.a_resultado.color = (0.2, 1, 0.2, 1)
            self.a_resultado.text = "¡Abono modificado correctamente!"
        except Exception as e:
            self.a_resultado.color = (1, 0.3, 0.3, 1)
            self.a_resultado.text = f"ERROR: {str(e)}\n\n¿Necesitas ayuda? Consulta el README en:\ngithub.com/manolo-restrepo/Proyecto-Ahorro-Programado"

    # ─────────────────────────────────────────
    # BIENVENIDA
    # ─────────────────────────────────────────
    def mostrar_bienvenida(self):
        """Muestra un popup de bienvenida con instrucciones de uso al iniciar la app."""
        contenido = BoxLayout(orientation='vertical', padding=20, spacing=15)
        contenido.add_widget(Label(
            text="[b]BIENVENIDO A AHORRO PROGRAMADO[/b]",
            markup=True, halign="center", size_hint_y=0.2
        ))
        contenido.add_widget(Label(
            text="Esta app tiene tres secciones:\n\n"
                 "• Planes: gestiona tus planes de ahorro.\n"
                 "• Usuarios: gestiona los usuarios registrados.\n"
                 "• Abonos: gestiona los abonos a los planes.\n\n"
                 "En cada pestaña puedes Insertar, Buscar y Modificar registros.",
            halign="left", size_hint_y=0.6
        ))
        btn = Button(text="Continuar", size_hint_y=0.2, background_color=(0.4, 0.75, 0.5, 1))
        contenido.add_widget(btn)
        self.popup = Popup(title="Instrucciones", content=contenido, size_hint=(0.85, 0.6))
        btn.bind(on_press=self.popup.dismiss)
        self.popup.open()


if __name__ == '__main__':
    AhorroApp().run()