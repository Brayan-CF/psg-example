'''
Simular un cajero automático que solicite un monto a retirar, 
si el monto es mayor al saldo lanzar una excepción personalizada y 
si el monto es mayor a 1000 lanzar una excepción genérica
'''

class SaldoInsuficiente(Exception):
    pass

def cajero():
    saldo = 1000
    while True:
        try:
            monto = float(input("Ingresa el monto a retirar: "))
            if monto > saldo:
                raise SaldoInsuficiente("Saldo insuficiente")
            if monto > 1000:
                raise Exception("Monto mayor a 1000")
            saldo -= monto
            print(f"Retiro exitoso, saldo restante: {saldo}")
        except SaldoInsuficiente as e:
            print(e)
        except Exception as e:
            print(f"Error: {e}")
            break
    
cajero()
