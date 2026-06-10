import json
from MATERIAL import Material, Libro, Manga 

class Biblioteca:
    def __init__(self, nombre, direccion, telefono, mail):
        self.nombre = nombre
        self.direccion = direccion 
        self.telefono = telefono 
        self.mail = mail
        self.materiales = []
        self.socios = []
        self.prestamos = []
     
    def registrar_material(self):
        print("\n[Registrar nuevo material]\n")

        if len(self.materiales) == 0:
            id_material = 1
        else:
            id_material = max(material.id_material for material in self.materiales) + 1

        print(f"ID asignado automáticamente: {id_material}")

        tipo = input("Tipo de material (libro/manga): ").lower().strip()
        titulo = input("Título: ")
        autor = input("Autor: ")
        fecha_publicacion = input("Fecha de publicación: ")
        disponible = "Disponible"

        if tipo == "libro":
            categoria = input("Categoría: ")
            editorial = input("Editorial: ")

            nuevo_material = Libro(id_material, titulo, autor, fecha_publicacion, disponible, categoria, editorial)

            self.materiales.append(nuevo_material)
            print("\nLibro registrado con éxito.\n")
            input("\nPresione Enter para volver al menú...")

        elif tipo == "manga":
            tomo = int(input("Tomo: "))

            nuevo_material = Manga(id_material, titulo, autor, fecha_publicacion, disponible, tomo)

            self.materiales.append(nuevo_material)
            print("\nManga registrado con éxito.\n")
            input("\nPresione Enter para volver al menú...")

        else:
            print("\nTipo inválido. Debe ser 'libro' o 'manga'.\n")






#listar_prestamos_activos()
#detectar_prestamos_vencidos()