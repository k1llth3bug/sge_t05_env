from datetime import date, datetime

def formatear_fecha(fecha) -> str:
    """Devuelve una fecha formateada en DD/MM/YY"""
    if isinstance(fecha, date):
        return f"{fecha.day:02}/{fecha.month:02}/{fecha.year}"
    elif isinstance(fecha, datetime):
        return f"{fecha.day:02}/{fecha.month:02}/{fecha.year} {fecha.hour:02}:{fecha.minute:02}:{fecha.second:02}"

def es_posterior_o_igual(fecha1: date, fecha2: date) -> bool:
    """Devuelve si la primera fecha es posterior o igual a la segunda"""
    return fecha1.year >= fecha2.year and fecha1.month >= fecha2.month and fecha1.day >= fecha2.month