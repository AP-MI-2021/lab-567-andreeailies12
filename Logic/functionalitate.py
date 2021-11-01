from Domain.vanzari import get_reducere, get_pret, schimbare_pret, get_titlu, schimbare_gen
from Logic.CRUD import get_by_titlu


def vanzare_discount(lista):
    for vanzare in lista:
        if get_reducere(vanzare) == "silver":
            pret_nou = get_pret(vanzare) - 0.05 * get_pret(vanzare)
        elif get_reducere(vanzare) == "gold":
            pret_nou = get_pret(vanzare) - 0.1 * get_pret(vanzare)
        else:
            pret_nou = get_pret(vanzare)
        schimbare_pret(vanzare, pret_nou)


def modificare_gen(titlu, gen_nou, lista):
    """
    Modifica genul cartii pentru un titlu dat
    :param titlu: titlul cartii al carui gen urmeaza sa fie modificat
    :param gen_nou: noul gen al acrtii
    :param lista: lista de vanzari
    :return:genul modificat in functie de titlul cartii
    """
    for vanzare in lista:
        if get_titlu(vanzare) == titlu:
            schimbare_gen(vanzare, gen_nou)
        if get_by_titlu(titlu, lista) is None:
            raise ValueError("Nu exista titlul dat!")


