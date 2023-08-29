import random

# Funcion auxiliar para crear una matriz aleatoria
def crear_matriz() -> list:
        
    n_filas = int(input("\nInserte el numero de filas para la matriz: "))
    n_columnas = int(input("Inserte el numero de columnas para la matriz: "))
    
    print("\n")
    
    matriz = []

    print("Matriz resultante: ")
    for i in range(0, n_filas):
        fila = []
        for i in range(0, n_columnas):
            fila.append(random.randint(0, 10))
        matriz.append(fila)
        print(fila)

    print("\n")

    return matriz

# Funcion auxiliar para crear un arreglo aleatorio
def crear_arreglo() -> list:
        
    n = int(input("\nInserte la cantidad de numeros que desea en el arreglo: "))
    
    print("\n")
    
    arreglo = []

    print("Arreglo resultante: ")
    for i in range(0, n):
        arreglo.append(random.randint(0, 10))
    print(arreglo)

    print("\n")

    return arreglo

def a(matriz: list) -> int:

    indice = -1
    sumatoria = 0
    n = len(matriz)-1
    while indice < n:
        indice += 1
        sumatoria += matriz[indice][indice]

    return sumatoria

def b(matriz: list, entero: int) -> bool:

    esta = False

    if len(matriz) != 0:

        fila = 0
        columna = 0
        n_filas = len(matriz)
        n_columnas = len(matriz[0])

        while fila < n_filas and columna < n_columnas:

            if matriz[fila][columna] == entero:
                esta = True

            if columna == n_columnas-1:
                columna = 0
                fila += 1
            
            elif columna < n_columnas-1:
                columna += 1

    return esta

def c(arreglo: list, entero: int) -> bool:

    esta = False

    if len(arreglo) != 0:

        len_arreglo = len(arreglo)
        indice = 0

        while indice < len_arreglo:
            if arreglo[indice] == entero:
                esta = True
            indice += 1
        
    return esta
        
# Descomente la siguiente linea para ejecutar la función a  
#print("La suma de la diagonal en la matriz anterior es: " + str(a(crear_matriz())) + "\n")

# Descomente la siguiente linea para ejecutar la función b
#print("El número ingresado se encuentra en la matriz anterior\n") if b(crear_matriz(), 7) else print("El numero ingresado no se encuentra en la matriz anterior\n")

# Descomente la siguiente linea para ejecutar la función c
#print("El número ingresado se encuentra en el arreglo anterior\n") if c(crear_arreglo(), 7) else print("El numero ingresado no se encuentra en el arreglo anterior\n")