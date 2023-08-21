def frecuencia_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
def mayor_frecuencia(frecuencia):
    palabra_mas_frecuente = None
    cant_frecuencia = 0
    for palabra, contador in frecuencia.items():
        if contador > cant_frecuencia:
            palabra_mas_frecuente = palabra
            cant_frecuencia = contador
    return (palabra_mas_frecuente, cant_frecuencia)

            
print("\033[H\033[J")  
cadena = input ("Escriba aquí: ")
frecuencia = frecuencia_palabras(cadena)
palabra_mas_frecuente, cant_frecuencia = mayor_frecuencia(frecuencia)
print((palabra_mas_frecuente, cant_frecuencia))