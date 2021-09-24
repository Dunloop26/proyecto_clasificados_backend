# from contacto import Contacto
# from contenido import Contenido
from .contenido import Contenido
from data import contenido

# Se creara un objeto para el anuncio
# Esta clase define los campos que tendra la publicación}

class Publicacion():
    def __init__(self,contenido):
        self.titulo = str
        self.fecha_inicial = str
        self.fecha_final = str
        self.ciudad = str
        self.precio = str
        self.contenido = contenido
        # id_usuario = "" ó nombre = "" // Nombre de la persona que subio el anuncio
        self.estado = True    

    # Metodos de la publicación  

    def estado_publicacion(self,estado):
        estado = self.estado
        




# Se llama la funcion
