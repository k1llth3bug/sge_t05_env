from typing import List
from Cuenta import Cuenta

class Banco():
    def __init__(self, nombre: str="", lista_cuentas: List[Cuenta]=[], saldo_total: float=0) -> None:
        self.__nombre, self.__lista_cuentas, self.__saldo_total = nombre, lista_cuentas, saldo_total

    def existe_cliente(self, dni: str):
        """Devuelve un cliente si existe, sino devuelve None"""
        for cliente in self.__lista_cuentas:
            if cliente.get_dni_titular() == dni:
                return cliente
        return None
        
    def __repr__(self) -> str:
        return f"Banco(nombre: {self.__nombre}, saldo total: {self.__saldo_total})"

if __name__ == "__main__":
    from Movimiento import Movimiento
    from os import linesep
    b1 = Banco("TestBanco", [Cuenta("79443146L", 2000), Cuenta("60064938R", 50000, Movimiento(200, True, "Test"))], 50200)
    b2 = Banco("BancoGP", [Cuenta("46091690N", 500)], 500)
    print(linesep.join(str(x) for x in [b1, b2]))