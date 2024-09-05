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
