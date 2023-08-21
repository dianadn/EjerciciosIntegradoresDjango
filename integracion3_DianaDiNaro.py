def frecuencia_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

print("\033[H\033[J")  
cadena = input ("Escriba aquí: ")
frecuencia = frecuencia_palabras(cadena)
print(frecuencia)