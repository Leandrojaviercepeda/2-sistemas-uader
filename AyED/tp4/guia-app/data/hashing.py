
from lista import Lista


def inicializarZonas():
    """
    Inicializa los Vectores para cada zona correspondiente.

    @return zonas: Lista de listas de zonas.
    """
    zonas = []

    uno = [Lista()]
    zonas.append(uno)

    dosDeDos = []
    for i in range(20, 100):
        dosDeDos.append(Lista())

    zonas.append(dosDeDos)

    dosDeTres = []
    for i in range(200, 1000):
        dosDeTres.append(Lista())

    zonas.append(dosDeTres)

    tresDeDos = []
    for i in range(30, 100):
        tresDeDos.append(Lista())

    zonas.append(tresDeDos)

    tresDeTres = []
    for i in range(300, 900):
        tresDeTres.append(Lista())

    zonas.append(tresDeTres)

    return zonas


def hashing(zonas, caracteristica):
    """
    Realiza un hashing sobre la caracteristica.

    @param caracteristica: caracteristica de telefono.
    @return nombreArchivo: retorna el nombre del archivo que se creara para la zona correspondiente.
    """

    primer_caracter = int(str(caracteristica)[0])

    caracteres_restantes = int(str(caracteristica)[1:])

    if primer_caracter == 1:
        return zonas[primer_caracter - 1][caracteres_restantes - 1]  # acceso a la lista "uno"

    if primer_caracter == 2 and len(str(caracteres_restantes)) == 2:
        return zonas[primer_caracter - 1][caracteres_restantes - 20]  # acceso a la lista "dos_de_dos"

    if primer_caracter == 2 and len(str(caracteres_restantes)) == 3:
        return zonas[primer_caracter][caracteres_restantes - 200]  # acceso a la lista "dos_de_tres"

    if primer_caracter == 3 and len(str(caracteres_restantes)) == 2:
        return zonas[primer_caracter][caracteres_restantes - 30]  # acceso a la lista "tres_de_dos"

    if primer_caracter == 3 and len(str(caracteres_restantes)) == 3:
        return zonas[primer_caracter + 1][caracteres_restantes - 300]  # acceso a la lista "tres_de_tres"
