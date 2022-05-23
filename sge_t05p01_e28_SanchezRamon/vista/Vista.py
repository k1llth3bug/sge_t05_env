class Vista:
    def __init__(self, controlador) -> None:
        self.__controlador = controlador

    def inicio(self, es_admin: bool):
        if es_admin:
            self.mostrar_opciones_admin()
        else:
            self.mostrar_opciones_socio()

    def error_login(self, login_error):
        print(login_error)

    def listar_socios(self, lista_socios):
        print("\n".join([repr(s) for s in lista_socios]))

    def listar_eventos(self, lista_eventos):
        if len(lista_eventos) > 0:
            print("\n".join([repr(ev) for ev in lista_eventos]))
        else:
            print("No hay próximos eventos")

    def pedir_entero(self, minimo, maximo):
        valido = False
        res = 0
        while not valido:
            try:
                res = int(input())
                if minimo <= res <= maximo:
                    valido = True
                else:
                    print(f"No está entre {minimo} y {maximo}")
            except ValueError:
                print("No es un número, pruebe de nuevo")
        return res

    def mostrar_opciones_admin(self):
        opcion = -1
        lista_opciones = ["1. Ver listado completo de socios.","2. Insertar un nuevo socio.",
        "3. Añadir a un socio su familia.","4. Ver listado completo de los próximos eventos.",
        "5. Buscar eventos por fecha y ver la información.","6. Insertar un nuevo evento.",
        "7. Ver el control de cuotas-socios anual.","8. Actualizar control de cuotas-socios.",
        "9. Realizar el pago de una cuota por DNI del socio.", "0. Salir"]
        while opcion != 0:
            print("\n".join(lista_opciones))
            print("Dime una opción: ")
            opcion = self.pedir_entero(0, len(lista_opciones)-1)
            self.__controlador.opciones_admin(opcion)

    def mostrar_opciones_socio(self):
        opcion = -1
        lista_opciones = ["1. Ver mis próximos eventos y lista de inscritos.","2. Inscribirme a evento.",
        "3. Ver mis bicicletas .","4. Ver mis reparaciones.", "5. Añadir nueva bicicleta.",
        "6. Añadir reparación a bicicleta.", "7. Ver mi familia.", "8. Ver mi histórico.",
        "0. Salir"]
        while opcion != 0:
            print("\n".join(lista_opciones))
            print("Dime una opción: ")
            opcion = self.pedir_entero(0, len(lista_opciones)-1)
            self.__controlador.opciones_socio(opcion)