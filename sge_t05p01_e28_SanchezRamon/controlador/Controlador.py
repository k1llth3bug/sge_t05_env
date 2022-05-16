from modelo.Club import Club
from vista.Vista import Vista

class Controlador:
    def __init__(self, club: Club, id_usuario: str, contrasena: str, es_admin: bool) -> None:
        self.__club , self.__id_usuario, self.__contrasena, self.__es_admin = club, id_usuario, contrasena, es_admin
        self.__vista = Vista(self)
        if club.es_usuario_valido(id_usuario, contrasena, es_admin):
            self.__vista.inicio()
        else:
            self.__vista.error_login()
