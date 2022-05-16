from typing import List
from Movimiento import Movimiento

class Cuenta():
    num_cuenta=1
    def __init__(self, dni_titular: str = "", saldo: float = 0, lista_movimientos : List[Movimiento] = []) -> None:
        if not Cuenta.__es_dni_valido(dni_titular):
            raise ValueError(f"{dni_titular} no es un DNI válido")
        Cuenta.num_cuenta+=1
        self.__dni_titular, self.__saldo, self.__lista_movimientos = dni_titular, saldo, lista_movimientos

    @staticmethod
    def __es_dni_valido(dni: str) -> bool:
        """Devuelve si un DNI es válido"""
        if len(dni) == 9:
            dni = dni.upper()
            letras = "TRWAGMYFPDXBNJZSQVHLCKE"
            return dni[:-1].isnumeric() and 1e6 <= int(dni[:-1]) < 1e8 and letras[int(dni[:-1])%23] == dni[8]
        else:
            return False

    def get_dni_titular(self):
        return self.__dni_titular

    def hacer_movimiento(self, movimiento: Movimiento) -> bool:
        """Devuelve si se puede haver el movimiento, y lo hace si es posible"""
        if not movimiento.es_ingreso():
            if self.__saldo < movimiento.get_cantidad():
                return False
            else:
                self.__saldo -= movimiento.get_cantidad()
                self.__lista_movimientos.append(movimiento)
                return True
        else:
            self.__saldo += movimiento.get_cantidad()
            self.__lista_movimientos.append(movimiento)
            return True

    def __repr__(self) -> str:
        return f"Cuenta(DNI: {self.__dni_titular}, saldo: {self.__saldo})"

if __name__ == "__main__":
    from random import randint
    from os import linesep
    def generar_dni() -> str:
        """Genera un DNI válido"""
        num = randint(1e6,1e8-1)
        letra = "TRWAGMYFPDXBNJZSQVHLCKE"[num % 23]
        return f"{num:08}{letra}"
    c1, c2 = Cuenta(generar_dni(), 2000), Cuenta(generar_dni(), 50000, [Movimiento(200, True, "Test ingresos")])
    print(linesep.join(str(x) for x in [c1, c2]))
