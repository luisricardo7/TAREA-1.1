# Adivina el numero

import random

# numero aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)
intentos = 0

print("¡Adivina el numero entre 1 y 100!")

# Ciclo para permitir al usuario seguir intentando
while True:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1
    
    if intento < numero_aleatorio:
        print("El numero es mayor.")
    elif intento > numero_aleatorio:
        print("El numero es menor.")
    else:
        print(f"¡Felicitaciones! Has adivinado el numero en {intentos} intentos.")
        break 
