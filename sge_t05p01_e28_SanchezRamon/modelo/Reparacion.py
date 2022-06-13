from datetime import date
from modelo.date_utils import formatear_fecha
from modelo.Categoria import Categoria
class Reparacion:
    def __init__(self, fecha: date, coste: float, descripcion: str, categoria: Categoria) -> None:
        self.__fecha, self.__coste, self.__descripcion, self.__categoria = fecha, coste, descripcion, categoria

    @classmethod
    def from_dict(cls, datos_rep: dict):
            return cls(date.fromisoformat(datos_rep["fecha"]), datos_rep["coste"], datos_rep["descripcion"], Categoria(int(datos_rep["categoria"])))

    def dict_reparcion(self):
        return {"fecha": self.__fecha.isoformat(), "coste": self.__coste, "descripcion": self.__descripcion, "categoria": self.__categoria.value}

    def __repr__(self) -> str:
        return f"Fecha: {formatear_fecha(self.__fecha)}, coste: {self.__coste}€, descripción: {self.__descripcion}, categoría: {self.__categoria}"