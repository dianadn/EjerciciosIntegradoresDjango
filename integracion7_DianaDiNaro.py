class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre


    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)


class Cuenta(Persona):
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni)
        self.titular = self.nombre
        self.cantidad = (float())

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def mostrar(self):
        print("Titular:", self.titular)
        if self.cantidad > 0:
            print("Cantidad:", self.cantidad)
        else:
            print("Su saldo es 0")

    def ingresar(self, cantidad):
        self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > self.cantidad:
            raise ValueError ("No se puede retirar más de lo que hay en la cuenta")
        else:
            self.cantidad -= cantidad
            
print("\033[H\033[J")  
persona = Persona("Juan Sinatra", 28, "41555666")
persona.mostrar()

cuenta = Cuenta("Juan Sinatra", 28, "41555666")
cuenta.mostrar()
cuenta.ingresar(500.00)
cuenta.mostrar()
cuenta.retirar(200.00)
cuenta.mostrar()
