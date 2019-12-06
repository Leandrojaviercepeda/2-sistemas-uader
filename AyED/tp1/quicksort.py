"""Quicksort.

    Se utilizan dos índices: inf, al que llamaremos índice izquierdo, y sup, al que llamaremos índice derecho.

    El algoritmo es el siguiente:

    Recorrer la lista simultáneamente con inf y sup: por la izquierda con inf (desde el primer elemento), y por la derecha
    con sup (desde el último elemento).
    Cuando lista[inf] sea mayor que el pivote y lista[sup] sea menor, se intercambian los elementos en esas posiciones.
    Repetir esto hasta que se crucen los índices.
    El punto en que se cruzan los índices es la posición adecuada para colocar el pivote, porque sabemos que a un lado
    los elementos son todos menores y al otro son todos mayores (o habrían sido intercambiados).
"""

from random import randrange


def quickSort(A):
    quickSort2(A, 0, len(A) - 1)


def quickSort2(A, inf, sup):
    if inf < sup:
        p = partition(A, inf, sup)
        quickSort2(A, inf, p - 1)
        quickSort2(A, p + 1, sup)


def partition(A, inf, sup):
    pivotIndice = getPivot(A, inf, sup)
    pivotValor = A[pivotIndice]
    A[pivotIndice], A[inf] = A[inf], A[pivotIndice]
    borde = inf

    for i in range(inf, sup + 1):
        if A[i] < pivotValor:
            borde += 1
            A[i], A[borde] = A[borde], A[i]
    A[inf], A[borde] = A[borde], A[inf]

    return (borde)


def getPivot(A, inf, sup):
    med = (sup + inf) // 2
    pivot = sup
    if A[inf] < A[med]:
        if A[med] < A[sup]:
            pivot = med
    elif A[inf] < A[sup]:
        pivot = inf
    return pivot


A = [randrange(0, 100) for _ in range(10)]
print("Lista desordenada: ", A, "\n")
quickSort(A)
print("Lista ordenada: ", A, "\n")
