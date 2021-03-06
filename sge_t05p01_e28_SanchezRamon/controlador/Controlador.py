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
                self.__vista.operacion_realizada(self.__club.annadir_socio(self.__vista.pedir_datos_socio()))
            case 3:
                dni_socio = self.__vista.pedir_dni_socio()
                dni_familiar = self.__vista.pedir_dni_familiar()
                tipo_familiar = self.__vista.pedir_tipo_familiar()
                self.__vista.operacion_realizada(self.__club.annadir_socio_familia(dni_socio, dni_familiar, tipo_familiar))
            case 4:
                self.__vista.listar_eventos(self.__club.get_proximos_eventos())
            case 5:
                fecha = self.__vista.pedir_fecha()
                self.__vista.listar_eventos(self.__club.eventos_fecha_exacta(fecha))
            case 6:
                self.__vista.operacion_realizada(self.__club.add_evento(self.__vista.pedir_datos_evento()))
            case 7:
                anno = self.__vista.pedir_anno()
                self.__vista.listar_control_cuotas(anno, self.__club.get_control_cuotas())
            case 8:
                datos_cuota = self.__vista.pedir_datos_cuota()
                self.__club.actualizar_cuotas(datos_cuota["anno"], datos_cuota["descuentos"], datos_cuota["pagos"])
            case 9:
                dni_socio = self.__vista.pedir_dni_socio()
                self.__vista.operacion_realizada(self.__club.realizar_pago(dni_socio))

    def opciones_socio(self, opcion: int) -> None:
        match opcion:
            case 0:
                self.__club.guardar_datos()
            case 1:
                self.__vista.listar_eventos_socio_inscrito(self.__club.get_proximos_eventos_socio(self.__id_usuario))
            case 2:
                eventos_abiertos = self.__club.get_proximos_eventos()
                self.__vista.listar_eventos(eventos_abiertos)
                if len(eventos_abiertos) != 0:
                    self.__vista.operacion_realizada(self.__club.inscribir_socio_evento(self.__vista.pedir_num_evento(eventos_abiertos)-1))
            case 3:
                self.__vista.listar_bicicletas(self.__club.get_listado_bicicletas())
            case 4:
                self.__vista.listar_reparaciones(self.__club.get_listado_reparaciones()) 
            case 5:
                self.__club.add_bicicleta(self.__vista.pedir_datos_bici())
            case 6:
                num_bici = self.__vista.pedir_num_bicicleta(self.__club.get_listado_bicicletas())
                self.__club.add_reparacion(num_bici-1, self.__vista.pedir_datos_reparacion())
            case 7:
                self.__vista.listar_familia(self.__club.get_familia_socio())
            case 8:
                self.__vista.listar_historico(self.__club.get_historico())