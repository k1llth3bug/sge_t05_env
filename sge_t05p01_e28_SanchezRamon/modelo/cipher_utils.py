from hashlib import sha256
from hmac import compare_digest

def cifrar_contrasena(passwd: str) -> str:
    """Recibe una contraseña y la devuelve cifrada"""
    return sha256(passwd.encode("UTF-8")).hexdigest()

def verificar_contrasena(passwd: str, sig: str) -> bool:
    """Verifica si una contraseña es correcta o no, devolviendo el resultado de la comparación"""
    return compare_digest(cifrar_contrasena(passwd), sig)

if __name__ == "__main__":
    testHash = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
    print(verificar_contrasena("admin", testHash))