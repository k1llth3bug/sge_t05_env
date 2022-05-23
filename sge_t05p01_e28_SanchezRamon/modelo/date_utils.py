from datetime import date, datetime, timedelta

def formatear_fecha(fecha: datetime | date) -> str:
    """Devuelve una fecha formateada en ISO"""
    return fecha.isoformat()

def es_posterior_o_igual(fecha1: date, fecha2: date) -> bool:
    """Devuelve si la primera fecha es igual o posterior a la segunda"""
    return fecha1 - fecha2 > timedelta(0)