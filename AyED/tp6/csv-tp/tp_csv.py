
import csv
from arbol_avl.arbolAvl import ArbolAVL

def cargarArboles(csv_, arbol=ArbolAVL()):
    """Carga un arbol con los datos del archivo csv.

        :argument
            csv -- str(nombre.csv)
    """

    try:
        with open(csv_) as File:
            reader = csv.reader(File, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)

            lista = ['idrisk', 'date', 'time', 'temperature', 'pressure', 'wind', 'humidity',
                    'weather', 'idname']

            for row in reader:
                if row != lista:
                    arbol.insertar(row)

    except FileNotFoundError:
        print('¡Error, el fichero o directorio no existe!')
        raise



datos_clima_csv = 'datos_clima.csv'
arbol_datos_clima = ArbolAVL()
cargarArboles(datos_clima_csv, arbol_datos_clima)
arbol_datos_clima.toString()