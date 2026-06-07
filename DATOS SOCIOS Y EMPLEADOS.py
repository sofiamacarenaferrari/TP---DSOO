
#Clase padre 
class Persona:
    def __init__(self, nombre, apellido, dni, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail

class Socio(Persona):
    def __init__(self, nombre, apellido, dni, mail, id_socio):
        super().__init__(nombre, apellido, dni, mail)
        self.id_socio = id_socio
        self.habilitado = True


        