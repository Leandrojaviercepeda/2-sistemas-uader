
import lista as lista
import contacto as contacto
import nodo_archivo as nodo_archivo


def criterio(dato, campo=None):
    """
    Dado un dato, devuelve un registro si este lo contiene. Por defecto devuelve el mismo dato ingresado.

    @param dato: "TDato()".
    @param campo: nombre del campo del dato en forma "str".
    @return "dato.campo". Devuelve el valor almacenado en ese campo si este lo contiene, caso contrario devuelve el dato que se ingreso.
    """
    if type(dato) is lista.Nodo:

        if type(dato.info) is nodo_archivo.NodoArchivo:

            if type(dato.info.info) is contacto.Contacto:

                if (campo == 'Nombre'):
                    return dato.info.info.nombre

                elif (campo == 'Apellido'):
                    return dato.info.info.apellido

                if (campo == 'Caracteristica'):
                    return dato.info.info.telefono.caracteristica

                elif (campo == 'Telefono'):
                    return dato.info.info.telefono

                elif (campo == 'Localidad'):
                    return dato.info.info.localidad

        elif type(dato.info) is contacto.Contacto:

            if (campo == 'Nombre'):
                return dato.info.nombre

            elif (campo == 'Apellido'):
                return dato.info.apellido

            elif (campo == 'Telefono'):
                return dato.info.telefono

            elif (campo == 'Localidad'):
                return dato.info.localidad

    elif type(dato) is nodo_archivo.NodoArchivo:

        if type(dato.info) is contacto.Contacto:

            if (campo == 'Nombre'):
                return dato.info.nombre

            elif (campo == 'Apellido'):
                return dato.info.apellido

            if (campo == 'Caracteristica'):
                return dato.info.telefono.caracteristica

            elif (campo == 'Telefono'):
                return dato.info.telefono

            elif (campo == 'Localidad'):
                return dato.info.localidad

    elif (campo == 'info'):
        return dato.info

    return dato
