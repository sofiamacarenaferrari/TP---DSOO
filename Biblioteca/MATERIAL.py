#MATERIALES

#Clase padre 
class Material: 
    def __init__(self, id_material, titulo, autor, fecha_publicacion, estado):
        self.id_material = id_material
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.estado = estado

#Clase hija de Material para gestionar libros
class Libro(Material):
    def __init__(self, id_material, titulo, autor, fecha_publicacion, estado, categoria, editorial):
        super().__init__(id_material, titulo, autor, fecha_publicacion, estado) #Heredan dichos atributos de su clase padre 
        self.categoria = categoria 
        self.editorial = editorial 

#Clase hija de Material para gestionar mangas
class Manga(Material):
    def __init__(self, id_material, titulo, autor, fecha_publicacion, estado, tomo):
        super().__init(id_material, titulo, autor, fecha_publicacion, estado) #Heredan dichos atributos de su clase padre 
        self.tomo = tomo 