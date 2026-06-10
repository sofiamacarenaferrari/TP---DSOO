class Socio:
    def __init__(self, id_socio, nombre, apellido, dni, mail):
        self.id_socio = id_socio
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail
        self.habilitado = True
# ______________________________________________________________________________________________________________________________________

def registrar_socio(socios):
    print("\n[Registrar nuevo socio]\n")

    if len(socios) == 0:
        id_socio = 1
    else:
        id_socio = max(socio.id_socio for socio in socios) + 1

    print(f"ID asignado automáticamente: {id_socio}")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    mail = input("Mail: ")

    nuevo_socio = Socio(id_socio, nombre, apellido, dni, mail)
    socios.append(nuevo_socio)

    print("\nSocio registrado con éxito.\n")
    input("Presione Enter para volver al menú...") 