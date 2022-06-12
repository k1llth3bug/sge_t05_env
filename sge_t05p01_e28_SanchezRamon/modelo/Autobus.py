from datetime import date

class Autobus:
    def __init__(self, fecha_tope: date,carrera: str, min_plazas: int, max_plazas: int, nombre: str) -> None:
        self.__fecha_tope, self.__carrera, self.__min_plazas, self.__max_plazas, self.__nombre = fecha_tope, carrera, min_plazas, max_plazas, nombre

    def __repr__(self) -> str:
        return f"Nombre: {self.__nombre}, plazas mínimas: {self.__min_plazas}, plazas máximas: {self.__max_plazas}, fecha tope: {self.__fecha_tope}, carrera: {self.__carrera}"