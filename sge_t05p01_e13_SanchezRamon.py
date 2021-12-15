def imprimir_triangulo(longitud: int) -> str:
    """Devuelve un triángulo de numeros impares ordenados descendentemente y líneas crecientes"""
    if not (longitud % 2 == 0):
        res = ""
        for i in range(1, longitud+2, 2):
            res+=f"{' '.join(str(j) for j in range(i, -1, -2))}"
            if not(i == longitud): res+= "\n"
        return res
    else:
        return "No se pueden pasar números pares"

print(imprimir_triangulo(int(input("Dime un número: "))))