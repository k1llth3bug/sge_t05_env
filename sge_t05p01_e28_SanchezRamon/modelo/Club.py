from typing import List
from Socio import Socio
from Evento import Evento
from Usuario import Usuario
from datetime import date
from date_utils import es_posterior_o_igual

class Club:
    def __init__(self, nombre: str, cif: str, sede_social: str, lista_socios : List[Socio] = [], lista_eventos: List[Evento] = []) -> None:
        self.__nombre, self.__cif, self.__sede_social, self.__lista_socios, self.__lista_eventos = nombre, cif, sede_social, lista_socios, lista_eventos

    def get_proximos_eventos(self) -> List[Evento]:
        return [ev for ev in self.__lista_eventos if es_posterior_o_igual(ev.get_fecha(), date.today())]

    def annadir_evento(self, ev: Evento) -> bool:
        for evento in self.__lista_eventos:
            if not evento.es_valido(ev):
                return False
        self.__lista_eventos.append(ev)
        return True

    def es_usuario_valido(self, dni: str, contrasena: str, es_admin: bool):
        for socio in self.__lista_socios:
            if(socio.get_usuario().es_valido(dni, contrasena, es_admin)):
                return True
        return False

    def get_lista_socios(self) -> None:
        return self.__lista_socios

    def __repr__(self) -> str:
        return f"Club(nombre: {self.__nombre}, cif: {self.__cif}, sede_social: {self.__sede_social})"

if __name__ == "__main__":
    c1 = Club("Satanases del infierno", "Satanases", "Cuenca")
    c1.annadir_evento(Evento(date(2022, 6, 1), date(2022, 6, 25), "Cuenca", "Cuenca", "Alejandro M.", 0, 100))
    c1.annadir_evento(Evento(date(2022, 5, 1), date(2022, 5, 10), "Toledo", "Toledo", "Juan J.", 0, 150))
    print(c1.get_proximos_eventos())