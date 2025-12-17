# ************ Zona de Funciones ************ #

def solicitar_opcion():
    while True:
        print("Presione la letra A para Actualizar el sistema")
        print("Presione la letra E para Eliminar catálogo")
        print("Presione la letra C para Crear productos")
        print("Presione la letra S para Salir del programa")
        opcion = str(input("Seleccione una opción: "))
        return opcion

def evaluar_opcion(opcion):
    if opcion == "A" or opcion == "a":
        respuesta = "Actualizando..."
    elif opcion == "E" or opcion == "e":
        respuesta = "Eliminando Catálogo..."
    elif opcion == "C" or opcion == "c":
        respuesta = "Creando Productos..."
    elif opcion == "S" or opcion == "s":
        respuesta = "Saliendo..."
    else:
        respuesta = "Opción no válida"
    return respuesta

def mostrar_respuesta(respuesta):
    print("Estás", respuesta)

# ************ Código Principal ************ #

letra = solicitar_opcion()
mensaje = evaluar_opcion(letra)
mostrar_respuesta(mensaje)
