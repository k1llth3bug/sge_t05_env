from datetime import date
class Vista:
    def __init__(self, controlador) -> None:
        self.__controlador = controlador

    def mostrar_login(self, usuario) -> None:
        print(f"Usuario: {usuario.get_dni()}")
        print(f"Último acceso: {usuario.get_ultimo_acceso_as_str()}")

    def inicio(self, es_admin: bool) -> None:
        if es_admin:
            self.mostrar_opciones_admin()
        else:
            self.mostrar_opciones_socio()

    def error_login(self, login_error) -> None:
        print(login_error)

    def pedir_entero(self, minimo: int, maximo: int) -> int:
        valido = False
        res = 0
        while not valido:
            try:
                res = int(input())
                if minimo <= res <= maximo:
                    valido = True
                else:
                    print(f"No está entre {minimo} y {maximo}, pruebe de nuevo")
            except ValueError:
                print("No es un número entero, pruebe de nuevo")
        return res

    def pedir_decimal_positivo(self) -> float:
        valido = False
        res = 0
        while not valido:
            try:
                res = float(input())
                if res <= 0:
                    print("No es un número válido, pruebe de nuevo")
                else:
                    valido = True
            except ValueError:
                print("No es un número, pruebe de nuevo")
        return res

    def pedir_decimal(self, minimo: float, maximo: float) -> float:
        valido = False
        res = 0
        while not valido:
            try:
                res = float(input())
                if minimo <= res < maximo:
                    valido = True
                else:
                    print(f"No está entre {minimo} y {maximo}, pruebe de nuevo")
            except ValueError:
                print("No es un número, pruebe de nuevo")
        return res

    def pedir_anno(self) -> int:
        print("Dime un año:")
        return self.pedir_entero(2000, 2100)

    def pedir_fecha(self) -> date:
        res = None
        es_valida = False
        while not es_valida:
            anno = self.pedir_anno()
            print("Dime un mes:")
            mes = self.pedir_entero(1, 12)
            print("Dime un día:")
            dia = self.pedir_entero(1, 31)
            try:
                res = date(anno, mes, dia)
                es_valida = True
            except ValueError:
                print("No es una fecha válida, pruebe de nuevo")
        return res

    def validar_respuesta(self, res: str, respuestas: list) -> bool:
        return res.casefold() in [r.casefold() for r in respuestas]

    def operacion_realizada(self, dato: bool) -> None:
        print("Operación realizada correctamente" if dato else "No se ha podido realizar la operación")

    def listar_socios(self, lista_socios: list) -> None:
        print("\n\n".join([repr(s) for s in lista_socios]))

    def pedir_datos_socio(self) -> dict:
        datos_socio = {}
        print("Dime el DNI del nuevo socio:")
        datos_socio["dni"] = input()
        while len(datos_socio["dni"]) == 0:
            print("El DNI no puede estar vacío")
            datos_socio["dni"] = input()
        print("Dime su contraseña:")
        datos_socio["contrasena"] = input()
        while len(datos_socio["contrasena"]) == 0:
            print("La contraseña no puede estar vacía")
            datos_socio["contrasena"] = input()
        print("Dime si es admin o no (s o n):")
        respuesta_admin = input()
        while not self.validar_respuesta(respuesta_admin, ["s", "n"]):
            print("Dime sólo s o n")
            respuesta_admin = input()
        datos_socio["es_admin"] = respuesta_admin.casefold() == "y"
        print("Dime su nombre:")
        datos_socio["nombre"] = input()
        while len(datos_socio["nombre"]) == 0:
            print("El nombre no puede estar vacío")
            datos_socio["nombre"] = input()
        print("Dime su dirección:")
        datos_socio["direccion"] = input()
        print("Dime su teléfono:")
        datos_socio["telefono"] = self.pedir_entero(600000000, 700000000-1)
        print("Dime su email:")
        datos_socio["email"] = input()
        return datos_socio

    def pedir_dni_socio(self) -> str:
        print("Dime el DNI del socio a actualizar:")
        return input()

    def pedir_dni_familiar(self) -> str:
        print("Dime el DNI del familiar:")
        return input()

    def pedir_tipo_familiar(self) -> str:
        print("Dime el tipo de familiar (hijo o pareja):")
        res = input()
        while not self.validar_respuesta(res, ["pareja", "hijo"]):
            print("No es válido, sólo pareja o hijo")
            res = input()
        return res

    def listar_eventos(self, lista_eventos: list) -> None:
        if len(lista_eventos) > 0:
            print("\n".join([repr(ev) for ev in lista_eventos]))
        else:
            print("No hay próximos eventos")

    def pedir_datos_evento(self) -> dict:
        datos_evento = {}
        print("Dime la fecha del evento:")
        datos_evento["fecha"] = self.pedir_fecha()
        print("Dime la fecha de inscripción del evento:")
        datos_evento["fecha_inscripcion"] = self.pedir_fecha()
        print("Dime la localidad:")
        localidad = input()
        while len(localidad) == 0:
            print("Localidad no puede estar vacía, prueba de nuevo")
            localidad = input()
        datos_evento["localidad"] = localidad
        print("Dime la provincia:")
        provincia = input()
        while len(provincia) == 0:
            print("Provincia no puede estar vacía, prueba de nuevo")
            provincia = input()
        datos_evento["provincia"] = provincia
        print("Dime el organizador:")
        organizador = input()
        while len(organizador) == 0:
            print("Organizador no puede estar vacío, prueba de nuevo")
            organizador = input()
        datos_evento["organizador"] = organizador
        print("Dime los kilómetros totales:")
        km_totales = self.pedir_decimal_positivo()
        datos_evento["km_totales"] = km_totales
        print("Dime el precio:")
        precio = self.pedir_decimal_positivo()
        datos_evento["precio"] = precio
        return datos_evento

    def listar_control_cuotas(self, anno: int, control_cuotas: dict) -> None:
        if anno not in control_cuotas:
            print(f"No hay control de cuotas para el año {anno}")
        else:
            datos = control_cuotas[anno]
            print(f"Cuotas de {anno}")
            print(f"Descuento por pareja: {100*datos['descuentos']['pareja']}%, hijos: {100*datos['descuentos']['hijos']}%, ambos: {100*datos['descuentos']['ambos']}%")
            if len(datos["pagos"]) != 0:
                for pago in datos["pagos"]:
                    print(f"Socio {pago['dni']}: {'Pagado' if pago['pagado'] else 'No pagado'}")
            else:
                print(f"No hay pagos para el año {anno}")

    def pedir_datos_cuota(self) -> dict:
        datos = {}
        print("Dime el año:")
        datos["anno"] = self.pedir_entero(2000, 2100)
        datos["descuentos"] = {}
        print("Dime el descuento por pareja:")
        datos["descuentos"]["pareja"] = self.pedir_decimal(0, 1)
        print("Dime el descuento por hijos:")
        datos["descuentos"]["hijos"] = self.pedir_decimal(0, 1)
        print("Dime el descuento por ambos:")
        datos["descuentos"]["ambos"] = self.pedir_decimal(0, 1)
        datos["pagos"] = []
        print("Dime cuántos socios quieres actualizar:")
        num_socios = self.pedir_entero(1, 5)
        for _ in range(0, num_socios):
            print("Dime un dni de socio:")
            dni_socio = input()
            while len(dni_socio.strip()) == 0:
                print("El dni no puede estar vacío ni ser sñolo espacios, pruebe de nuevo")
                dni_socio = input()
            print("Dime si ha pagado este año:")
            pagado = input()
            while not self.validar_respuesta(pagado, ["s", "n"]):
                print("No es una respuesta válida, sólo s o n")
                pagado = input()
            datos["pagos"].append({"dni": dni_socio, "pagado": pagado.casefold() == "y", "fecha_pago": date(datos["anno"], date.today().month, date.today().day)})
        return datos

    def listar_eventos_socio_inscrito(self, lista_eventos_socio_inscrito: list) -> None:
        if len(lista_eventos_socio_inscrito) > 0:
            for ev in lista_eventos_socio_inscrito:
                print(f"Socios inscritos en {ev}:")
                for socio in ev.get_socios_inscritos():
                    print(socio)
        else:
            print("No hay próximos eventos")

    def pedir_num_evento(self, lista_eventos) -> int:
        print("Dime un número de evento")
        return self.pedir_entero(1, len(lista_eventos))

    def listar_bicicletas(self, lista_bicis: list) -> None:
        if len(lista_bicis) > 0:
            print("\n".join([repr(b) for b in lista_bicis]))
        else:
            print("No hay bicicletas")

    def listar_reparaciones(self, reparaciones: dict) -> None:
        for bici, lista_reparaciones in reparaciones.items:
            if len(lista_reparaciones) > 0:
                print(f"La bicicleta {bici} no tiene reparaciones")
            else:
                print(f"Las reparaciones de la bicicleta {bici} son:")
                print("\n".join([repr(r) for r in lista_reparaciones]))

    def pedir_datos_bici(self) -> dict:
        datos_bici = {}
        datos_bici["fecha_compra"] = self.pedir_fecha()
        print("Dime la marca de la bici")
        marca = input()
        while len(marca) == 0:
            print("No puede estar vacía la marca, pruebe de nuevo")
            marca = input()
        datos_bici["marca"] = marca
        print("Dime el modelo de la bici")
        modelo = input()
        while len(modelo) == 0:
            print("No puede estar vacío el modelo, pruebe de nuevo")
            modelo = input()
        datos_bici["modelo"] = modelo
        print("Dime el tipo de la bici")
        tipo = input()
        while len(tipo) == 0:
            print("No puede estar vacío el tipo, pruebe de nuevo")
            tipo = input()
        datos_bici["tipo"] = tipo
        print("Dime el color de la bici")
        color = input()
        while len(color) == 0:
            print("No puede estar vacío el color, pruebe de nuevo")
            color = input()
        datos_bici["color"] = color
        print("Dime el tamaño del cuadro")
        tamano_cuadro = self.pedir_decimal_positivo()
        datos_bici["tamano_cuadro"] = tamano_cuadro
        print("Dime el tamaño de las ruedas")
        tamano_ruedas = self.pedir_decimal_positivo()
        datos_bici["tamano_ruedas"] = tamano_ruedas
        print("Dime el precio")
        precio = self.pedir_decimal_positivo()
        datos_bici["precio"] = precio
        return datos_bici

    def pedir_datos_reparacion(self) -> dict:
        datos_reparacion = {}
        print("Dime la fecha de la reparación:")
        fecha = self.pedir_fecha()
        datos_reparacion["fecha"] = fecha
        print("Dime el coste:")
        coste = self.pedir_decimal_positivo()
        datos_reparacion["coste"] = coste
        print("Dime la descripción:")
        descripcion = input()
        datos_reparacion["descripcion"] = descripcion
        print("Dime un número de categoría:")
        print("\n".join(["1. Ruedas", "2. Frenos", "3. Asiento", "4. Cuadro", "5. Delantera", "6. Trasera", "0. Otros"]))
        num_categoria = self.pedir_entero(0, 6)
        datos_reparacion["num_categoria"] = num_categoria
        return datos_reparacion

    def pedir_num_bicicleta(self, lista_bicis) -> int:
        num = 1
        for bici in lista_bicis:
            print(f"{num}. {bici}")
            num +=1
        print("Dime el número de la bicicleta:")
        return self.pedir_entero(1, len(lista_bicis))

    def listar_familia(self, familia: dict) -> None:
        for tipo, socios in familia.items():
            print(f"{tipo}: {socios}")

    def listar_historico(self, historico: dict) -> None:
        for anno, pagos in historico.items():
            if len(pagos) == 0:
                print(f"No hay pagos para el año {anno}")
            else:
                for pago in pagos:
                    print(f"Fecha de pago: {pago['fecha_pago']}")

    def mostrar_opciones_admin(self) -> None:
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
            if opcion != 0:
                input("Presione una tecla para continuar...")

    def mostrar_opciones_socio(self) -> None:
        opcion = -1
        lista_opciones = ["1. Ver mis próximos eventos y lista de inscritos.","2. Inscribirme a evento.",
        "3. Ver mis bicicletas.","4. Ver mis reparaciones.", "5. Añadir nueva bicicleta.",
        "6. Añadir reparación a bicicleta.", "7. Ver mi familia.", "8. Ver mi histórico.",
        "0. Salir"]
        while opcion != 0:
            print("\n".join(lista_opciones))
            print("Dime una opción: ")
            opcion = self.pedir_entero(0, len(lista_opciones)-1)
            self.__controlador.opciones_socio(opcion)
            if opcion != 0:
                input("Presione una tecla para continuar...")