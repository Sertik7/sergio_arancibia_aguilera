from datetime import datetime

def calculo_antiguedad(fecha_ingreso):
    fecha_actual = datetime.now()
    antiguedad = fecha_actual.year - fecha_ingreso.year

    if (fecha_actual.month, fecha_actual.day) < (fecha_ingreso.month, fecha_ingreso.day):
        antiguedad -= 1
        
    return antiguedad

def obtener_beneficio(antiguedad):
    beneficios = []

    if antiguedad >= 5:
        beneficios.append("Se otorgara bono anual")
    if antiguedad >= 3:
        beneficios.append("5 dias adicionales de vacaciones")
    return beneficios