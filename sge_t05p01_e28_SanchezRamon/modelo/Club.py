from typing import List
from modelo.Socio import Socio
from modelo.Evento import Evento
from datetime import date
from modelo.date_utils import es_posterior_o_igual
from os.path import exists
from json import dump, load
from modelo.Usuario import Usuario
from modelo.LoginError import LoginError
ARCHIVO_USUARIOS = "usuarios.json"
ARCHIVO_SOCIOS = "socios.json"
ARCHIVO_EVENTOS = "eventos.json"

class Club:
    def __init__(self, nombre: str, cif: str, sede_social: str, lista_socios : List[Socio] = None, lista_eventos: List[Evento] = None) -> None:
        self.__nombre, self.__cif, self.__sede_social = nombre, cif, sede_social 
        self.__lista_socios = [] if lista_socios is None else lista_socios
        self.__lista_eventos = [] if lista_eventos is None else lista_eventos
        self.__logged_user = None
        self.comprobar_archivos()

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
        usuarios = [socio.get_usuario() for socio in self.__lista_socios if socio.get_usuario().get_dni() == dni]
        if len(usuarios) == 0:
            return LoginError.USER_ERROR
        elif usuarios[0].get_contrasenna() != contrasena:
            return LoginError.PASSWORD_ERROR
        elif usuarios[0].is_admin() != es_admin:
            return LoginError.PERMISSION_ERROR
        else:
            self.__logged_user = usuarios[0]
            return LoginError.NO_ERROR

    def get_logged_user(self) -> Usuario:
        return self.__logged_user

    def get_lista_socios(self) -> List[Socio]:
        return self.__lista_socios

    def __repr__(self) -> str:
        return f"Club(nombre: {self.__nombre}, cif: {self.__cif}, sede_social: {self.__sede_social})"