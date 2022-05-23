from datetime import datetime
from modelo.date_utils import formatear_fecha
from modelo.Categoria import Categoria
class Reparacion:
    def __init__(self, fecha: datetime, coste: float, descripcion: str, categoria: Categoria) -> None:
        self.__fecha, self.__coste, self.__descripcion, self.__categoria = fecha, coste, descripcion, categoria

    def dict_reparcion(self):
        return {"fecha": self.__fecha.isoformat(), "coste": self.__coste, "descripcion": self.__descripcion, "categoria": self.__categoria.value}

    def __repr__(self) -> str:
        return f"Reparación(fecha: {formatear_fecha(self.__fecha)}, coste: {self.__coste}, descripción: {self.__descripcion}, categoría: {self.__categoria})"

if __name__ == "__main__":
    r1 = Reparacion(datetime.now(), 20, "Test", Categoria.OTRAS)
    print(r1)