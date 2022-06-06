from typing import List
from modelo.Usuario import Usuario
from modelo.Bicicleta import Bicicleta

class Socio:
    def __init__(self, usuario: Usuario, nombre: str = "", direccion: str = "", telefono: int = 6666666666, email: str = "", lista_bicicletas: List[Bicicleta] = None, familia: dict = None) -> None:
        self.__usuario, self.__nombre, self.__direccion, self.__telefono = usuario, nombre, direccion, telefono
        self.__email = email
        self.__lista_bicicletas = [] if lista_bicicletas is None else lista_bicicletas
        self.__familia = {} if familia is None else familia

    def annadir_miembro_familia(self, dni_miembro, tipo) -> bool:
        if dni_miembro != self.__usuario.get_dni():
            if tipo == "pareja" and len(self.__familia) == 0 and dni_miembro not in self.__familia["hijos"]:
                self.__familia["pareja"] = dni_miembro
                return True
            elif dni_miembro not in self.__familia["hijos"] and dni_miembro not in self.__familia["pareja"]:
                self.__familia["hijos"].append(dni_miembro)
                return True
        return False

    def get_familia(self) -> dict:
        return self.__familia

    def get_usuario(self) -> Usuario:
        return self.__usuario

    def set_usuario(self, usuario) -> None:
        self.__usuario = usuario

    def get_lista_bicis(self) -> List[Bicicleta]:
        return self.__lista_bicicletas

    @classmethod
    def from_dict(cls, dict_socio: dict):
        for datos in dict_socio.values():
            return cls(None, datos["nombre"], datos["direccion"], datos["telefono"], datos["email"], [Bicicleta.from_dict(b) for b in datos["lista_bicicletas"]], datos["familia"])

    def dict_socio(self):
        return {self.__usuario.get_dni(): {"nombre": self.__nombre, "direccion": self.__direccion, "telefono": self.__telefono, "email": self.__email, "lista_bicicletas": [b.dict_bicicleta() for b in self.__lista_bicicletas], "familia": self.__familia}}

    def get_lista_mantenimientos(self) -> dict:
        res = {}
        for bici in self.__lista_bicicletas:
            res[f"{bici.get_marca()} {bici.get_modelo()}"] = [r for r in bici.get_lista_reparaciones()]
        return res

    def __repr__(self) -> str:
        return f"Socio(usuario: {self.__usuario}, nombre: {self.__nombre}, dirección: {self.__direccion}, teléfono: {self.__telefono}, email: {self.__email})"