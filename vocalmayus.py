frase =input("escriba una frase: ")
vocales = ""
for i in frase:
       if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
          vocales +=i 
          mayusculasvocal = vocales.upper()
# ahora para generar la palabra asi hOlA EmmA
modificado = frase
for i1, i2 in zip(vocales, mayusculasvocal):
    modificado = modificado.replace(i1, i2,1)
print(f"frase modificada {modificado}")
#ejemplo 
# for i1, i2 in zip(vocales, mayusculasvocal):
# lo que hace aqui es buscar las primeras vocales q ya habiamos extraido 
# el i1 sera "a" el (i2)el "A" el "1" es para indicar que lo va a remplazar al i2 por el primero que vea en i1(a)
# digamos hola emma
# como ya sacamos las vocales son = o,a,e,a
# entonces el i1 ="a" el i2 = "A" el 1 le dice por el i1 "a" cambialo por i2 "A"
# asi unimos tod      
   