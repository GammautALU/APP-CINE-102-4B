from cliente import Cliente


class ClientePremium(Cliente):

    def __init__(self, nombre, correo, edad, descuento, puntos):
        super().__init__(nombre, correo, edad)
        self.__descuento = descuento
        self.__puntos = puntos

    def calcular_precio(self, precio):
        descuento = precio * self.__descuento // 100
        return f"Precio: {precio - descuento}"