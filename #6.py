# Definiendo la funcion fibonacci

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=", " if i < n-1 else "\n")
        a, b = b, a + b

# Pidiendo al usuario que ingrese el valor de n
n = int(input("Ingrese el numero de terminos: "))

# Llamando a la funcion fibonacci
print("Secuencia de Fibonacci:")
fibonacci(n)
