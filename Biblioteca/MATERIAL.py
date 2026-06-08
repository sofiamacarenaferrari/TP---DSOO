
class Material: 
    def __init__(self, id_material, titulo, autor, fecha_publicacion, disponible):
        self.id_material = id_material
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.disponible = disponible


class Libro(Material):
    def __init__(self, id_material, titulo, autor, fecha_publicacion, disponible, categoria, editorial):
        super().__init__(id_material, titulo, autor, fecha_publicacion, disponible) 
        self.categoria = categoria 
        self.editorial = editorial 


class Manga(Material):
    def __init__(self, id_material, titulo, autor, fecha_publicacion, disponible, tomo):
        super().__init__(id_material, titulo, autor, fecha_publicacion, disponible) 
        self.tomo = tomo 