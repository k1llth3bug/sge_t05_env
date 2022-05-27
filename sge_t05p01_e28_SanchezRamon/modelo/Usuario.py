from datetime import datetime
from modelo.date_utils import formatear_fecha

class Usuario:
    def __init__(self, dni: str, contrasena: str, ultimo_acceso: datetime = datetime.today(), es_admin: bool = False) -> None:
        self.__dni, self.__contrasena, self.__ultimo_acceso , self.__es_admin = dni, contrasena, ultimo_acceso, es_admin

    def get_dni(self) -> str:
        return self.__dni

    def get_contrasenna(self) -> str:
        return self.__contrasena

    def get_ultimo_acceso(self) -> datetime:
        return self.__ultimo_acceso

    def is_admin(self) -> bool:
        return self.__es_admin

    def set_ultimo_acceso(self, ultimo_acceso: datetime) -> None:
        self.__ultimo_acceso = ultimo_acceso

    @classmethod
    def from_dict(cls, dic_user: dict):
        for dni, datos in dic_user.items():
            return cls(dni, datos["contrasena"], datetime.fromisoformat(datos["ultimo_acceso"]), datos["es_admin"])

    def dict_user(self) -> dict:
        return {self.__dni: {"contrasena": self.__contrasena, "ultimo_acceso": self.__ultimo_acceso.isoformat(), "es_admin": self.__es_admin}}

    def __repr__(self) -> str:
        return f"Usuario(DNI: {self.__dni}, contraseña: {self.__contrasena}, ultimo_acceso: {formatear_fecha(self.__ultimo_acceso).replace('T', ' ')}, es_admin: {'Si' if self.__es_admin else 'No'})"
