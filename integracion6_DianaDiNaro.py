class Persona:
    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_dni(self):
        return self.dni
    
    def set_nombre(self,nombre):
        self.nombre = nombre
        if nombre is None:
            raise ValueError("El nombre no puede estar vacío")
        if not nombre.isalpha() and nombre.split(" "):
            raise ValueError("Ingrese nombre y apellido")
        self.nombre = nombre
        
    def set_edad(self,edad):
        self.edad = edad
        if edad is None:
            raise ValueError("La edad no puede estar vacía")
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años.")
        
               
    def set_dni(self,dni):
        self.dni = dni
        if dni is None:
            raise ValueError("El DNI no puede estar vacío")
        if len(dni) != 8:
            raise ValueError("El DNI debe tener 8 números")
        if not dni.isdigit():
            raise ValueError("El DNI debe contener solo números")
                
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
        
    def mayor(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

         
print("\033[H\033[J")     
persona1 = Persona("Juan Perez", 38, 31500500)
persona1.mostrar()
persona1.mayor()



