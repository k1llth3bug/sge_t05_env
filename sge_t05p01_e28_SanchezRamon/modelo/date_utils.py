from datetime import date, datetime, timedelta

def formatear_fecha_iso(fecha: datetime | date) -> str:
    """Devuelve una fecha formateada en ISO"""
    return fecha.isoformat()

def formatear_fecha(fecha: datetime | date) -> str:
    if isinstance(fecha, datetime):
        return f"{fecha.day:02}/{fecha.month:02}/{fecha.year} {fecha.hour:02}:{fecha.minute:02}:{fecha.second:02}"
    elif isinstance(fecha, date):
        return f"{fecha.day:02}/{fecha.month:02}/{fecha.year}"    

def es_posterior_o_igual(fecha1: date, fecha2: date) -> bool:
    """Devuelve si la primera fecha es igual o posterior a la segunda"""
    return fecha1 - fecha2 > timedelta(0)