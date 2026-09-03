from pelicula import Pelicula
from funcion import Funcion
from sala import Sala
from entrada import Entrada
from cliente_premium import ClientePremium

def main():
    #instanciar pelicula
    pelicula1 = Pelicula("Avengers", "Accion", "120")
    print(pelicula1.mostrar_datos())

    #instanciar funcion
    funcion1 = Funcion("03-09-2026", "21:00", 8500)
    print(funcion1.mostrar_datos())
    print(funcion1.es_funcion_nocturna())

    #instanciar sala
    sala1 = Sala(7, 100)
    print(sala1.mostrar_datos())
    print(sala1.hay_disponibilidad(95))

    #instanciar asiento
    entrada1 = Entrada(123, 8)
    print(entrada1.mostrar_datos())

    #Instanciar clientes
    cliente_prem = ClientePremium("Claudio", "Claudio@gmail.com", 26, 20, 100)
    print(cliente_prem.calcular_precio(7000))

if __name__ == "__main__":
    main()