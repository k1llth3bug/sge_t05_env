from datetime import date
from modelo.date_utils import formatear_fecha
from typing import List
from modelo.Socio import Socio

class Evento:
    def __init__(self, fecha: date, fecha_inscripcion: date, localidad: str, provincia: str, organizador: str, km_totales: float, precio: float, lista_socios_inscritos: List[Socio] = None) -> None:
        self.__fecha, self.__fecha_inscripcion, self.__localidad, self.__provincia = fecha, fecha_inscripcion, localidad, provincia
        self.__organizador, self.__km_totales, self.__precio = organizador, km_totales, precio
        self.__lista_socios_inscritos = lista_socios_inscritos if lista_socios_inscritos is not None else []

    @classmethod
    def from_dict(cls, dict_evento: dict):
        for datos_evento in dict_evento.values():
            return cls(date.fromisoformat(datos_evento["fecha"]), date.fromisoformat(datos_evento["fecha_inscripcion"]), datos_evento["localidad"], datos_evento["provincia"],
            datos_evento["organizador"], datos_evento["km_totales"], datos_evento["precio"], None)

    def to_dict(self):
        return {"fecha":self.__fecha.isoformat(), "fecha_inscripcion":self.__fecha_inscripcion.isoformat(), "localidad":self.__localidad, "provincia":self.__provincia,
        "organizador":self.__organizador, "km_totales": self.__km_totales, "precio": self.__precio, "socios_inscritos": [s.get_usuario().get_dni() for s in self.__lista_socios_inscritos]}

    def get_fecha(self) -> date:
        return self.__fecha

    def get_organizador(self) -> str:
        return self.__organizador

    def get_socios_inscritos(self) -> List[Socio]:
        return self.__lista_socios_inscritos

    def set_socios_inscritos(self, lista_socios: List[Socio]) -> None:
        self.__lista_socios_inscritos = lista_socios

    def es_valido(self, ev) -> bool:
        return self.__fecha != ev.get_fecha() and self.__organizador != ev.get_organizador()

    def inscribir_socio(self, socio: Socio) -> bool:
        if self.check_inscrito(socio.get_usuario().get_dni()):
            return False
        else:
            self.__lista_socios_inscritos.append(socio)
            return True

    def check_inscrito(self, dni_socio: str) -> bool:
        return len([s for s in self.__lista_socios_inscritos if s.get_usuario().get_dni() == dni_socio]) > 0

    def __repr__(self) -> str:
        return f"Evento(fecha: {formatear_fecha(self.__fecha)}, inscripción: {formatear_fecha(self.__fecha_inscripcion)}, localidad: {self.__localidad}, provincia: {self.__provincia}, organizador: {self.__organizador}, km totales: {self.__km_totales}, precio: {self.__precio})"