from datetime import datetime
from date_utils import formatear_fecha
from Categoria import Categoria

class Reparacion:
    def __init__(self, fecha: datetime, coste: float, descripcion: str, categoria: Categoria) -> None:
        self.__fecha, self.__coste, self.__description, self.__categoria = fecha, coste, descripcion, categoria

    def __repr__(self) -> str:
        return f"Reparación(fecha: {formatear_fecha(self.__fecha)}, coste: {self.__coste}, descripción: {self.__description}, categoría: {self.__categoria})"

if __name__ == "__main__":
    r1 = Reparacion(datetime.now(), 20, "Test", Categoria.OTRAS)
    print(r1)