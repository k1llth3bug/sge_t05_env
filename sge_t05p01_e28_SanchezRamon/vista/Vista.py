from pathlib import Path
from sys import argv

match argv:
    case [_,"-u", user, "-p", password]:
        print(f"Introducido usuario: {user}, contraseña: {password}, socio")
    case [_,"-u", user, "-p", password, "-A"]:
        print(f"Introducido usuario: {user}, contraseña: {password}, admin")
    case [_]:
        print(f"No hay argumentos. Uso: {Path(argv[0]).name} <-u user> <-p password> [-A]")
    case _:
        print(f"Argumentos incorrectos. Uso: {Path(argv[0]).name} <-u user> <-p password> [-A]")