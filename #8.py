# Vocales 

def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0
    
    for letra in frase:
        if letra in vocales:
            contador += 1
            
    return contador

# Pidiendo al usuario que ingrese una frase
frase = input("Ingrese una frase: ")

# Utilizando la funcion para contar las vocales
numero_vocales = contar_vocales(frase)

# Mostrando el resultado
print(f"Numero de vocales en la frase: {numero_vocales}")
