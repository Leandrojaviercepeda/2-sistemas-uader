import random


def quickSortIterativo(A):
    quickSortIterativo2(A, 0, len(A) - 1)


def quickSortIterativo2(A, inf, sup):
    pila = []
    pila.append((inf, sup))

    # Bucle principal para abrir y empujar elementos hasta que la pila esté vacía
    while pila:
        pos = pila.pop()
        sup, inf = pos[1], pos[0]
        piv = particion(A, inf, sup)
        # Si los elementos en el inf del pivote los empujan a la pila
        if piv - 1 > inf:
            pila.append((inf, piv - 1))
        # Si los elementos en el sup del pivote los empujan a la pila
        if piv + 1 < sup:
            pila.append((piv + 1, sup))


def particion(A, inf, sup):
    piv = A[inf]
    i = inf + 1
    j = sup

    while 1:
        while i <= j and A[i] <= piv:
            i += 1
        while j >= i and A[j] >= piv:
            j -= 1
        if j <= i:
            break

        A[i], A[j] = A[j], A[i]

    A[inf], A[j] = A[j], A[inf]
    return j


lista = random.sample(range(0, 100), 10)
print("Lista desordenada: ", lista, "\n")
quickSortIterativo(lista)
print("Lista ordenada: ", lista)
