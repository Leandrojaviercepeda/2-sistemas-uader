 #!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Nodo:
    """Nodo AVL."""

    def __init__(self, clave=None):
        self.clave = clave
        self.hijo_izquierdo = None
        self.hijo_derecho = None
        self.padre = None  # puntero al nodo padre en el árbol
        self.altura = 1  # altura del nodo en árbol NUEVO PARA AVL

    def __str__(self):
        return "{0}".format(self.clave)

    def __eq__(self, cosa):
        return self.clave == cosa

    def __ne__(self, cosa):
        return self.clave != cosa

    def __lt__(self, cosa):
        if cosa:
            return self.clave < cosa
        return False

    def __gt__(self, cosa):
        if cosa:
            return self.clave > cosa
        return False

    def tieneHijoIzquierdo(self):
        return self.hijo_izquierdo

    def tieneHijoDerecho(self):
        return self.hijo_derecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijo_izquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijo_derecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijo_derecho or self.hijo_izquierdo)

    def tieneAlgunHijo(self):
        return self.hijo_derecho or self.hijo_izquierdo

    def tieneAmbosHijos(self):
        return self.hijo_derecho and self.hijo_izquierdo

class ArbolAVL:

    def __init__(self):
        """Constructor"""
        self.raiz = None

    def __repr__(self):

        if self.raiz == None:
            return ''
        contenido = '\n'  # para contener la cadena final
        nodos_actuales = [self.raiz]  # todos los nodos en el nivel actual
        altura_actual = self.raiz.altura  # altura de nodos en el nivel actual
        # separador de tamanio variable entre los elementos
        sep = ' ' * (2**(altura_actual - 1))
        while True:
            altura_actual += -1  # disminuir la altura actual
            if len(nodos_actuales) == 0:
                break
            fila_actual = ' '
            fila_siguiente = ''
            nodos_siguientes = []

            if all(n is None for n in nodos_actuales):
                break

            for n in nodos_actuales:

                if n == None:
                    fila_actual += '   ' + sep
                    fila_siguiente += '   ' + sep
                    nodos_siguientes.extend([None, None])
                    continue

                if n.clave != None:
                    buf = ' ' * int((5 - len(str(n.clave))) / 2)
                    fila_actual += '%s%s%s' % (buf, str(n.clave), buf) + sep
                else:
                    fila_actual += ' ' * 5 + sep

                if n.hijo_izquierdo != None:
                    nodos_siguientes.append(n.hijo_izquierdo)
                    fila_siguiente += ' /' + sep

                else:
                    fila_siguiente += '  ' + sep
                    nodos_siguientes.append(None)

                if n.hijo_derecho != None:
                    nodos_siguientes.append(n.hijo_derecho)
                    fila_siguiente += '\ ' + sep

                else:
                    fila_siguiente += '  ' + sep
                    nodos_siguientes.append(None)

            contenido += (altura_actual * '   ' + fila_actual + '\n' +
                          altura_actual * '   ' + fila_siguiente + '\n')
            nodos_actuales = nodos_siguientes
            # cortar el tamanio del separador por la mitad
            sep = ' ' * int(len(sep) / 2)

        return contenido

    def printArbol(self):

        if self.raiz != None:
            self._print_arbol(self.raiz)

    def _print_arbol(self, nodo_actual):

        if nodo_actual != None:

            self._print_arbol(nodo_actual.hijo_izquierdo)
            print ('%s, Altura: %d' %
                   (str(nodo_actual.clave), nodo_actual.altura))
            self._print_arbol(nodo_actual.hijo_derecho)

    def inOrden(self):

        if self.raiz:
            self._inOrden(self.raiz)

    def _inOrden(self, nodo_actual):

        if nodo_actual:

            self._inOrden(nodo_actual.hijo_izquierdo)
            print ("{0} ".format(nodo_actual))
            self._inOrden(nodo_actual.hijo_derecho)

    def insertar(self, clave):

        if self.raiz == None:
            self.raiz = Nodo(clave)
        else:
            self._insertar(clave, self.raiz)

    def _insertar(self, clave, nodo_actual):

        if clave < nodo_actual.clave:

            if nodo_actual.hijo_izquierdo == None:
                nodo_actual.hijo_izquierdo = Nodo(clave)
                nodo_actual.hijo_izquierdo.padre = nodo_actual  # set padre
                self._inspeccionar_insercion(nodo_actual.hijo_izquierdo)

            else:
                self._insertar(clave, nodo_actual.hijo_izquierdo)

        elif clave > nodo_actual.clave:
            if nodo_actual.hijo_derecho == None:
                nodo_actual.hijo_derecho = Nodo(clave)
                nodo_actual.hijo_derecho.padre = nodo_actual  # set padre
                self._inspeccionar_insercion(nodo_actual.hijo_derecho)

            else:
                self._insertar(clave, nodo_actual.hijo_derecho)
        else:
            print("¡La clave ya esta en el árbol!")

    def altura(self):

        if self.raiz != None:
            return self._altura(self.raiz, 0)

        else:
            return 0

    def _altura(self, nodo_actual, altura_actual):

        if nodo_actual == None:
            return altura_actual

        altura_izquierda = self._altura(
            nodo_actual.hijo_izquierdo, altura_actual + 1)
        altura_derecha = self._altura(
            nodo_actual.hijo_derecho, altura_actual + 1)

        return max(altura_izquierda, altura_derecha)

    def encontrar(self, clave):

        if self.raiz != None:
            return self._encontrar(clave, self.raiz)

        else:
            return None

    def _encontrar(self, clave, nodo_actual):

        if clave == nodo_actual.clave:
            return nodo_actual

        elif clave < nodo_actual.clave and nodo_actual.hijo_izquierdo != None:
            return self._encontrar(clave, nodo_actual.hijo_izquierdo)

        elif clave > nodo_actual.clave and nodo_actual.hijo_derecho != None:
            return self._encontrar(clave, nodo_actual.hijo_derecho)

    def borrar_clave(self, clave):
        return self.borrar_nodo(self.encontrar(clave))

    def borrar_nodo(self, nodo):

        # Proteger contra la eliminación de un nodo no encontrado en el árbol
        if nodo == None or self.encontrar(nodo.clave) == None:
            print("El nodo a eliminar no se encuentra en el árbol!")
            return None

        # devuelve el nodo con clave mínimo en el árbol enraizado en el nodo de entrada
        def min_clave_nodo(n):

            actual = n
            while actual.hijo_izquierdo != None:
                actual = actual.hijo_izquierdo

            return actual

        # devuelve la cantidad de hijos para el nodo especificado
        def num_hijos(n):

            num_hijos = 0
            if n.hijo_izquierdo != None:
                num_hijos += 1
            if n.hijo_derecho != None:
                num_hijos += 1

            return num_hijos

        # obtener el padre del nodo para ser eliminado
        nodo_padre = nodo.padre

        # obtener la cantidad de hijos del nodo que se eliminará
        nodos_hijos = num_hijos(nodo)

        # romper la operación en diferentes casos en función de la
        # estructura del árbol y nodo a eliminar

        # CASO 1 (el nodo no tiene hijos)
        if nodos_hijos == 0:

            if nodo_padre != None:
                # eliminar la referencia al nodo del padre
                if nodo_padre.hijo_izquierdo == nodo:
                    nodo_padre.hijo_izquierdo = None

                else:
                    nodo_padre.hijo_derecho = None
            else:
                self.raiz = None

        # CASO 2 (el nodo tiene un hijo único)
        if nodos_hijos == 1:

            # obtener el nodo hijo único
            if nodo.hijo_izquierdo != None:
                hijo = nodo.hijo_izquierdo

            else:
                hijo = nodo.hijo_derecho

            if nodo_padre != None:
                # reemplace el nodo que se eliminará con su hijo
                if nodo_padre.hijo_izquierdo == nodo:
                    nodo_padre.hijo_izquierdo = hijo

                else:
                    nodo_padre.hijo_derecho = hijo

            else:
                self.raiz = hijo

            # corregir el puntero padre en el nodo
            hijo.padre = nodo_padre

        # CASO 3 (el nodo tiene dos hijos)
        if nodos_hijos == 2:

            # obtener el sucesor inorden del nodo eliminado
            sucesor = min_clave_nodo(nodo.hijo_derecho)

            # Copia el clave del sucesor inorden al nodo anteriormente
            # sosteniendo el clave que deseamos eliminar
            nodo.clave = sucesor.clave

            # eliminar el sucesor inorden ahora que su clave era
            # copiado en el otro nodo
            self.borrar_nodo(sucesor)

            # salir de la función por lo que no llamamos _inspeccionar_insercion dos veces
            return

        if nodo_padre != None:
            # arregla la altura del padre del nodo actual
            nodo_padre.altura = 1 + max(self.get_altura(nodo_padre.hijo_izquierdo),
                                        self.get_altura(nodo_padre.hijo_derecho))

            # comenzar a recorrer una copia de seguridad del árbol comprobando si hay
            # cualquier sección que ahora invalide las reglas de equilibrio de AVL
            self._inspeccionar_eliminacion(nodo_padre)

    def buscar(self, clave):

        if self.raiz != None:
            return self._buscar(clave, self.raiz)

        else:
            return False

    def _buscar(self, clave, nodo_actual):

        if clave == nodo_actual.clave:
            return True

        elif clave < nodo_actual.clave and nodo_actual.hijo_izquierdo != None:
            return self._buscar(clave, nodo_actual.hijo_izquierdo)

        elif clave > nodo_actual.clave and nodo_actual.hijo_derecho != None:
            return self._buscar(clave, nodo_actual.hijo_derecho)

        return False

    # Funciones agregadas para AVL ...
    def _inspeccionar_insercion(self, nodo_actual, camino=[]):

        if nodo_actual.padre == None:
            return

        camino = [nodo_actual] + camino

        altura_izquierda = self.get_altura(nodo_actual.padre.hijo_izquierdo)
        altura_derecha = self.get_altura(nodo_actual.padre.hijo_derecho)

        if abs(altura_izquierda - altura_derecha) > 1:

            camino = [nodo_actual.padre] + camino
            self._rebalance_nodo(camino[0], camino[1], camino[2])

            return

        nueva_altura = 1 + nodo_actual.altura

        if nueva_altura > nodo_actual.padre.altura:

            nodo_actual.padre.altura = nueva_altura

        self._inspeccionar_insercion(nodo_actual.padre, camino)

    def _inspeccionar_eliminacion(self, nodo_actual):

        if nodo_actual == None:
            return

        altura_izquierda = self.get_altura(nodo_actual.hijo_izquierdo)
        altura_derecha = self.get_altura(nodo_actual.hijo_derecho)

        if abs(altura_izquierda - altura_derecha) > 1:

            y = self.taller_hijo(nodo_actual)
            x = self.taller_hijo(y)
            self._rebalance_nodo(nodo_actual, y, x)

        self._inspeccionar_eliminacion(nodo_actual.padre)

    def _rebalance_nodo(self, z, y, x):

        if y == z.hijo_izquierdo and x == y.hijo_izquierdo:
            self._rotar_derecha(z)

        elif y == z.hijo_izquierdo and x == y.hijo_derecho:
            self._rotar_izquierda(y)
            self._rotar_derecha(z)

        elif y == z.hijo_derecho and x == y.hijo_derecho:
            self._rotar_izquierda(z)

        elif y == z.hijo_derecho and x == y.hijo_izquierdo:
            self._rotar_derecha(y)
            self._rotar_izquierda(z)

        else:
            raise Exception(
                '_rebalance_nodo: configuración de nodo z, y, x no reconocida!')

    def _rotar_derecha(self, z):

        sub_raiz = z.padre
        y = z.hijo_izquierdo
        t3 = y.hijo_derecho
        y.hijo_derecho = z
        z.padre = y
        z.hijo_izquierdo = t3

        if t3 != None:
            t3.padre = z
        y.padre = sub_raiz

        if y.padre == None:
            self.raiz = y

        else:
            if y.padre.hijo_izquierdo == z:
                y.padre.hijo_izquierdo = y

            else:
                y.padre.hijo_derecho = y
        z.altura = 1 + max(self.get_altura(z.hijo_izquierdo),
                           self.get_altura(z.hijo_derecho))
        y.altura = 1 + max(self.get_altura(y.hijo_izquierdo),
                           self.get_altura(y.hijo_derecho))

    def _rotar_izquierda(self, z):

        sub_raiz = z.padre
        y = z.hijo_derecho
        t2 = y.hijo_izquierdo
        y.hijo_izquierdo = z
        z.padre = y
        z.hijo_derecho = t2

        if t2 != None:
            t2.padre = z
        y.padre = sub_raiz

        if y.padre == None:
            self.raiz = y

        else:
            if y.padre.hijo_izquierdo == z:
                y.padre.hijo_izquierdo = y

            else:
                y.padre.hijo_derecho = y
        z.altura = 1 + max(self.get_altura(z.hijo_izquierdo),
                           self.get_altura(z.hijo_derecho))
        y.altura = 1 + max(self.get_altura(y.hijo_izquierdo),
                           self.get_altura(y.hijo_derecho))

    def get_altura(self, nodo_actual):

        if nodo_actual == None:
            return 0

        return nodo_actual.altura

    def taller_hijo(self, nodo_actual):

        izquierdo = self.get_altura(nodo_actual.hijo_izquierdo)
        derecho = self.get_altura(nodo_actual.hijo_derecho)

        return nodo_actual.hijo_izquierdo if izquierdo >= derecho else nodo_actual.hijo_derecho

    def insertarElementos(self, elementos):

        for elemento in elementos:
            self.insertar(elemento)