# ************ Zona de Funciones ************ #

def solicitar_numero():
    valor = int(input("Digite un número: "))
    return valor

def evaluar_paridad(valor):
    while valor != 0:
        if valor % 2 == 0:
            mensaje = "El número es par"
        else:
            mensaje = "El número es impar"
        return mensaje

def mostrar_informacion(mensaje):
    print("El número es " + mensaje)
    print("Finalizó el programa")

# ************ Código Principal ************ #

numero = solicitar_numero()
resultado = evaluar_paridad(numero)
mostrar_informacion(resultado)
