import shelve


def abrirArchivo(ruta):
    return shelve.open(ruta)


def cerrarArchivo(archivo):
    archivo.close()


def agregarDato(archivo, dato):
    try:
        archivo[str(len(archivo))] = dato
        return True
    except:
        return None


def leerArchivo(archivo, pos):
    try:
        return archivo[str(pos)]
    except:
        return None


def modificarDato(archivo, pos, dato):
    try:
        archivo[str(pos)] = dato
        return True
    except:
        return None


def borrarRegistro(A, pos):
    del A[str(pos)]


def borrarArchivo(A):
    A.clear()


def qsArchivo(A, inf, sup):
    if ((sup - inf) > 0):
        p = partition(A, inf, sup)
        qsArchivo(A, inf, p-1)
        qsArchivo(A, p+1, sup)


def partition(A, inf, sup):
    divisor = inf
    pivot = sup

    for i in range(inf, sup):
        if (A[str(i)] < A[str(pivot)]):
            A[str(i)], A[str(divisor)] = A[str(divisor)], A[str(i)]
            divisor += 1

    A[str(pivot)], A[str(divisor)] = A[str(divisor)], A[str(pivot)]

    return divisor



def bbArchivo(array, pri, lim, item):
    if (pri > lim):
        return False
    else:
        med = ((pri + lim) // 2)
        if (array[str(med)] == item):
            return med
        elif (array[str(med)] > item):
            return(bbArchivo(array,pri,med-1,item))
        elif (array[str(med)] < item):
            return(bbArchivo(array,med+1,lim,item))
