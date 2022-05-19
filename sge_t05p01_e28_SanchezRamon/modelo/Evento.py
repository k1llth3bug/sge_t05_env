from datetime import date
from modelo.date_utils import formatear_fecha
from typing import List
from modelo.Socio import Socio

class Evento:
    def __init__(self, fecha: date, fecha_inscripcion: date, localidad: str, provincia: str, organizador: str, km_totales: float, precio: float) -> None:
        self.__fecha, self.__fecha_inscripcion, self.__localidad, self.__provincia = fecha, fecha_inscripcion, localidad, provincia
        self.__organizador, self.__km_totales, self.__precio = organizador, km_totales, precio
        self.__lista_socios_inscritos: List[Socio] = []

    def get_fecha(self) -> date:
        return self.__fecha

    def get_organizador(self) -> str:
        return self.__organizador

    def es_valido(self, ev) -> bool:
        return self.__fecha != ev.get_fecha() and self.__organizador != ev.get_organizador()

    def inscribir_socio(self, socio: Socio) -> bool:
        dni_usuario = socio.get_usuario().get_dni()
        for s in self.__lista_socios_inscritos:
            socio_inscrito = s.get_usuario()
            if dni_usuario == socio_inscrito.get_dni():
                return False
        self.__lista_socios_inscritos.append(socio)
        return True

    def __repr__(self) -> str:
        return f"Evento(fecha: {formatear_fecha(self.__fecha)}, inscripción: {formatear_fecha(self.__fecha_inscripcion)}, localidad: {self.__localidad}, provincia: {self.__provincia}, organizador: {self.__organizador}, km totales: {self.__km_totales}, precio: {self.__precio})"