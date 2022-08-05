""" Gestor de los clientes"""
import pickle
import re
import helpers

class Client:
    """Objeto que representara a cada cliente"""
    
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    
    def __str__(self):
        return f"{self.dni}: {self.nombre} {self.apellido}"


class Manager:
    """Clase con los metodos necesarios para realizar las operaciones indicadas en el menu del programa"""

    clients = [] # Se crea la variable contenedora de clientes

    @staticmethod
    def show_clients():
        """Muestra todos los clientes cargados hasta el momento"""

        for client in Manager.clients:
            print(client)

    @staticmethod
    def find():
        """Devuelve el cliente y su indice, en caso de encontrarse a traves de su DNI"""

        dni = input("Ingresar un DNI: \n>")

        for i, client in enumerate(Manager.clients):
            if client.dni == dni:
                print(client)
                return i, client

        return None, None


    def _is_valid(dni):
        """Verifica si el formato de DNI ingresado es valido, e inspecciona si el mismo ya se encuentra agregado
        >>> Manager._is_valid("23G") # No cumple, ya existe
        False

        >>> Manager._is_valid("T76") # No cumple, patron incorrecto
        False

        >>> Manager._is_valid("89H") # Correcto
        True
        """
        
        if not re.match("[0-9]{2}[A-Z]",dni): # Comprobando si cumple con el formato
            return False

        for client in Manager.clients: # Comprobando que el DNI no se encuentre registrado
            if client.dni == dni:
                return False
        
        return True

    @staticmethod
    def add():
        """Agrega un cliente al lista"""

        client = {}

        print("\nIngresar un nombre. (Debe tener de 3 a 30 acaracteres): ")
        client["nombre"] = helpers.input_text(3,30)

        print("\nIngresar un apellido. (Debe tener de 3 a 30 acaracteres): ")
        client["apellido"] = helpers.input_text(3,30)

        while True:
            print("\nIngresar un ID. (debe tener dos numeros y una letra mayuscula): ")
            dni = helpers.input_text(3,3)

            if Manager._is_valid(dni):
                client["dni"] = dni
                break
            else:
                print("\nID invalido, reintentar...")
        
        Manager.clients.append(Client(client["nombre"],client["apellido"],client["dni"]))

        # Guardando el objeto como un archivo .pckl
        with open("lista.pckl","wb") as f:
            pickle.dump(Manager.clients, f)

        return client

    @staticmethod
    def edit():
        """Modificar un cliente a partir de su DNI"""

        i, client = Manager.find() #Buscando un cliente mediante el DNI
        
        if client != None:
            print("\nIngrese el nuevo nombre. (debe tener entre 3 y 30 caracteres):")
            Manager.clients[i].nombre = helpers.input_text(3,30)

            print("\nIngrese el nuevo apellido. (debe tener entre 3 y 30 caracteres):")
            Manager.clients[i].apellido = helpers.input_text(3,30)

            return True

        print("\nCliente no encontrado")
        return False

    @staticmethod
    def delete():
        """Eliminar un cliente a partir de su DNI"""

        i, client = Manager.find()
        if client != None:
            Manager.clients.pop(i)
            return True
        return False


marta = Client("Marta", "Sanchez","15J") # Agregando objetos al gestor
Manager.clients.append(marta)
Manager.clients.append(Client("Raul","Fernandez", "23G"))
Manager.clients.append(Client("Nicolas","Gomez","37H"))
Manager.clients.append(Client("Maximiliano","Madrid","25U"))

if __name__ == "__main__": # Test
    import doctest
    doctest.testmod()
