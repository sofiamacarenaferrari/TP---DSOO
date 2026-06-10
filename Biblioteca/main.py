import json
from BIBLIOTECA import Biblioteca
from MATERIAL import Material, Libro, Manga 
from SOCIOS import Socio, registrar_socio
from PRESTAMO import Prestamo, registrar_prestamo, registrar_devolucion, listar_prestamos_activos, listar_prestamos_vencidos

# ______________________________________________________________________________________________________________________________________

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

    for item in datos["socios"]:
        nuevo_socio = Socio(item["id_socio"], item["nombre"], item["apellido"], item["dni"], item["mail"])
        nuevo_socio.habilitado = item["habilitado"]
        mi_biblioteca.socios.append(nuevo_socio)

    print(f"Materiales cargados con éxito. Total: {len(mi_biblioteca.materiales)}")
    print(f"Socios cargados con éxito. Total: {len(mi_biblioteca.socios)}")
# ______________________________________________________________________________________________________________________________________

def mostrar_menu(mi_biblioteca):
        continuar = True

        while continuar:
            print(f"\n--- BIENVENIDO A LA {mi_biblioteca.nombre.upper()} ---\n")
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
            print("10. Listado de préstamos vencidos")
            print("11. Salir")

            opcion = input("\nElige una opción: ")

            if opcion == "1":
                print("\n[Lista de los libros y mangas]\n")
                hay_disponible = False
                for material in mi_biblioteca.materiales: 
                    if material.disponible == "Disponible":
                        print(f"ID: {material.id_material} | Título: {material.titulo} | Autor: {material.autor}")
                hay_disponible = True 

                if not hay_disponible: 
                    print("No hay materiales disponibles en este momento.")
                    
                input("\nPresione Enter para volver al menú...")

            elif opcion == "2":
                mi_biblioteca.registrar_material()

            elif opcion == "3":
                print("\n[Buscar Material por Título o Autor]")
                busqueda = input("Ingrese el título o el autor que desea buscar: ").lower()
                encontrado = False
                print("\nResultados de la búsqueda:")
                       
                for material in mi_biblioteca.materiales:
                    if busqueda in material.titulo.lower() or busqueda in material.autor.lower():
                        if isinstance(material, Manga):
                            print(f"-> [MANGA] ID: {material.id_material} | Título: {material.titulo} | Autor: {material.autor} | Tomo: {material.tomo} | Estado: {material.disponible}\n")
                        elif isinstance(material, Libro):
                            print(f"-> [LIBRO] ID: {material.id_material} | Título: {material.titulo} | Autor: {material.autor} | Estado: {material.disponible}\n")
                encontrado = True

                if not encontrado:
                    print("No se encontraron materiales que coincidan con ese título o autor.")
                input("\nPresione Enter para volver al menú...")

            elif opcion == "4":
                registrar_socio(mi_biblioteca.socios)
        
            elif opcion == "5":
                print("\n[Consultar información de socio]\n")

                dni_buscado = input("Ingrese el DNI del socio: ").strip()
                encontrado = False
                print("Socios cargados:", len(mi_biblioteca.socios))

                for socio in mi_biblioteca.socios:
                    print("DNI guardado:", socio.dni)
                    if socio.dni == dni_buscado:
                        print("\nSocio encontrado:")
                        print(f"ID: {socio.id_socio}")
                        print(f"Nombre: {socio.nombre}")
                        print(f"Apellido: {socio.apellido}")
                        print(f"DNI: {socio.dni}")
                        print(f"Mail: {socio.mail}")
                        print(f"Habilitado: {'Habilitado' if socio.habilitado else 'No habilitado'}")
                        encontrado = True

                if not encontrado:
                    print("\nNo se encontró ningún socio con ese DNI.")
                input("\nPresione Enter para volver al menú...")

            elif opcion == "6":
                print("\n[Listado de usuarios habilitados]\n")
                hay_socios = False

                for socio in mi_biblioteca.socios:
                    if socio.habilitado == True:
                        print(f"ID: {socio.id_socio} | Nombre: {socio.nombre} | Apellido: {socio.apellido} | DNI: {socio.dni} | Mail: {socio.mail}\n")
                        hay_socios = True

                if not hay_socios:
                    print("No hay usuarios habilitados en este momento.")
                input("\nPresione Enter para volver al menú...")
                
            
            elif opcion == "7":
                registrar_prestamo(mi_biblioteca.prestamos, mi_biblioteca.socios, mi_biblioteca.materiales)

            elif opcion == "8":
                registrar_devolucion(mi_biblioteca.prestamos, mi_biblioteca.socios)

            elif opcion == "9":
                listar_prestamos_activos(mi_biblioteca.prestamos)

            elif opcion == "10":
                listar_prestamos_vencidos(mi_biblioteca.prestamos)

            elif opcion == "11":
                print("Saliendo del sistema...")
                continuar = False
            
            else:
                print("Opción incorrecta. Elige una opcion")
                input("\nPresione Enter para volver al menú...")


mi_biblioteca_fireandblood = Biblioteca("Biblioteca Fire and Blood", "Malabia 246", "4321-5678", "biblioteca_fire_and_blood@gmail.com")
cargar_base_de_datos(mi_biblioteca_fireandblood)
mostrar_menu(mi_biblioteca_fireandblood)