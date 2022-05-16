from sys import argv
from pathlib import Path
from modelo.Club import Club
from controlador.Controlador import Controlador

if __name__ == "__main__":
    club = Club("Satanases del infierno", "Satanases", "Cuenca")
    match argv:
        case [_,"-u", user, "-p", password]:
            controlador = Controlador(club, user, password, False)
        case [_,"-u", user, "-p", password, "-A"]:
            controlador = Controlador(club, user, password, True)
        case [_]:
            print(f"No hay argumentos. Uso: {Path(argv[0]).name} <-u user> <-p password> [-A]")
        case _:
            print(f"Argumentos incorrectos. Uso: {Path(argv[0]).name} <-u user> <-p password> [-A]")