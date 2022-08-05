""" Aquí se realiza el menu """

import helpers
from manager import Manager

command = Manager() #Quien gestiona las funcionalidades

class Menu:
    """Clase donde se desplega el menu del programa con el metodo loop"""

    def loop():
        while True:

            helpers.clear_any_OS() #Limpiamos la terminal, sin importar el sistema operativo

            print("=============================")
            print("    BIENVENIDOS AL GESTOR    ")
            print("=============================")
            print("[1] Listar los clientes      ")
            print("[2] Mostrar un cliente       ")
            print("[3] Añadir cliente           ")
            print("[4] Modificar cliente        ")
            print("[5] Borrar cliente           ")
            print("[6] Salir del programa       ")
            print("=============================")

            select = input(">")

            helpers.clear_any_OS()

            if select == "1": # Seleccion del comando a realizar segun valor ingresado
                print("Se mostraran los clientes:\n")
                command.show_clients()
            elif select == "2":
                print("Se mostraran un clientes:\n")
                command.find()
            elif select == "3":
                print("Se añadirá un clientes:\n")
                command.add()
            elif select == "4":
                print("Se modificará un clientes:\n")
                if command.edit():
                    print("\nCliente ingresado:")
                else:
                    print("\nEl cliente no existe")
            elif select == "5":
                print("Se borrará un clientes:\n")
                if command.delete():
                    print("Cliente eliminado")
                else:
                    print("No se encontro el cleinte")
            elif select == "6":
                print("Saliendo del programa:\n")
                break
            else:
                print("valor incorrecto")

            input("\nPresione Enter para continuar...") # Espera luego de ejecutar cada comando