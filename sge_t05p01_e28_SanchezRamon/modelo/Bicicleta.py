from datetime import datetime
from typing import List
from modelo.date_utils import formatear_fecha
from modelo.Reparacion import Reparacion

class Bicicleta:
    def __init__(self, fecha_compra: datetime, marca: str, modelo: str, tipo: str, color: str, tamano_cuadro: float, tamano_ruedas: float, precio: float, lista_reparaciones: List[Reparacion] = None) -> None:
        self.__fecha_compra, self.__marca, self.__modelo, self.__tipo, self.__color = fecha_compra, marca, modelo, tipo, color
        self.__tamano_cuadro, self.__tamano_ruedas, self.__precio = tamano_cuadro, tamano_ruedas, precio
        self.__lista_reparaciones = [] if lista_reparaciones is None else lista_reparaciones

    def get_marca(self) -> str:
        return self.__marca

    def get_modelo(self) -> str:
        return self.__modelo

    @classmethod
    def from_dict(cls, dict_bici: dict):
        for datos_bici in dict_bici.values():
            return cls(datetime.fromisoformat(datos_bici["fecha_compra"]), datos_bici["marca"], datos_bici["modelo"], datos_bici["tipo"], datos_bici["color"],
            datos_bici["tamano_cuadro"], datos_bici["tamano_ruedas"], datos_bici["precio"], [Reparacion.from_dict(r) for r in datos_bici["reparaciones"]])

    def dict_bicicleta(self):
        return {"fecha_compra": self.__fecha_compra.isoformat(), "marca": self.__marca, "modelo": self.__modelo, "tipo": self.__tipo, "color": self.__color,
        "tamano_cuadro": self.__tamano_cuadro, "tamano_ruedas": self.__tamano_ruedas, "precio": self.__precio, "reparaciones": [r.dict_reparcion() for r in self.__lista_reparaciones]}

    def get_lista_reparaciones(self) -> List[Reparacion]: 
        return self.__lista_reparaciones

    def add_reparacion(self, reparacion: Reparacion) -> None:
        self.__lista_reparaciones.append(reparacion)

    def __repr__(self) -> str:
        return f"Bicicleta(fecha de compra: {formatear_fecha(self.__fecha_compra)}, marca: {self.__marca}, modelo: {self.__modelo}, tipo: {self.__tipo}, color: {self.__color}, tamaño del cuadro: {self.__tamano_cuadro}, tamaño de las ruedas: {self.__tamano_ruedas}, precio: {self.__precio})"