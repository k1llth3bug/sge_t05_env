from typing import List
from Socio import Socio
from Evento import Evento
from datetime import datetime, date
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

if __name__ == "__main__":
    c1 = Club("Satanases del infierno", "Satanases", "Cuenca")
    c1.annadir_evento(Evento(datetime(2022, 3, 1), datetime(2022, 2, 25), "Cuenca", "Cuenca", "Alejandro M.", 0, 100))
    c1.annadir_evento(Evento(datetime(2022, 2, 1), datetime(2022, 1, 25), "Toledo", "Toledo", "Juan J.", 0, 150))
    print(c1.get_proximos_eventos())