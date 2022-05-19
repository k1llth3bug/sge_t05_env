from datetime import datetime
from typing import List
from modelo.date_utils import formatear_fecha
from modelo.Reparacion import Reparacion

class Bicicleta:
    def __init__(self, fecha_compra: datetime, marca: str, modelo: str, tipo: str, color: str, tamano_cuadro: float, tamano_ruedas: float, precio: float, lista_reparaciones: List[Reparacion] = []) -> None:
        self.__fecha_compra, self.__marca, self.__modelo, self.__tipo, self.__color = fecha_compra, marca, modelo, tipo, color
        self.__tamano_cuadro, self.__tamano_ruedas, self.__precio, self.__lista_reparaciones = tamano_cuadro, tamano_ruedas, precio, lista_reparaciones

    def get_lista_reparaciones(self) -> List[Reparacion]: 
        return self.__lista_reparaciones

    def add_reparacion(self, reparacion: Reparacion) -> None:
        self.__lista_reparaciones.append(reparacion)

    def __repr__(self) -> str:
        return f"Bicicleta(fecha de compra: {formatear_fecha(self.__fecha_compra)}, marca: {self.__marca}, modelo: {self.__modelo}, tipo: {self.__tipo}, color: {self.__color}, tamaño del cuadro: {self.__tamano_cuadro}, tamaño de las ruedas: {self.__tamano_ruedas}, precio: {self.__precio})"