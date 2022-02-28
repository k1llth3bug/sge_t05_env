from datetime import datetime
from date_utils import formatear_fecha
from cipher_utils import cifrar_contrasena

class Usuario:
    def __init__(self, dni: str, contrasena: str, ultimo_acceso: datetime, es_admin: bool = False) -> None:
        self.__dni, self.__contrasena, self.__ultimo_acceso , self.__es_admin = dni, contrasena, ultimo_acceso, es_admin

    def get_dni(self) -> str:
        return self.__dni

    def get_socio(self):
        return self.__socio

    def __repr__(self) -> str:
        return f"Usuario(DNI: {self.__dni}, contraseña: {cifrar_contrasena(self.__contrasena)}, último acceso: {formatear_fecha(self.__ultimo_acceso)}, es_admin: {'Si' if self.__es_admin else 'No'})"

if __name__ == "__main__":
    u1 = Usuario("79443146L", "passwd", datetime.now(), es_admin=True)
    print([u1])
