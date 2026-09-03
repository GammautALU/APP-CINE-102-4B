class Entrada:

    def __init__(self, numero, asiento):
        self.__numero = numero
        self.__asiento = asiento

    def mostrar_datos(self):
        return f"""--Entrada--
Número: {self.__numero}
Asiento: {self.__asiento}
"""

    def es_asiento_valido(self):
        pass