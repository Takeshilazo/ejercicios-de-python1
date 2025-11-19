#DADO UNA CADENA SE PIDE ELIMINAR LAS VOCALES Y DUPLCIAR COSTANTES
def reemplazarvocal(texto):
    if len(texto) == 0:
        return texto
    
    resultado = texto[0]
    
    for i in range(1, len(texto)):
        letra_actual = texto[i]
        
        match letra_actual.lower():
            case 'a' | 'e' | 'i' | 'o' | 'u':
                # Es vocal → reemplazar por la letra anterior
                resultado += texto[i-1]
            case _:
                # Es consonante → mantener igual
                resultado += letra_actual
    
    return resultado
texto = input("escriba una letra: ")
print(f"Original: {texto} modificado {reemplazarvocal(texto)}")
