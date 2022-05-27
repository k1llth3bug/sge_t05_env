from datetime import datetime
from modelo.date_utils import formatear_fecha
from modelo.Categoria import Categoria
class Reparacion:
    def __init__(self, fecha: datetime, coste: float, descripcion: str, categoria: Categoria) -> None:
        self.__fecha, self.__coste, self.__descripcion, self.__categoria = fecha, coste, descripcion, categoria

    @classmethod
    def from_dict(cls, dict_rep: dict):
        for datos_rep in dict_rep.values():
            return cls(datetime.fromisoformat(datos_rep["fecha"]), datos_rep["coste"], datos_rep["descripcion"], Categoria(datos_rep["categoria"]))

    def dict_reparcion(self):
        return {"fecha": self.__fecha.isoformat(), "coste": self.__coste, "descripcion": self.__descripcion, "categoria": self.__categoria.value}

    def __repr__(self) -> str:
        return f"Reparación(fecha: {formatear_fecha(self.__fecha)}, coste: {self.__coste}, descripción: {self.__descripcion}, categoría: {self.__categoria})"