def crear_lista_bidimensional():
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))

    lista_bidimensional = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Introduce el elemento en la posición ({i+1}, {j+1}): "))
            fila.append(elemento)
        lista_bidimensional.append(fila)

    return lista_bidimensional

def contar_numeros(lista_bidimensional):
    menor_cero = 0
    mayor_cero = 0
    igual_cero = 0

    for fila in lista_bidimensional:
        for elemento in fila:
            if elemento < 0:
                menor_cero += 1
            elif elemento > 0:
                mayor_cero += 1
            else:
                igual_cero += 1

    return menor_cero, mayor_cero, igual_cero

if __name__ == "__main__":
    lista_bidimensional = crear_lista_bidimensional()

    menor_cero, mayor_cero, igual_cero = contar_numeros(lista_bidimensional)

    print("\nResultados:")
    print(f"Números menores a cero: {menor_cero}")
    print(f"Números mayores a cero: {mayor_cero}")
    print(f"Números iguales a cero: {igual_cero}")

# Comprobamos si se ha generado un archivo bytecode (.pyc) durante la ejecución.
# Python compila módulos a bytecode para mejorar la velocidad de ejecución.
# Si encuentras un archivo con la extensión .pyc en el directorio, significa que Python lo ha generado.
