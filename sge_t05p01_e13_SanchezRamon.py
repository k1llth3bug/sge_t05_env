def imprimir_triangulo(longitud: int) -> str:
    if not (longitud % 2 == 0):
        res = ""
        for i in range(1, longitud+2, 2):
            for j in range(i, -1, -2):
                res+= f"{j}"
                if not (j==1): res+=" "
            if not(i == longitud): res+= "\n"
        return res
    else:
        return "No se pueden pasar números pares"

print(imprimir_triangulo(int(input("Dime un número: "))))