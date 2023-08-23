import os

def calcular_mcd(a, b):
    """Algoritmo de Euclides utilizado para calcular el Maximo Comun Divisor entre 2 valores"""
    # Supongo 2 valores a, b
    # a/b = q + r donde r es el resto de la division entre a y q
    # Entonces mcd(a,b) = mcd(b,r)
    while b:
        a, b = b, a % b
    return a

def calcular_mcm(a, b):
    return (a * b) // calcular_mcd(a, b)

def contar_palabras(cadena):
    cadena = cadena.lower()
    # por si hay signos de puntuacion
    for puntuacion in '.,?!':
        cadena = cadena.replace(puntuacion, "")

    palabras = cadena.split()
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias

def palabra_mas_repetida(diccionario):
    palabra_mas_comun = None
    frecuencia_mas_alta = 0

    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_mas_alta:
            palabra_mas_comun = palabra
            frecuencia_mas_alta = frecuencia

    return (palabra_mas_comun, frecuencia_mas_alta)

def get_int_iterativo():
    while True:
        try:
            valor = int(input("Ingresa un valor entero: "))
            return valor
        except ValueError:
            print("El valor ingresado no es un entero válido. Inténtalo de nuevo.")

def get_int_recursivo():
    try:
        valor = int(input("Ingresa un valor entero: "))
        return valor
    except ValueError:
        print("El valor ingresado no es un entero válido. Inténtalo de nuevo.")
        return get_int_recursivo()

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

#------------------------------------------------------------------------------------------
# ---------------- MENU DE VISUALIZACION PARA TESTEAR LOS EJERCICIOS ----------------------
#------------------------------------------------------------------------------------------

def ejercicio1():
    print("Escribir una función que calcule el máximo común divisor entre dos números.")
    try:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        print(f"El MCD de {numero1} y {numero2} es {calcular_mcd(numero1, numero2)}")
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")

def ejercicio2():
    print("Escribir una función que calcule el mínimo común múltiplo entre dos números.")
    try:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        print(f"El MCD de {numero1} y {numero2} es {calcular_mcm(numero1, numero2)}")
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")

def ejercicio3():
    print("Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).")
    cadena_usuario = input("Ingrese una cadena de caracteres: ")
    resultado = contar_palabras(cadena_usuario)
    for palabra, frecuencia in resultado.items():
        print(f"{palabra}: {frecuencia}")

def ejercicio4():
    print("Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).")
    print("Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.")
    cadena_usuario = input("Ingrese una cadena de caracteres: ")
    diccionario = contar_palabras(cadena_usuario)
    palabra, frecuencia = palabra_mas_repetida(diccionario)
    print(f"la palabra mas repetida es '{palabra}' cona la frecuencia de {frecuencia}")

def ejercicio5():
    print("Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.")
    print("--------------------------------------------------------------------------------------")
    print("Test de get_int_iterativo(): ")
    int1 = get_int_iterativo()
    print("Test de get_int_recursivo(): ")
    int2 = get_int_recursivo()
    print("--------------------------------------------------------------------------------------")
    print("Pregunta para el lector: ¿Existio alguna diferencia?")
    print(f"Aqui sus numeros: iterativo-> {int1} recursivo-> {int2}")

def ejercicio6():
    print("Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase: ")
    print(" - Un constructor, donde los datos pueden estar vacíos.")
    print(" - Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.")
    print(" - mostrar(): Muestra los datos de la persona.")
    print(" - Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.")
    print("--------------------------------------------------------------------------------------")
    nombre = input("ingrese un nombre de persona: ")
    edad = input("ingrese una edad >= 0 de persona: ")
    dni = input("ingrese un DNI de persona de 7 u 8 digitos: ")
    p = Persona(nombre, edad, dni)
    p.mostrar

def ejercicio7():
    print("7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.")
    print("Crear los siguientes métodos para la clase:")
    print(" - Un constructor, donde los datos pueden estar vacíos.")
    print(" - Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.")
    print(" - mostrar(): Muestra los datos de la cuenta.")
    print(" - ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.")
    print(" - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.")
    nombre = input("ingrese un nombre de persona: ")
    edad = input("ingrese una edad >= 0 de persona: ")
    dni = input("ingrese un DNI de persona de 7 u 8 digitos: ")
    titular = Persona(nombre, edad, dni)
    cantidad = input("ingrese una cantidad: ")
    c = Cuenta(titular, cantidad)
    c.mostrar

def ejercicio8():
    print("Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7.")
    print("Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:")
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

def salir():
    print("Saliendo...")

def menu(opciones, opcion_salida):
    sistema = os.name
    opcion = None
    while opcion != opcion_salida:
        print("--------------------------------------------------------------------------------------")
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        if sistema == 'posix':
            os.system('clear')  # Para sistemas Unix/Linux
        elif sistema == 'nt':
            os.system('cls')    # Para Windows
        ejecutar_opcion(opcion, opciones)

def mostrar_menu(opciones):
    print("Seleccione un ejercicio para testear:")
    for clave in sorted(opciones):
        print(f"{clave}. {opciones[clave][0]}")

def leer_opcion(opciones):
    while(opc := input("Opción: ")) not in opciones:
        print("Opción invalida.")
    return opc

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

opciones = {
    '1': ('Máximo común divisor entre dos números', ejercicio1),
    '2': ('Mínimo común múltiplo entre dos números', ejercicio2),
    '3': ('Conteo frecuencia de palabras', ejercicio3),
    '4': ('Palabra más repetida y su frecuencia', ejercicio4),
    '5': ('get_init() iterativo y recursivo', ejercicio5),
    '6': ('Clase Persona(nombre, edad, dni)', ejercicio6),
    '7': ('Clase Cuenta(titular, cantidad)', ejercicio7),
    '8': ('Clase Cuenta_joven(titular, cantidad, bonificacion)', ejercicio8),
    '9': ('Salir', salir)
}

menu(opciones, '9')