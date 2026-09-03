from cliente import Cliente


class ClienteNormal(Cliente):
    def __init__(self, nombre, correo, edad):
        super().__init__(nombre, correo, edad)

    def calcular_precio(self, precio):
        print(f"""Precio : {precio}""")