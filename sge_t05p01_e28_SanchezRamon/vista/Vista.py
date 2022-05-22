class Vista:
    def __init__(self, controlador) -> None:
        self.__controlador = controlador

    def inicio(self, es_admin: bool):
        if es_admin:
            self.mostrar_opciones_admin()
        else:
            self.mostrar_opciones_socio()

    def error_login(self):
        print("Error")

    def mostrar_opciones_admin(self):
        lista_opciones = ["1. Ver listado completo de socios.","2. Insertar un nueco socio.",
        "3. Añadir a un socio su familia.","4. Ver listado completo de los próximos eventos.",
        "5. Buscar eventos por fecha y ver la información.","6. Insertar un nuevo evento.",
        "7. Ver el control de cuotas-socios anual.","8. Actualizar control de cuotas-socios.",
        "9. Realizar el pago de una cuota por DNI del socio.","0. Salir"]
        print("\n".join(lista_opciones))

    def mostrar_opciones_socio(self):
        lista_opciones = ["1. Ver mis próximos eventos y lista de inscritos.","2. Inscribirme a evento.",
        "3. Ver mis bicicletas .","4. Ver mis reparaciones.", "5. Añadir nueva bicicleta.",
        "6. Añadir reparación a bicicleta.", "7. Ver mi familia.", "8. Ver mi histórico.",
        "0. Salir"]
        print("\n".join(lista_opciones))