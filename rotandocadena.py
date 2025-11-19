r = int(input("ingrese el numero de rotaciones: "))
s = (input("ungrese cualquier texto: "))
sin_espacios= "".join(s.split()) #Quitar los espacios y que tome encuenta 
cantidad = len(sin_espacios) #contar la cantidad de elementos
rotado = sin_espacios #asignar el valor de sin_espacios a una variable
for i in range(r): #para que itere elemeeto por elemento hasta (r)el numero deelementos
    rotado = rotado[-1] + rotado[:-1] #rota desde el final  ejemplo:  
print(f"la rotacion es : {rotado}")
print(f"quitando espacios : {sin_espacios}")
print("EMMA CLARA LAZO LAYME")
#explicacion de la linea 7 
#rotado = "ABCD"
#rotado[-1] = ultima letra = "D" el [-1 ] simepre toma el ultimo elemento
# rotado [:´-1 ] = rotar excepto la ultima letra
#[:-1]significa desde el inicio hasta el penultimo
#todo unido 
#rotado[-1]+ rotado[:-1] = "D" + "ABC" ="DABc"
