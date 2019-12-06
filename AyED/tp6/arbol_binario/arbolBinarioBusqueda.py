 #!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Nodo:

    def __init__(self, valor=None):
        self.valor = valor
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.padre = None # puntero al nodo padre en el árbol

    def __str__(self):
        return "{0}".format(self.valor)

    def comparar(self, otro):
        if otro:
            return (self.valor == otro.valor) and (self.siguiente == otro.siguiente)
        else:
            return False

    def __eq__(self, cosa):
        return self.valor == cosa

    def __ne__(self, cosa):
        return self.valor != cosa

    def __lt__(self, cosa):
        if cosa:
            return self.valor < cosa
        return False

    def __gt__(self, cosa):
        if cosa:
            return self.valor > cosa
        return False


class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz == None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodoActual):
        if valor < nodoActual.valor:
            if nodoActual.hijoIzquierdo == None:
                nodoActual.hijoIzquierdo = Nodo(valor)
                nodoActual.hijoIzquierdo.padre = nodoActual # set padre
            else:
                self._insertar(valor, nodoActual.hijoIzquierdo)
        elif valor > nodoActual.valor:
            if nodoActual.hijoDerecho == None:
                nodoActual.hijoDerecho = Nodo(valor)
                nodoActual.hijoDerecho.padre = nodoActual # set padre
            else:
                self._insertar(valor, nodoActual.hijoDerecho)
        else:
            print ("Este valor ya en el árbol!")

    def printArbol(self):
        if self.raiz != None:
            self._printArbol(self.raiz)

    def _printArbol(self,nodoActual):
        if nodoActual != None:
            self._printArbol(nodoActual.hijoIzquierdo)
            print (str(nodoActual.valor))
            self._printArbol(nodoActual.hijoDerecho)

    def altura(self):
        if self.raiz != None:
            return self._altura(self.raiz, 0)
        else:
            return 0

    def _altura(self,nodoActual, alturaActual):
        if nodoActual == None: return alturaActual
        alturaIzquierda = self._altura(nodoActual.hijoIzquierdo, alturaActual+1)
        alturaDerecha = self._altura(nodoActual.hijoDerecho, alturaActual+1)
        return max(alturaIzquierda, alturaDerecha)

    def encontrar(self, valor):
        if self.raiz != None:
            return self._encontrar(valor, self.raiz)
        else:
            return None

    def _encontrar(self, valor,nodoActual):
        if valor == nodoActual.valor:
            return nodoActual
        elif valor < nodoActual.valor and nodoActual.hijoIzquierdo != None:
            return self._encontrar(valor, nodoActual.hijoIzquierdo)
        elif valor > nodoActual.valor and nodoActual.hijoDerecho != None:
            return self._encontrar(valor, nodoActual.hijoDerecho)

    def remover(self, valor):
        return self._remover(self.encontrar(valor))

    def _remover(self, nodo):

        ## -----
        # Mejoras desde la lección anterior

        # Proteger contra la eliminación de un nodo no encontrado en el árbol
        if nodo == None or self.encontrar(nodo.valor) == None:
            print ("El nodo que se quiere eliminar no se encuentra en el árbol!")
            return None
        ## -----

        # devuelve el nodo con valor mínimo en árbol aumentado en el nodo de entrada
        def nodoValorMinimo(nodo):
            nodTemporal = nodo
            while nodTemporal.hijoIzquierdo != None:
                nodTemporal = nodTemporal.hijoIzquierdo
            return nodTemporal

        # devuelve el número de hijos para el nodo especificado
        def numeroHijos(nodo):
            numeroHijos = 0
            if nodo.hijoIzquierdo != None: numeroHijos+=1
            if nodo.hijoDerecho != None: numeroHijos+=1
            return numeroHijos

        # hacer que el padre del nodo sea eliminado
        nodoPadre = nodo.padre

        # obtener el número de hijoren del nodo que se eliminará
        nodoHijo = numeroHijos(nodo)

        # romper la operación en diferentes casos en función de la
        # estructura del árbol y nodo a eliminar

        # CASO 1 (el nodo no tiene hijos)
        if nodoHijo == 0:

            # eliminado el nodo de la raíz que eliminaría todo el árbol.
            if nodoPadre != None:
                # eliminar la referencia al nodo del padre
                if nodoPadre.hijoIzquierdo == nodo:
                    nodoPadre.hijoIzquierdo = None
                else:
                    nodoPadre.hijoDerecho = None
            else:
                self.raiz = None

        # CASO 2 (el nodo tiene un hijo único)
        if nodoHijo == 1:

            # obtener el nodo hijo único
            if nodo.hijoIzquierdo != None:
                hijo = nodo.hijoIzquierdo
            else:
                hijo = nodo.hijoDerecho

            # eliminado el nodo de la raíz que eliminaría todo el árbol.
            if nodoPadre != None:
                # reemplazar el nodo que se eliminará con su hijo
                if nodoPadre.hijoIzquierdo == nodo:
                    nodoPadre.hijoIzquierdo = hijo
                else:
                    nodoPadre.hijoDerecho = hijo
            else:
                self.raiz = hijo

            # corregir el puntero del padre en el nodo
            hijo.padre = nodoPadre

        # CASO 3 (el nodo tiene dos hijos)
        if nodoHijo == 2:

            # obtener el sucesor inOrden del nodo eliminado
            sucesor = nodoValorMinimo(nodo.hijoDerecho)

            # copia el valor del sucesor de inOrden al nodo anteriormente
            # sosteniendo el valor que deseamos eliminar
            nodo.valor = sucesor.valor

            # eliminar el sucesor inorder ahora que su valor era
            # copiado en el otro nodo
            self._remover(sucesor)

    def buscar(self, valor):
        if self.raiz != None:
            return self._buscar(valor, self.raiz)
        else:
            return False

    def _buscar(self, valor,nodoActual):
        if valor == nodoActual.valor:
            return True
        elif valor < nodoActual.valor and nodoActual.hijoIzquierdo != None:
            return self._buscar(valor, nodoActual.hijoIzquierdo)
        elif valor > nodoActual.valor and nodoActual.hijoDerecho != None:
            return self._buscar(valor, nodoActual.hijoDerecho)
        return False

