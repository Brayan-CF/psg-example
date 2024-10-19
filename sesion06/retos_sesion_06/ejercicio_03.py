'''
Imprime una tabla de verdad para la siguiente afirmación:
"Una puerta tiene dos interruptores que controlan dos luces
la puerta sólo debe abrirse cuando las dos luces están 
apagadas o las dos están encendidas, caso contrario la puerta
no se abre, ¿qué operador lógico se puede utilizar?"
'''
# Usamos XNOR
luz1 = True
luz2 = False
print(not((not luz1)or luz2))
print(not(luz1 or luz2))
print(not(luz2 or luz1))
print((luz1 or(not luz2)))


