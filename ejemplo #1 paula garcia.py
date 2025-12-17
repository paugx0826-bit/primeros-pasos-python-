# ************ Área de Funciones ************ #

def ingresar_numero():
    valor = int(input("Digite un número: "))
    return valor

def evaluar_numero(valor):
    if valor > 0:
        resultado = "El número es Positivo."
    elif valor == 0:
        resultado = "El número es Neutro."
    else:
        resultado = "El número es Negativo."
    return resultado

def mostrar_resultado(resultado):
    print("El número es:", resultado)

# ************ Programa Principal ************ #

numero = ingresar_numero()
mensaje = evaluar_numero(numero)
mostrar_resultado(mensaje)
