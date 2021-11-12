from Domain.vanzari import creeaza_vanzare, get_id, get_titlu, get_reducere


def adauga_vanzare(id, titlu, gen, pret, reducere, lista):
    """
    Adauga o vanzare de carte intr o lista
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param reducere: string
    :param lista: lista de vanzari
    :return: o lista continand atat elementele vechi, cat si noua vanzare de carte
    """
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    vanzare = creeaza_vanzare(id, titlu, gen, pret, reducere)
    if pret < 0:
        raise ValueError("Pretul nu poate fi numar negativ!")
    if get_reducere(vanzare) != "none" and get_reducere(vanzare) != "silver" and get_reducere(vanzare) != "gold":
        raise ValueError("Nu exista acest tip de reducere!")
    return lista + [vanzare]


def get_by_id(id, lista):
    """
    Da cartea/vanzarea cu id ul dat dintr o lista
    :param id: string
    :param lista: lista de vanzari/carti
    :return: cartea/vanzarea cu id ul dat dintr o lista sau None daca nu exista
    """
    for vanzare in lista:
        if get_id(vanzare) == id:
            return vanzare
    return None


def get_by_titlu(titlu, lista):
    """

    :param titlu:
    :param lista:
    :return:
    """
    for vanzare in lista:
        if get_titlu(vanzare) == titlu:
            return vanzare
    return None


def sterge_vanzare(id, lista):
    """
    :param id:
    :param lista:
    :return: o lista de vanzari
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista vreo vanzare cu id-ul dat!")
    return [vanzare for vanzare in lista if get_id(vanzare) != id]


def modifica_vanzare(id, titlu, gen, pret, reducere, lista):
    """
    modifica o vanzare dupa id
    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param reducere:
    :param lista:
    :return:
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista vreo vanzare cu id-ul dat!")
    lista_noua = []
    for vanzare in lista:
        if get_id(vanzare) == id:
            vanzare_noua = creeaza_vanzare(id, titlu, gen, pret, reducere)
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)
    return lista_noua
