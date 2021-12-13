lista_numeros = []
while (num := int(input("Dime un número: "))) >=0:
    if num>=0:
        lista_numeros.append(num)
print(f"El valor medio de los números es: {sum(lista_numeros)/len(lista_numeros)}")
