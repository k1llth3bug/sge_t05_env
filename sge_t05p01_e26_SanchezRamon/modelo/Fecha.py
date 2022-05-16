from datetime import datetime
import logging

class Fecha():
    def __init__(self, dia: int = 0, mes: int = 0, anio: int = 0) -> None:
        self.__dia, self.__mes, self.__anio = dia, mes, anio

    @classmethod
    def fecha_actual(cls):
        """Inicializa la fecha a la actual"""
        fecha = datetime.now()
        return cls(fecha.day, fecha.month, fecha.year)

    @classmethod
    def comprobar_fecha(cls, dia: int, mes: int, anio: int):
        """Comprueba si una fecha es válida, devolviendo la actual si no lo es"""
        try:
            datetime(anio, mes, dia)
            return cls(dia, mes, anio)
        except ValueError as ve:
            logging.warning(ve)
            return Fecha.fecha_actual()

    def __repr__(self) -> str:
        return f"{self.__dia:02}/{self.__mes:02}/{self.__anio}"

if __name__ == "__main__":
    from os import linesep
    f1, f2 = Fecha(29, 2, 2000), Fecha.comprobar_fecha(29, 2, 2006)
    print(linesep.join(str(x) for x in [f1, f2]))