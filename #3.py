# Clase Cuenta Bancaria

class CuentaBancaria:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, cantidad: float):
        self.saldo += cantidad
        print(f"Deposito de {cantidad} realizado. Saldo actual: {self.saldo}")

    def retirar(self, cantidad: float):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}")
        else:
            print(f"Fondos insuficientes. Saldo actual: {self.saldo}")

    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta es: {self.saldo}")


cuenta = CuentaBancaria("Luis Soriano")

cuenta.depositar(500)   # Deposito de 500 L.
cuenta.retirar(200)     # Retiro de 200 L.
cuenta.mostrar_saldo()  # Mostrando el saldo actual

cuenta.retirar(400)     # Intento de retiro mayor al saldo actual
cuenta.depositar(300)   # Depsito de 300 L.
cuenta.mostrar_saldo()  # Mostrando el saldo actual final
