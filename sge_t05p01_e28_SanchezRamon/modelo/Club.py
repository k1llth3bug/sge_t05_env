from typing import List
from modelo.Socio import Socio
from modelo.Evento import Evento
from datetime import date, datetime
from modelo.date_utils import es_posterior_o_igual
from os.path import exists
from json import dump, load
from modelo.Usuario import Usuario
from modelo.LoginError import LoginError
from modelo.Bicicleta import Bicicleta
from modelo.Reparacion import Reparacion
from modelo.Categoria import Categoria
ARCHIVO_USUARIOS = "usuarios.json"
ARCHIVO_SOCIOS = "socios.json"
ARCHIVO_EVENTOS = "eventos.json"
DESCUENTO_HIJOS_PAREJA = 0.3
DESCUENTO_SOLO_HIJOS = 0.15
DESCUENTO_SOLO_PAREJA = 0.1
class Club:
    def __init__(self, nombre: str, cif: str, sede_social: str, lista_socios : List[Socio] = None, lista_eventos: List[Evento] = None) -> None:
        self.__nombre, self.__cif, self.__sede_social = nombre, cif, sede_social 
        self.__lista_socios = [] if lista_socios is None else lista_socios
        self.__lista_eventos = [] if lista_eventos is None else lista_eventos
        self.__logged_user = None
        self.__logged_socio = None
        self.comprobar_archivos()

    def get_lista_socios(self) -> List[Socio]:
        return self.__lista_socios

    def get_logged_user(self) -> Usuario:
        return self.__logged_user

    def comprobar_archivos(self):
        if exists(ARCHIVO_USUARIOS) and exists(ARCHIVO_SOCIOS) and exists(ARCHIVO_EVENTOS):
            self.__cargar_usuarios_socios()
            self.__cargar_eventos()
        else:
            self.__lista_socios.append(Socio(Usuario("11111111A", "admin", es_admin=True), "admin"))

    def __cargar_usuarios_socios(self) -> None: 
        with open(ARCHIVO_USUARIOS, "r", encoding="UTF-8") as f_users, open(ARCHIVO_SOCIOS, "r", encoding="UTF-8") as f_socios:
            list_usuarios = load(f_users)
            list_socios = load(f_socios)
            for dict_usuario, dict_socio in zip(list_usuarios, list_socios):
                socio = Socio.from_dict(dict_socio)
                socio.set_usuario(Usuario.from_dict(dict_usuario))
                self.__lista_socios.append(socio)
                for socio in self.__lista_socios:
                    self.__actualizar_descuento_socio(socio)

    def __cargar_eventos(self) -> None:
        with open(ARCHIVO_EVENTOS, "r", encoding="UTF-8") as f:
            lista_eventos = load(f)
            for evento in lista_eventos:
                lista_dni_socios = [dni_socio for dni_socio in evento["socios_inscritos"]]
                lista_socios = []
                for dni_socio in lista_dni_socios:
                    lista_socios.append([socio for socio in self.__lista_socios if socio.get_usuario().get_dni() == dni_socio][0])
                ev = Evento.from_dict(evento)
                ev.set_socios_inscritos(lista_socios)
                self.__lista_eventos.append(ev)

    def guardar_datos(self) -> None:
        self.__guardar_socios_usuarios()
        self.__guardar_eventos()

    def __guardar_socios_usuarios(self) -> None:
        lista_usuarios = [socio.get_usuario().dict_user() for socio in self.__lista_socios]
        with open(ARCHIVO_USUARIOS, "w", encoding="UTF-8") as f:
            dump(lista_usuarios, f, indent=4)
        with open(ARCHIVO_SOCIOS, "w", encoding="UTF-8") as f:
            dump([socio.dict_socio() for socio in self.__lista_socios], f, indent=4)

    def __guardar_eventos(self) -> None:
        with open(ARCHIVO_EVENTOS, "w", encoding="UTF-8") as f:
            dump([ev.to_dict() for ev in self.__lista_eventos], f, indent=4)

    def get_proximos_eventos_socio(self, dni_socio) -> List[Evento]:
        return [ev for ev in self.__lista_eventos if es_posterior_o_igual(ev.get_fecha(), date.today()) and ev.check_inscrito(dni_socio)]

    def get_proximos_eventos(self) -> List[Evento]:
        return [ev for ev in self.__lista_eventos if es_posterior_o_igual(ev.get_fecha(), date.today())]

    def annadir_evento(self, ev: Evento) -> bool:
        for evento in self.__lista_eventos:
            if not evento.es_valido(ev):
                return False
        self.__lista_eventos.append(ev)
        return True

    def comprobar_usuario(self, dni: str, contrasena: str, es_admin: bool):
        socios = [socio for socio in self.__lista_socios if socio.get_usuario().get_dni() == dni]
        if len(socios) == 0:
            return LoginError.USER_ERROR
        else:
            usuario = socios[0].get_usuario()
            if usuario.get_contrasenna() != contrasena:
                return LoginError.PASSWORD_ERROR
            elif usuario.is_admin() != es_admin:
                return LoginError.PERMISSION_ERROR
            else:
                self.__logged_user = usuario
                self.__logged_socio = socios[0]
                return LoginError.NO_ERROR

    def actualizar_logged_usuario(self):
        self.__logged_user.set_ultimo_acceso(datetime.now())
        dni_usuario = self.__logged_user.get_dni()
        for socio in self.__lista_socios:
            if socio.get_usuario().get_dni() == dni_usuario:
                socio.set_usuario(self.__logged_user)

    def get_listado_bicicletas(self) -> List[Bicicleta]:
        return self.__logged_socio.get_lista_bicis()

    def add_bicicleta(self, datos_bici: dict) -> None:
        bici = Bicicleta(datos_bici["fecha_compra"], datos_bici["marca"], datos_bici["modelo"],
        datos_bici["tipo"], datos_bici["color"], datos_bici["tamano_cuadro"], datos_bici["tamano_ruedas"],
        datos_bici["precio"])
        self.__logged_socio.add_bici(bici)

    def get_listado_reparaciones(self):
        return self.__logged_socio.get_lista_mantenimientos()

    def get_familia_socio(self) -> dict:
        familia = {}
        familia_socio = self.__logged_socio.get_familia()
        if "pareja" in familia_socio:
            dni_pareja = [dni for dni in familia_socio["pareja"] if dni != self.__logged_user.get_dni()][0]
            familia["pareja"] = [s for s in self.__lista_socios if s.get_usuario().get_dni() == dni_pareja]
        if "hijos" in familia_socio:
            familia["hijos"] = [s for s in self.__lista_socios if s.get_usuario().get_dni() in familia_socio["hijos"]]
        return familia

    def inscribir_socio_evento(self, num_evento: int) -> bool:
        self.get_proximos_eventos()[num_evento].inscribir_socio(self.__logged_socio)

    def annadir_socio(self, datos_socio: dict) -> bool:
        coincidencias_dni = [s for s in self.__lista_socios if s.get_usuario().get_dni() == datos_socio["dni"]]
        if len(coincidencias_dni) == 0:
            usuario = Usuario(datos_socio["dni"], datos_socio["contrasena"], es_admin=datos_socio["es_admin"])
            socio = Socio(usuario, datos_socio["nombre"], datos_socio["direccion"], datos_socio["telefono"], datos_socio["email"])
            self.__lista_socios.append(socio)
            return True
        else:
            return False

    def __actualizar_descuento_socio(self, socio: Socio) -> None:
        familia_socio = socio.get_familia()
        if "hijos" in familia_socio and "pareja" in familia_socio:
            socio.set_descuento(DESCUENTO_HIJOS_PAREJA)
        elif "pareja" in familia_socio:
            socio.set_descuento(DESCUENTO_SOLO_PAREJA)
        elif "hijos" in familia_socio:
            socio.set_descuento(DESCUENTO_SOLO_HIJOS)
        else:
            dni_hijos = [s.get_familia()["hijos"] for s in self.__lista_socios if "hijos" in s.get_familia()]
            for dni_hijo in dni_hijos:
                socios_hijos = [s for s in self.__lista_socios if s.get_usuario().get_dni() in dni_hijo]
                for socio in socios_hijos:
                    socio.set_descuento(DESCUENTO_SOLO_HIJOS)

    def annadir_socio_familia(self, dni_socio: str, dni_familiar: str, tipo_familiar: str) -> bool:
        socio = [s for s in self.__lista_socios if s.get_usuario().get_dni() == dni_socio]
        familiar = [s for s in self.__lista_socios if s.get_usuario().get_dni() == dni_familiar]
        if len(socio) != 0 and len(familiar) != 0:
            if socio[0].annadir_miembro_familia(dni_familiar, tipo_familiar):
                if tipo_familiar == "pareja":
                    familiar[0].annadir_miembro_familia(dni_socio, tipo_familiar)
                self.__actualizar_descuento_socio(socio[0])
                self.__actualizar_descuento_socio(familiar[0])
            return True
        else:
            return False

    def eventos_fecha_exacta(self, fecha: date) -> List[Evento]:
        return [ev for ev in self.__lista_eventos if ev.get_fecha() == fecha]

    def add_reparacion(self, num_bici: int, datos_reparacion: dict) -> None:
        reparacion = Reparacion(datos_reparacion["fecha"], datos_reparacion["coste"], datos_reparacion["descripcion"], Categoria(datos_reparacion["num_categoria"]))
        self.get_listado_bicicletas()[num_bici].add_reparacion(reparacion)

    def add_evento(self, datos_evento: dict) -> bool:
        evento = Evento(datos_evento["fecha"], datos_evento["fecha_inscripcion"], datos_evento["localidad"], datos_evento["provincia"],
        datos_evento["organizador"], datos_evento["km_totales"], datos_evento["precio"])
        for ev in self.__lista_eventos:
            if not ev.es_valido(evento):
                return False
        self.__lista_eventos.append(evento)
        return True

    def __repr__(self) -> str:
        return f"Nombre: {self.__nombre}, cif: {self.__cif}, sede_social: {self.__sede_social}"