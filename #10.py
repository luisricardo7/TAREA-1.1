#Generador de contraseñas

import random
import string

# Definiendo la funcion para generar una contraseña aleatoria
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Generando la contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contrasena

# Pidiendo al usuario que ingrese la longitud de la contraseña
longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8 caracteres): "))

# Asegurandose de que la longitud sea minima
if longitud < 8:
    print("La longitud minima de la contraseña es 8 caracteres.")
else:
    # Generando y mostrando la contraseña
    contrasena_generada = generar_contrasena(longitud)
    print(f"Contraseña generada: {contrasena_generada}")
