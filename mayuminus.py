#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
nombre = input("escriba su nombre: ")
apellidosList = nombre.split() #convierte a listas en si se van a dividir en listas
mayuscula =nombre.upper()
minuscula = nombre.lower()
apellidosini =nombre.title()
primeraLetra =nombre[0]
for i in apellidosList[1:]: #[1:] omite el primer elemento de la lista que hicimos
      apellidos = i 
apellidosmayus=apellidos.upper()
print(minuscula)
print(mayuscula)
print(f"{primeraLetra} {apellidosmayus}")
print(apellidosini)