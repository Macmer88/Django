
class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre
        # Tal vez innecesario
        self.__edad = edad if edad is None or (isinstance(edad, int) and edad >= 0) else None
        self.__dni = dni if dni is None or len(str(dni)) == 7 or len(str(dni)) == 8 else None

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad debe ser un valor positivo.")
    
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, dni):
        if self.__validar_dni(dni):
            self.__dni = dni
        else:
            print("DNI inválido.")
    
    def __validar_dni(self, dni):
        try:
            dni_str = str(dni)
            cantidad_cifras = len(dni_str)
            return cantidad_cifras == 7 or cantidad_cifras == 8
        except:
            return False
    
    @property
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")
    
    @property
    def es_mayor_de_edad(self):
        return self.__edad >= 18

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def cantidad(self):
        return self.__cantidad
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad+=cantidad
        else:
            print("cantidad invalida")
    
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__cantidad:
            self.__cantidad-=cantidad
        else:
            print("cantidad invalida")
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def mostrar(self):
        print(f"Titular de la cuenta: {self.__titular.nombre}")
        print(f"DNI: {self.__titular.dni}")
        print(f"Edad: {self.__titular.edad}")
        print(f"Cantidad: {self.__cantidad}")

class Cuenta_joven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        return self.__edad >= 18 and self.__edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            self.retirar(cantidad)
        else:
            print("El titular no cumple la restriccion de edad.")

    @property
    def mostrar(self):
        super().mostrar
        print(f"Cuenta joven: Bonificacion {self.__bonificacion}")


    print(" - Un constructor. ")
    print(" - Los setters y getters para el nuevo atributo. ")
    print(" - En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. ") 
    print(" - Además, la retirada de dinero sólo se podrá hacer si el titular es válido. ")
    print(" - El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.")
    nombre = input("ingrese un nombre de persona: ")
    edad = input("ingrese una edad >= 0 de persona: ")
    dni = input("ingrese un DNI de persona de 7 u 8 digitos: ")
    titular = Persona(nombre, edad, dni)
    cantidad = input("ingrese una cantidad: ")
    bonificacion = input("ingrese una bonificacion: ")
    cj = Cuenta_joven(titular, cantidad, bonificacion)
    cj.mostrar
