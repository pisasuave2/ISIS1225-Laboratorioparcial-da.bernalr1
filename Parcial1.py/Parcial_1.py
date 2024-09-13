def get_sublist_idx(my_list, idx):
    """
    Retorna una sub-lista cada idx posiciones. La posición 0 hace parte de la sub-lista.

    Parameters:
    my_list: La lista a examinar con los equipos inscritos
    type my_list: dict (representando una lista del tipo array list o single linked (como prefiera))
    idx (int): Número del salto de cada cuantos elementos se toma un equipo

    Returns: la sub-lista de la lista original
    return type: dict (representando una lista del mismo tipo que la lista my_list)
    """
    sub_list= []

    if my_list ==None:
        return None

    else:
        priemro = my_list[0]
        sub_list.append(priemro)
        pos = 0
        while pos < my_list["size"]:
            pos +=1
            temp = my_list[idx]
            sub_list.append(temp)
            siguiente = idx + idx
            temp = my_list[siguiente]

    return sub_list

