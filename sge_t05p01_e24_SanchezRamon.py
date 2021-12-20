import re

REGEX_MAIL = re.compile(r"""^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$""", re.IGNORECASE)

def es_nif_valido(nif: str)-> bool:
    """Devuelve si un NIF es válido"""
    if len(nif) == 9:
        nif = nif.upper()
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        return nif[:-1].isnumeric() and letras[int(nif[:-1])%23] == nif[8]
    else:
        return 

def es_telefono_valido(tlfn: str) -> bool:
    """Devuelve si una cadena es un múmero de teléfono válido"""
    return tlfn.isnumeric() and len(tlfn) == 9 and tlfn.startswith(("6","9"))

def add_cliente(clientes: dict):
    """Añade un nuevo cliente pidiendo sus datos"""
    nif = input("Dime un NIF válido: ")
    while not es_nif_valido(nif) or nif in clientes.keys():
        print("No es válido o ya existe, pruebe de nuevo")
        nif = input()
    nombre = input("Dime su nombre: ")
    apellidos = input("Dime sus apellidos: ")
    direccion = input("Dime su dirección: ")
    telefono = input("Dime un número de teléfono: ")
    while not es_telefono_valido(telefono):
        print(f"{telefono} no es un número válido, pruebe de nuevo")
        telefono = input()
    correo = input("Dime su dirección de correo: ")
    while REGEX_MAIL.fullmatch(correo) is None:
        print("No es una dirección de correo válida, pruebe de nuevo")
        correo = input()
    preferente = input("Dime si es preferente(s/S/n/N): ")
    while preferente.lower() not in ["s","n"]:
        print("No es un valor válido, pruebe de nuevo(s/S/n/N)")
        preferente = input()
    clientes[nif] = {"nombre": nombre, "apellidos": apellidos, "direccion": direccion, "telefono": telefono, "correo": correo, "preferente": preferente.lower() == "s"}


def eliminar_cliente(clientes: dict, nif_cliente: str):
    """Elimina, si está, un cliente del diccionario"""
    if nif_cliente in clientes.keys():
        del clientes[nif_cliente]
    else:
        print(f"No hay ningún cliente con NIF {nif_cliente}")

def mostrar_cliente(clientes: dict, nif_cliente: str):
    """Muestra al completo los datos de un cliente si existe, sino muestra un mensaje de error"""
    if nif_cliente in clientes.keys():
        cliente = clientes[nif_cliente]
        print(f"""NIF: {nif_cliente}, nombre completo: {cliente["nombre"]} {cliente["apellidos"]}, dirección: {cliente["direccion"]}, teléfono: {cliente["telefono"]}, correo: {cliente["correo"]}, preferente: {cliente["preferente"]}""")
    else:
        print(f"No hay ningún cliente con NIF {nif_cliente}")

def mostrar_clientes(clientes: dict):
    """Muestra todos los clientes"""
    if len(clientes) == 0:
         print("No hay clientes que mostrar")
    else: 
        for nif in clientes.keys():
            mostrar_cliente(clientes, nif)

def mostrar_preferentes(clientes: dict):
    """Muestra los clientes preferentes"""
    if len(clientes) == 0:
        print("No hay clientes que mostrar")
    else:
        for nif, cliente in clientes.items():
            if cliente["preferente"]:
                mostrar_cliente(clientes, nif)

def ordenar_por_apellidos(clientes: dict):
    """Ordena los clientes por apellidos y los muestra"""
    clientes = dict(sorted(clientes.items(), key=lambda item : item[1]["apellidos"].lower()))
    mostrar_clientes(clientes)

def validar_numero(cadena: str) -> bool:
    """Valida si una cadena es numérica"""
    return cadena[1:].isnumeric() if cadena.startswith(("+","-")) else cadena.isnumeric()

def pedir_nif() -> str:
    """Pide al usuario un nif válido"""
    res = input("Dime un NIF: ")
    while not es_nif_valido(res):
        print("f{nif} no es in nif válido, prueba de nuevo")
        res = input()
    return res

clientes = {}
num = 0
while not num==7:
    print("\n".join(["1. Añadir cliente","2. Eliminar cliente","3. Mostrar cliente","4. Listar clientes","5. Listar clientes preferentes","6. Ordenar alfabéticamente por apellidos","7. Terminar"]))
    num_str = input("Dime un número: ")
    while not validar_numero(num_str):
        print("No es válido, prueba de nuevo")
        num_str = input()
    num = int(num_str)
    match num:
        case 1:
            add_cliente(clientes)
        case 2:
            nif = pedir_nif()
            eliminar_cliente(clientes, nif)
        case 3:
            nif = pedir_nif()
            mostrar_cliente(clientes, nif)
        case 4:
            mostrar_clientes(clientes)
        case 5:
            mostrar_preferentes(clientes)
        case 6:
            ordenar_por_apellidos(clientes)
        case 7:
            print("Saliendo...")
        case _:
            print("No es un número válido, prueba de nuevo")