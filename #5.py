# Numero Primo

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un numero entero: "))

if es_primo(numero):
    print(f"El numero {numero} es primo.")
else:
    print(f"El numero {numero} no es primo.")
