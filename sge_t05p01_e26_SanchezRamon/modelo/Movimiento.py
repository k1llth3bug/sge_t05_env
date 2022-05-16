from Fecha import Fecha

class Movimiento():
    def __init__(self, cantidad: float, es_ingreso: bool, concepto: str) -> None:
        self.__cantidad , self.__ingreso ,self.__concepto = cantidad, es_ingreso, concepto
        self.__fecha = Fecha.fecha_actual()

    def es_ingreso(self):
        return self.__ingreso

    def get_cantidad(self):
        return self.__cantidad

    def __repr__(self) -> str:
        return f"Movimiento(cantidad: {self.__cantidad}, ingreso: {'Sí' if self.__ingreso else 'No'}, concepto: {self.__concepto}, fecha: {self.__fecha})"

if __name__ == "__main__":
    from os import linesep
    m1, m2 = Movimiento(200, True, "Ingreso"), Movimiento(100, False, "Retirada")
    print(linesep.join(str(x) for x in {m1, m2}))