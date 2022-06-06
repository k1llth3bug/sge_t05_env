from modelo.Club import Club
from modelo.LoginError import LoginError
from vista.Vista import Vista
class Controlador:
    def __init__(self, club: Club, id_usuario: str, contrasena: str, es_admin: bool) -> None:
        self.__club, self.__id_usuario = club, id_usuario
        self.__vista = Vista(self)
        login_error = club.comprobar_usuario(id_usuario, contrasena, es_admin)
        if login_error == LoginError.NO_ERROR:
            self.__vista.mostrar_login(club.get_logged_user())
            club.actualizar_logged_usuario()
            self.__vista.inicio(es_admin)
        else:
            self.__vista.error_login(login_error)

    def opciones_admin(self, opcion: int) -> None:
        match opcion:
            case 0:
                self.__club.guardar_datos()
            case 1:
                self.__vista.listar_socios(self.__club.get_lista_socios())
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

    def opciones_socio(self, opcion: int) -> None:
        match opcion:
            case 0:
                self.__club.guardar_datos()
            case 1:
                self.__vista.listar_eventos_socio_inscrito(self.__club.get_proximos_eventos_socio(self.__id_usuario))
            case 2:
                eventos_abiertos = self.__club.get_proximos_eventos()
                self.__vista.listar_eventos(eventos_abiertos)
                self.__club.inscribir_socio_evento(self.__vista.pedir_num_evento(eventos_abiertos))
            case 3:
                self.__vista.listar_bicicletas(self.__club.get_listado_bicicletas())
            case 4:
                self.__vista.listar_reparaciones(self.__club.get_listado_reparaciones()) 
            case 5:
                #TODO: Añadir bici
                pass
            case 6:
                #TODO: Añadir reparacion
                pass
            case 7:
                self.__vista.listar_familia(self.__club.get_familia_socio())
            case 8:
                #TODO: Ver historico
                pass