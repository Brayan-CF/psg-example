'''
Gestión de hábitats en peligro: Crea un diccionario que asocie 
especies animales en peligro de extinción con información sobre 
sus hábitats amenazados, lo que permite priorizar la protección 
de áreas críticas para la supervivencia de estas especies

habitats = {"polo norte" : {"especies": {"oso polar", "morsa", 
        "ballena"}}, "amazonas" : {"especies": {"tigre", "mono", 
"guacamayo"}}}


   * Añade al diccionario de habitats 2 habitats más usando update()
   * Existe en el diccionario de habitats el habitat 'amazonas'?
   * Añade al diccionario de amazonas la especie 'anaconda'

'''
habitats = {
    "polo norte" : {"especies": {"oso polar", "morsa", "ballena"}}, 
    "amazonas" :   {"especies": {"tigre", "mono", "guacamayo"}}
}

habitats.update({
    'pantanos' : {'especies': {'largarto', 'sapos', 'rana'}},
    'altiplano': {'especies': {'huemul', 'huanaco', 'alpaca'}}

})
print(f"Anadido dos habitats mas: {habitats['pantanos']} {habitats['altiplano']}")
existe = 'amazonas' in habitats
print(f"Existe en el diccionario la clave amazonas: {existe}")
habitats.update({
    "amazonas" :   {"especies": {"tigre", "mono", "guacamayo", 'anaconda'}}
})
print(f"Diccionario actualizado: {habitats['amazonas']}")