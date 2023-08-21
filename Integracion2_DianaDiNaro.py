numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: ")) 

def mcm (numero1, numero2):
    
    if numero1 > numero2:
        num_mayor = numero1
    else:
        num_mayor = numero2
        
    while (num_mayor % numero1) != 0 or (num_mayor % numero2) != 0:
        num_mayor += 1
    return num_mayor
        
print("\033[H\033[J")  
print (f"El mínimo común multiplo entre ambos números es: {mcm (numero1, numero2)} ")   
