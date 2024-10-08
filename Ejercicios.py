print ("hola mundo")

# Funciones de inserciÃ³n en single_linked_list

import DataStructures.List from list_node as nodo

def add_first(lst, element):
    """
    Agrega un elemento en la primera posiciÃ³n de la lista lst.
    """
    nuevo = nodo.new_single_node(element)
    nuevo['next'] = lst['first']
    if lst['first'] is None:     
        lst['last'] = nuevo

    lst['first'] = nuevo
    lst['size'] += 1
    return lst

def add_last(lst, element):
    """
    Agrega un elemento en la ultima posiciÃ³n de la lista lst.
    """
    nuevo = nodo.new_single_node( element)
    if lst['first'] is None:     
        lst['first'] = nuevo
    else:
        lst['last']['next'] = nuevo

    lst['last'] = nuevo
    lst['size'] += 1

    return lst

def insert_element(lst, element, pos):
    """
    Inserta el elemento element en la posiciÃ³n pos de la lista.
    Precondicion: 0 <= pos <= lst['size']
    """
    if pos == 0:
        add_first(lst, element)
    elif pos == lst['size']:
        add_last(lst, element)
    else:
        nuevo = nodo.new_single_node(element)
        pos_act = 0
        actual = lst['first']
        while pos_act != (pos â€“ 1):
            actual = actual['next']
            pos += 1

        nuevo['next'] = actual['next']
        actual['next'] = nuevo
        lst['size'] += 1

    return lst


def contar_ocurrencias(my_lst, x):
    """
    Contar el numero de ocurrencias de x al interior de my_lst
    param my_lst: linked list con los numeros
    type my_lst: dict (representa una linked list)
    param x: elemento a contar ocurrencias en la lista
    Return: numero de ocurrencias de x en my_lst
    """
    numero = 0 
    contador = 0 
    actual = my_lst["first"]
    while contador <= my_lst:
        if actual["info"] == x:
            numero+=1
        else:
            None
        actual = actual["next"]
    return numero 




def buscar_mas_repetido(my_lst):
    """
    Buscar el numero que se repite mas veces en la lista my_lst
    param my_lst: list con los numeros
    type my_lst: dict (representa una list)
    Return: numero que se repite más veces en la lista my_lst
    """
    los_mas = {}
    for numero in my_lst:
        if numero in los_mas:
            los_mas[numero] += 1
        else:
            los_mas[numero] = 1 
    return los_mas
    


    def contar_ocurrencias(my_lst, x):
        """Contar el numero de ocurrencias de x al interior de my_lst
    param my_lst: array list con los numeros
    type my_lst: dict (representa un array list)
    param x: elemento a contar ocurrencias en la lista
    Return: numero de ocurrencias de x en my_lst
    """

    contador =0 
    for numero in my_lst:
        if numero == x:
            contador += 1
    return contador


