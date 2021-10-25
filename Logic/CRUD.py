from Domain.vanzari import creeaza_vanzare, get_id


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
    vanzare = creeaza_vanzare(id, titlu, gen, pret, reducere)
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

def sterge_vanzare(id, lista):
    """
    :param id:
    :param lista:
    :return: o lista de vanzari
    """
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
    lista_noua = []
    for vanzare in lista:
        if get_id(vanzare) == id:
            vanzare_noua =creeaza_vanzare(id, titlu, gen, pret, reducere)
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)
    return lista_noua