'''
Convertir a cuantos días, horas, minutos
y segundos corresponde la siguiente cantidad
de segundos: 288325
'''
segundos = 288325
minutos = (segundos//60)
horas = (minutos//60)
dias = (horas//24)

print("los segundos son: ", segundos,"[s]")
print("los minutos correspondientes de 288325[s] es: ",minutos,"[min]")
print("las horas correspondientes de 288325[s] es: ",horas,"[hrs]")
print("los dias correspondientes de 288325[s] es: ",dias,"[dias]")