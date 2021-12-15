import re

REGEX_SYMBOL_GROUP = re.compile(r"""(\W|_)+""")
SYMBOL_GROUP_REPLACER = " "
REGEX_SYMBOLS = re.compile(r"""[\W|_]""")

def contar_letras_y_palabras(cadena: str) -> tuple:
    """Devuelve 2 diccionarios con las palabras contadas y las letras contadas"""
    cadena_sin_simbolos = re.sub(REGEX_SYMBOL_GROUP, SYMBOL_GROUP_REPLACER, cadena.lower()).strip()
    palabras = frozenset(cadena_sin_simbolos.split(SYMBOL_GROUP_REPLACER))
    dicc_pal = {}
    dicc_let = dict.fromkeys('abcdefghijklmnñopqrstuvwxyz')
    for p in palabras:
        dicc_pal[p] = cadena_sin_simbolos.count(p)
    for letra in dicc_let.keys():
        dicc_let[letra] = cadena_sin_simbolos.count(letra)
    dicc_let["no-letra"] = len(re.findall(REGEX_SYMBOLS, cadena))
    return dicc_pal, dicc_let

print(contar_letras_y_palabras("Hola!, que tal. ¿Como esta usted?"))
print(contar_letras_y_palabras.__doc__)