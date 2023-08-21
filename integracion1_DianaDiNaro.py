numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: ")) 

def mcd (numero1, numero2):
    while numero1 % numero2 != 0 :
        resto = numero1 % numero2
        numero1 = numero2
        numero2 = resto
    return numero2

print("\033[H\033[J")  
print (f"El mayor común divisor entre ambos números es: {mcd (numero1, numero2)} ")   
