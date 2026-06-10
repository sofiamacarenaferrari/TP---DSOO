from datetime import date, timedelta

# ______________________________________________________________________________________________________________________________________
class Prestamo:
    def __init__(self, id_prestamo, socio, material):
        self.id_prestamo = id_prestamo
        self.socio = socio
        self.material = material
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=30)
        self.activo = True
# ______________________________________________________________________________________________________________________________________

def registrar_prestamo(prestamos, socios, materiales):
    print("\n[Registrar nuevo préstamo]\n")

    dni_buscado = input("Ingrese el DNI del socio: ").strip()
    socio_encontrado = None

    for socio in socios:
        if socio.dni == dni_buscado:
            socio_encontrado = socio
            break

    if not socio_encontrado:
        print("No se encontró ningún socio con ese DNI.")
        return

    titulo_buscado = input("Ingrese el título del material: ").strip()
    material_encontrado = None

    for material in materiales:
        if material.titulo.lower() == titulo_buscado.lower():
            material_encontrado = material
            break

    if not material_encontrado:
        print("No se encontró ningún material con ese título.")
        return
    
    if len(prestamos) == 0:
        id_prestamo = 1

    else:
        id_prestamo = max(prestamo.id_prestamo for prestamo in prestamos) + 1

    nuevo_prestamo = Prestamo(id_prestamo, socio_encontrado, material_encontrado)
    prestamos.append(nuevo_prestamo)

    print(f"\nPréstamo registrado con éxito.")
    print(f"Fecha de préstamo: {nuevo_prestamo.fecha_prestamo}")
    print(f"Fecha límite de devolución: {nuevo_prestamo.fecha_devolucion}")
    input("\nPresione Enter para volver al menú...")

# ______________________________________________________________________________________________________________________________________

def registrar_devolucion(prestamos, socios):
    print("\n[Registrar devolución]\n")

    dni_buscado = input("Ingrese el DNI del socio: ").strip()
    socio_encontrado = None

    for socio in socios:
        if socio.dni == dni_buscado:
            socio_encontrado = socio
            break

    if not socio_encontrado:
        print("No se encontró ningún socio con ese DNI.")
        return

    prestamos_activos = []
    for prestamo in prestamos:
        if prestamo.socio.dni == dni_buscado and prestamo.activo == True:
            prestamos_activos.append(prestamo)

    if len(prestamos_activos) == 0:
        print("El socio no tiene préstamos activos.")
        return

    print("\nPréstamos activos del socio:\n")
    for i, prestamo in enumerate(prestamos_activos):
        print(f"{i + 1}. {prestamo.material.titulo} - Vence: {prestamo.fecha_devolucion}")

    eleccion = input("\n¿Cuál desea devolver? (ingrese el número): ")
    indice = int(eleccion) - 1

    prestamos_activos[indice].activo = False
    print(f"\nDevolución registrada con éxito.")
    print(f"Material devuelto: {prestamos_activos[indice].material.titulo}")
    input("\nPresione Enter para volver al menú...")

# ______________________________________________________________________________________________________________________________________

def listar_prestamos_activos(prestamos):
    print("\n[Listado de préstamos activos]\n")

    hay_prestamos = False

    for prestamo in prestamos:
        if prestamo.activo == True:
            print(f"ID préstamo: {prestamo.id_prestamo}")
            print(f"Socio: {prestamo.socio.nombre} {prestamo.socio.apellido}")
            print(f"Material: {prestamo.material.titulo}")
            print(f"Fecha préstamo: {prestamo.fecha_prestamo}")
            print(f"Fecha devolución: {prestamo.fecha_devolucion}")
            print("---")
            hay_prestamos = True

    if not hay_prestamos:
        print("No hay préstamos activos.")
    input("\nPresione Enter para volver al menú...")

# ______________________________________________________________________________________________________________________________________

def listar_prestamos_vencidos(prestamos):
    print("\n[Listado de préstamos vencidos]\n")

    hay_vencidos = False

    for prestamo in prestamos:
        if prestamo.activo == True and prestamo.fecha_devolucion < date.today():
            print(f"ID préstamo: {prestamo.id_prestamo}")
            print(f"Socio: {prestamo.socio.nombre} {prestamo.socio.apellido}")
            print(f"Material: {prestamo.material.titulo}")
            print(f"Fecha préstamo: {prestamo.fecha_prestamo}")
            print(f"Fecha vencimiento: {prestamo.fecha_devolucion}")
            print("---")
            hay_vencidos = True

    if not hay_vencidos:
        print("No hay préstamos vencidos.")

    input("\nPresione Enter para volver al menú...")