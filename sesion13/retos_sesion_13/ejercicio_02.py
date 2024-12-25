'''
Imprimir los 20 primeros números primos
'''

for num in range(1, 80):
    if num < 2:
        continue  

    #contador = 1
    es_primo = True  
    for i in range(2, num):
        if num % i == 0:
            es_primo = False 
            break  
    
    for contador, es_primo in enumerate(range):
        print(contador, es_primo)

    #if es_primo:
        #print(f"{contador}: {num}")
        

