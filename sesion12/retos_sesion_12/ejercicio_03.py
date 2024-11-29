'''
El usuario Jhon Doe esta en una red social sus amigos son:
{Alice, Bob, Charlie, David, Eve}

La usuaria Jess Doe tiene los siguientes amigos
{Alice, Bob,  Frank, Grace}

¿Tienen Jhon y Jess amigos en común?, ¿Cuáles son?
'''
jhon = {
    'Alice', 'Bob', 'Charlie', 'David', 'Eve'
}
jess = {
    'Alice', 'Bob',  'Frank', 'Grace'
}

if jhon & jess:
    print(f"los amigos en comun son: {jhon.intersection(jess)}")
else:
    print("no tienen amigos en comun :(")

