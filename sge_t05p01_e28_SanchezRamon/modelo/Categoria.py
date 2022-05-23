from enum import Enum, unique
@unique
class Categoria(Enum):
    RUEDAS = 1
    FRENOS = 2
    ASIENTO = 3
    CUADRO = 4
    DELANTERA = 5
    TRASERA = 6
    OTRAS = 0