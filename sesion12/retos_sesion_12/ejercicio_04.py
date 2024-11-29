'''
Una tienda ofrece descuentos a sus clientes, si el cliente es 
mayor de edad y tiene una compra mayor a 1000, se le aplica un 
descuento del 10%, si es menor de edad y tiene una compra mayor a 
500 se le aplica un descuento del 5%, si no cumple ninguna 
condición se le aplica un descuento del 2%
'''
edad = int(input("Ingrese su edad:\n"))
compras = int(input("Ingrese el monto de su compra:\n"))

if edad >= 18 and compras > 1000:
    tienda = "Se te aplica un descuento del 10%"
elif edad < 18 and compras > 500:
    tienda = "Se te aplica un descuento del 5%"
else:
    tienda = "Solo te daré un 2% de descuento"

print(tienda)
