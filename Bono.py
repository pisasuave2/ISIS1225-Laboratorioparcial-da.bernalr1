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


