lista_numeros = []
while (num := int(input("Dime un número: "))) >=0:
    lista_numeros.append(num)
if len(lista_numeros) == 0:
    print("No ha introducido nungún número no negativo")
else:
    print(f"El valor medio de los números es: {sum(lista_numeros)/len(lista_numeros)}")
