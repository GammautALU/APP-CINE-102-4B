class Cliente:

    def __init__(self, nombre, correo, edad):
        self.__nombre = nombre
        self.__correo = correo
        self.__edad = edad

    def mostrar_datos(self):
        return f"""--Cliente--
Nombre: {self.__nombre}
Correo: {self.__correo}
Edad: {self.__edad}
"""

    def calcular_precio(self, precio):
        return precio