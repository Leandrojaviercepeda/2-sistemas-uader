
"""Guia practica 1: Recursividad"""

#Realizar una funci�n recursiva que calcule los seis primeros t�rminos de la serie de Fibonacci.  0, 1, 1, 2, 3, 5.
def fibonacci(n):
    if (n > 3) and (n <= 6):
        return (fibonacci(n-2)+fibonacci(n-1))
    elif (n == 1):
        return 0
    else:
        return 1

            
#Realizar una funci�n recursiva tal que reciba un n�mero y muestre su factorial.
def factorial(n):
    if n > 1:
        return (n * factorial(n-1))
    else:
        return 1


#Escribir una funci�n recursiva que calcule la suma: 1 + 2 + 3 + 4 + ... + (n-1) + n. 
def sumatoria(n):
    if (n > 0):
        return (n + sumatoria(n-1))
    else:
        return (n)
    
#Escribir una funci�n recursiva que calcule la potencia de un N� entero. 
def potencia(n,y):
    if (y == 0):
        return 1
    else:
        return (n * potencia(n,y-1)) 
    
#Escribir una funci�n recursiva tal que reciba una cadena y devuelva su inversa. 
def cadena_invertida(s):
    if (len(s)>0):
        return (s[-1] + cadena_invertida(s[:-1]))
    else:
        return s

#Obtener un subprograma recursivo que imprima los d�gitos de un n�mero entero positivo en orden inverso.
def entero_invertido(n):
    n = str(n)
    if len(n) > 0:
        return (n[-1] + entero_invertido(n[:-1]))
    else:
        return n

#Obtener un subprograma recursivo de busqueda binaria.
lista = [1,2,3,4,5,6,7,8,9,10]    

def bb(array, pri, lim, item):
    if (pri > lim):
        return False
    else:    
        med = ((pri + lim) // 2)
        if (array[med] == item):
            return item, True
        elif (array[med] > item):
            return(bb(array,pri,med-1,item))
        elif (array[med] < item):
            return(bb(array,med+1,lim,item))