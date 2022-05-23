from math import hypot

class Punto:
    def __init__(self, x:float = 0, y:float = 0):
        self.__x , self.__y = x, y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __repr__(self) -> str:
        return f"({self.__x}, {self.__y})"

    def cuadrante(self):
        """Devuelve en qué cuadrante o eje está el vector"""
        match self.__x, self.__y:
            case [0, y]:
                if y == 0:
                    return "Origen"
                else:
                    return "Eje Y"
            case [x, 0]:
                if x != 0:
                    return "Eje X"
            case [x,y]:
                if x>=0 and y>=0:
                    return "Primer Cuadrante"
                elif x<=0 and y>=0:
                    return "Segundo Cuadrante"
                elif x<=0:
                    return "Tercer Cuadrande"
                else:
                    return "Cuarto Cuadrante"
    
    def vector(self, other):
        """Devuelve el vector formado por este punto y otro dado"""
        return other.get_x() - self.__x, other.get_y() - self.__y

    def distancia(self, other):
        """Calcula la distancia entre este punto y otro dado"""
        return hypot(self.__x - other.get_x(), self.__y - other.get_y())

class Rectangulo:
    def __init__(self, inicial:Punto = Punto(), final:Punto = Punto()):
        self.__inicial , self.__final = inicial, final

    def es_rectangulo(self) -> bool:
        """Devuelve si los 2 puntos forman una diagonal de rectángulo válida"""
        return not(self.__inicial.get_x() == self.__final.get_x() or self.__inicial.get_y() == self.__final.get_y())

    def get_base(self) -> float:
        """Devuelve la base del rectángulo"""
        return abs(self.__final.get_x() - self.__inicial.get_x())

    def get_altura(self) -> float:
        """Devuelve la altura del rectángulo"""
        return abs(self.__final.get_y() - self.__inicial.get_y())

    def get_area(self) -> float:
        """Devuelve el área del rectángulo"""
        return self.get_base() * self.get_altura()

def pedir_decimal(input_str: str)-> float:
    """Pide al usuario un número decimal, validando el formato"""
    res_str = input(input_str)
    res = 0
    es_decimal = False
    while not es_decimal:
        try:
            res = float(res_str)
            es_decimal = True
        except ValueError:
            print("No es un número, prueba de nuevo")
            res_str = input()
    return res

def pedir_entero(input_str: str)-> int:
    """Pide al usuario un número entero"""
    res_str = input(input_str)
    res = 0
    es_entero = False
    while not es_entero:
        try:
            res = int(res_str)
            es_entero = True
        except ValueError:
            print("No es un número, prueba de nuevo")
            res_str = input()
    return res

def pedir_puntos_distintos() -> tuple:
    """Devuelve 2 puntos distintos pedidos al usuario"""
    x1 = pedir_decimal("Dime la coordenada x del primer punto: ")
    y1 = pedir_decimal("Dime la coordenada y del primer punto: ")
    x2 = pedir_decimal("Dime la coordenada x del segundo punto: ")
    y2 = pedir_decimal("Dime la coordenada y del segundo punto: ")
    while x1 == x2 and y1 == y2:
        print("No pueden ser iguales, introduce las coordenadas del segundo punto de nuevo")
        x2 = pedir_decimal("Dime la primera: ")
        y2 = pedir_decimal("Dime la segunda: ")
    return Punto(x1, y1), Punto(x2, y2)

def mostrar_menu():
    """Muestra un menú de opciones"""
    op1 = """1. Operaciones con puntos:
    a) Mostrar cuadrantes
    b) Calcular vector
    c) Calcular distancia
    d) Salir del submenú"""
    op2 = """2. Operaciones con rectángulos:
    a) Calcular base
    b) Calcular altura
    c) Calcular área
    d) Salir del submenú"""
    op3 = """3. Salir"""
    print("\n".join([op1, op2, op3]))

def opciones_puntos(p1: Punto, p2: Punto):
    """Pide una opción del submenú de puntos, y muestra el resultado correspondiente"""
    op = input("Dime una opción (puntos): ")
    while op != "d":
        match op:
            case "a":
                    print(f"{p1} -> {p1.cuadrante()}, {p2} -> {p2.cuadrante()}")
            case "b":
                print(f"Vector de {p2} a {p1}: {p2.vector(p1)}")
            case "c":
                print(f"Distancia entre {p1} y {p2}: {p1.distancia(p2)}")
            case "d":
                print("Saliendo del submenú")
            case _:
                print("No es una opción válida de punto")
        op = input("Dime otra opción: ")


def opciones_rectangulo(r1: Rectangulo):
    """Pide, si es un rectángulo, una opción del submenú de rectángulo, y muestra el resultado correspondiente"""
    if r1.es_rectangulo():
        op = input("Dime una opción (rectángulo): ")
        while op != "d":
            match op:
                case "a":
                    print(f"Base: {r1.get_base()}")
                case "b":
                    print(f"Altura: {r1.get_altura()}")
                case "c":
                    print(f"Área: {r1.get_area()}")
                case "d":
                    print("Saliendo del submenú")
                case _:
                    print("No es una opción válida de rectángulo")
            op = input("Dime otra opción:")
    else:
        print("No es un rectángulo")

p1, p2 = pedir_puntos_distintos()
opcion = 0
while opcion != 3:
    mostrar_menu()
    opcion = pedir_entero("Dime una opción: ")
    while opcion != 3:
        match opcion:
            case 1:
                opciones_puntos(p1, p2)
            case 2:
                opciones_rectangulo(Rectangulo(p1, p2))
            case 3:
                print("Saliendo...")
            case _:
                print("No es una opción principal válida")
        mostrar_menu()
        opcion = pedir_entero("Dime otra opción: ")