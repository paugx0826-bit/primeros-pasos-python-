# ************ Zona de Funciones ************ #

def solicitar_mes():
    valor = int(input("Digite un número del 1 al 12: "))
    return valor

def obtener_nombre_mes(valor_mes):
    match valor_mes:
        case 1:
            return "Enero"
        case 2:
            return "Febrero"
        case 3:
            return "Marzo"
        case 4:
            return "Abril"
        case 5:
            return "Mayo"
        case 6:
            return "Junio"
        case 7:
            return "Julio"
        case 8:
            return "Agosto"
        case 9:
            return "Septiembre"
        case 10:
            return "Octubre"
        case 11:
            return "Noviembre"
        case 12:
            return "Diciembre"
        case _:
            return "Número inválido"

def mostrar_mes(nombre_mes):
    print("El nombre de tu mes es:", nombre_mes)

# ************ Código Principal ************ #

numero = solicitar_mes()
mes = obtener_nombre_mes(numero)
mostrar_mes(mes)
