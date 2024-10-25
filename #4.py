# Clase Calculadora

class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: Division por cero no permitida."
        return a / b

# Creando una instancia de la calculadora
calculadora = Calculadora()

# Solicitando numeros al usuario
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

# Realizando las operaciones y mostrando los resultados
suma = calculadora.sumar(a, b)
resta = calculadora.restar(a, b)
multiplicacion = calculadora.multiplicar(a, b)
division = calculadora.dividir(a, b)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

