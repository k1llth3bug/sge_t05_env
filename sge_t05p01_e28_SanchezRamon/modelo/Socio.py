from typing import List
from modelo.Usuario import Usuario
from modelo.Bicicleta import Bicicleta
from modelo.Reparacion import Reparacion

class Socio:
    def __init__(self, usuario: Usuario, nombre: str = "", direccion: str = "", telefono: int = 6666666666, email: str = "x@x.com", lista_bicicletas: List[Bicicleta] = [], familia: List = []) -> None:
        self.__usuario, self.__nombre, self.__direccion, self.__telefono = usuario, nombre, direccion, telefono
        self.__email, self.__lista_bicicletas, self.__familia = email, lista_bicicletas, familia

    def annadir_miembro_familia(self, miembro):
        self.__familia.append(miembro)

    def get_lista_bicis(self) -> List[Bicicleta]:
        return self.__lista_bicicletas

    def get_lista_mantinimientos(self) -> List[Reparacion]:
        res = []
        for bici in self.__lista_bicicletas:
            res.append(x for x in bici.get_lista_reparaciones())
        return res

    def get_usuario(self) -> Usuario:
        return self.__usuario

    def set_usuario(self, usuario) -> None:
        self.__usuario = usuario

    def __repr__(self) -> str:
        return f"Socio(usuario: {self.__usuario}, nombre: {self.__nombre}, dirección: {self.__direccion}, teléfono: {self.__telefono}, email: {self.__email})"

if __name__ == "__main__":
    from Usuario import Usuario
    from datetime import datetime

    u1 = Usuario("11111111A", "admin", datetime.now(), es_admin=True)
    s1 = Socio(u1, "Ramón", "Tomelloso 46", 666666666, "r@r.com", None)
    print([s1])