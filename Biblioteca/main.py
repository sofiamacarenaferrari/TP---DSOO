import json
from BIBLIOTECA import Biblioteca
from MATERIAL import Material, Libro, Manga 

# ______________________________________________________________________________________________________________________________________________________________________________

def cargar_base_de_datos(mi_biblioteca):
    print("Cargando materiales...")
    with open("Biblioteca/datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo) 

    for item in datos["libros"]:
        nuevo_libro = Libro(**item)
        mi_biblioteca.materiales.append(nuevo_libro)
        
    for item in datos["mangas"]:
        nuevo_manga = Manga(**item)
        mi_biblioteca.materiales.append(nuevo_manga)

    print(f"Materiales cargados con éxito. Total: {len(mi_biblioteca.materiales)}")

# ______________________________________________________________________________________________________________________________________________________________________________

def mostrar_menu(mi_biblioteca):
        continuar = True

        while continuar:
            print(f"\n--- BIENVENIDO A LA {mi_biblioteca.nombre.upper()} ---")
            print("Elige una opción:")
            print("1. Ver materiales disponibles")
            print("2. Registrar nuevo material (Libro/Manga)")
            print("3. Buscar material por criterios")
            print("4. Registrar un Socio")
            print("5. Consultar info de Socio")
            print("6. Listado de usuarios habilitados")
            print("7. Registrar un préstamo")
            print("8. Registrar una devolución")
            print("9. Listado de préstamos activos")
            print("10. Salir")

            opcion = input()

            if opcion == "1":
                print("\n[Lista de los libros y mangas]")
                hay_disponible = False
                for material in mi_biblioteca.materiales: 
                    if material.disponible == True:
                        print(f"ID: {material.id_material} | Título: {material.titulo} | Autor: {material.autor}")
                        hay_disponible = True 

                if not hay_disponible: 
                    print("No hay materiales disponibles en este momento.")
                continuar = False

            elif opcion == "10":
                print("Saliendo del sistema...")
                continuar = False
            else:
                print("Opción incorrecta. Elige una opcion")


mi_biblioteca_fireandblood = Biblioteca("Biblioteca Fire and Blood", "Malabia 246", "4321-5678", "biblioteca_fire_and_blood@gmail.com")
print(mi_biblioteca_fireandblood.nombre)

cargar_base_de_datos(mi_biblioteca_fireandblood)
mostrar_menu(mi_biblioteca_fireandblood)