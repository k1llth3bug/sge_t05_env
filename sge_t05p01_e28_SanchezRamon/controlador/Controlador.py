from modelo.Club import Club
from modelo.LoginError import LoginError
from vista.Vista import Vista
class Controlador:
    def __init__(self, club: Club, id_usuario: str, contrasena: str, es_admin: bool) -> None:
        self.__club = club
        self.__vista = Vista(self)
        login_error = club.comprobar_usuario(id_usuario, contrasena, es_admin)
        if login_error == LoginError.NO_ERROR:
            self.__vista.mostrar_login(club.get_logged_user())
            self.__vista.inicio(es_admin)
        else:
            self.__vista.error_login(login_error)

    def opciones_admin(self, opcion):
        match opcion:
            case 0:
                self.__club.guardar_datos()
            case 1:
                self.__vista.listar_socios(self.__club.get_lista_socios())
                pass
            case 2: 
                #TODO: Insertar socio
                pass
            case 3:
                #TODO: Añadir socio a familia
                pass
            case 4:
                self.__vista.listar_eventos(self.__club.get_proximos_eventos())
            case 5:
                #TODO: Buscar eventos por fecha
                pass
            case 6:
                #TODO: Insertar evento
                pass
            case 7:
                #TODO: Ver control cuotas anual
                pass
            case 8:
                #TODO: Actualizar control cuotas
                pass
            case 9:
                #TODO: Realizar pago cuota
                pass