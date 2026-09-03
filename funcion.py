class Funcion:

    def __init__(self, fecha, hora, precio):
        self.__fecha = fecha
        self.__hora = hora
        self.__precio = precio

    def mostrar_datos(self):
        return f"""--Funcion--
Fecha: {self.__fecha}
Hora: {self.__hora}
Precio: {self.__precio}"""

    def es_funcion_nocturna(self):
        hora = int(self.__hora.split(":")[0])
        if hora >= 20:
            return True
        else:
            return False