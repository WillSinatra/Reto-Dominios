import os

def verificar_ping(dominio):
    """ Verifica si un dominio responde a un ping. """
    response = os.system(f"ping -n 1 {dominio}") 
    if response == 0:
        return True
    else:
        return False

def leer_dominios(archivo):
    """ Lee el archivo .txt y devuelve una lista de dominios. """
    with open(archivo, "r") as file:
        return [line.strip() for line in file.readlines()]

def verificar_dominios(archivo):
    """ Lee los dominios y verifica cuáles están activos y cuáles no """
    dominios = leer_dominios(archivo)
    for dominio in dominios:
        if verificar_ping(dominio):
            print(f"{dominio}: Activo")
        else:
            print(f"{dominio}: Inactivo")


archivo_dominios = "dominios.txt"


verificar_dominios(archivo_dominios)
