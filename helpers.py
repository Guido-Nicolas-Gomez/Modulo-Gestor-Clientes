""" Aquí iran las funciones de ayuda y auxiliares"""

import os
import platform

def clear_any_OS():
    """Limpia la linea de comando sin importar el sistema operativo"""

    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def input_text(min_length,max_length):
    """Solicita el ingreso de una cadena de texto con una longitud limitada"""
    
    while True:
        text = input(">")

        if max_length >= len(text) >= min_length:
            return text
        print("\nEl texto no cumple con la longitud, reintentar...")

