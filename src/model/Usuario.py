class Usuario:

    def __init__(self, cedula, nombre, apellido, telefono, correo, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def is_equal(self, otro):
        return (self.cedula == otro.cedula and
                self.nombre == otro.nombre and
                self.apellido == otro.apellido and
                self.telefono == otro.telefono and
                self.correo == otro.correo and
                self.direccion == otro.direccion)