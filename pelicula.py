class Pelicula:

    def __init__(self, titulo, genero, duracion):
        self.__titulo = titulo
        self.__genero = genero
        self.__duracion = duracion

    def mostrar_datos(self):
        return f"""--Pelicula--
Título: {self.__titulo}
Género: {self.__genero}
Duracion: {self.__duracion}"""