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
    def __init__(self, nombre, edad, dni, titular, cantidad):
        super().__init__(nombre, edad, dni)
        self.titular = titular
        self.cantidad = cantidad

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a 0")
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
            raise ValueError("No se puede retirar más de lo que hay en la cuenta")
        else:
            self.cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, nombre, edad, dni, titular, cantidad, bonificacion):
        super().__init__(nombre, edad, dni, titular, cantidad)
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def asignar_bonificacion(self):
        if self.edad >= 18 and self.edad < 25:
            self.cantidad += float((self.cantidad * self.bonificacion) / 100)
        else:
            self.cantidad += 0

    def retirar(self, cantidad):
        if cantidad > self.cantidad:
            raise ValueError("No se puede retirar más de lo que hay en la cuenta")
        else:
            self.cantidad -= cantidad

    def mostrar(self):
        if self.edad >= 18 and self.edad < 25:
            print(f"Cuenta Joven: {self.nombre} - Bonificación: {self.bonificacion}% - Saldo total: {self.cantidad}")
        else:
            print(f"{self.nombre} no puede acceder al beneficio")

print("\033[H\033[J")  
cuentajoven1 = CuentaJoven("Juan Sinatra", 22, "41555666", "Juan Sinatra", 1000, 10)
cuentajoven1.asignar_bonificacion()
cuentajoven1.mostrar()