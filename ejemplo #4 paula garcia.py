# ************ Zona de Funciones ************ #

acumulado = 0

for contador in range(0, 10):
    valor = int(input("Digite el número " + str(contador + 1) + ": "))
    acumulado = acumulado + valor

def mostrar_total(total):
    print("La suma total es:", total)

# ************ Código Principal ************ #

mostrar_total(acumulado)
