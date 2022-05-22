def verificar_contrasena(passwd1: str, passwd2: str) -> bool:
    """Verifica si una contraseña es correcta o no, devolviendo el resultado de la comparación"""
    return passwd1 == passwd2

if __name__ == "__main__":
    testHash = "admin"
    print(verificar_contrasena("admin", testHash))