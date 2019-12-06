

def busquedaBinaria(lista, item):
    """Realiza una busqueda binaria.

    Args:
        lista -- conjunto de elementos [].
        item -- elemento buscado en el conjunto.

    Returns:
        True si se encuentra, False caso contrario.
    """

    primero = 0
    ultimo = len(lista) - 1
    encontrado = False

    while primero <= ultimo and not encontrado:
        puntoMedio = (primero + ultimo) // 2
        if lista[puntoMedio] == item:
            encontrado = True
        else:
            if item < lista[puntoMedio]:
                ultimo = puntoMedio - 1
            else:
                primero = puntoMedio + 1

    return encontrado


listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(busquedaBinaria(listaPrueba, 3))
print(busquedaBinaria(listaPrueba, 13))