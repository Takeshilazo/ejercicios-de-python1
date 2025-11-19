numero =input("escriba su telefono con prefijo numero y extension : ")
prefijo = numero[3:-3]#combina el para quitar adelante y el de atras 
# numero [:3] #"para eliminar de adelante"
# numero [:-3] "slicing"con indices negativos elimina los ultimos caracteres
print(f"el numero de telefono es{prefijo}")