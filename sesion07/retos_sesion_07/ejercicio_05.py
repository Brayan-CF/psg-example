'''
Escribe un programa que reciba una cadena 
y retorna verdadero o falso si es palindrome 
la frase o palabra ejemplo "Anita lava la 
Tina" es verdad
'''
oracion ="Anita lava la Tina"
sin_espacios = oracion.replace(" ","").lower()
es_palindromo = sin_espacios == sin_espacios[::-1]
print(es_palindromo)



