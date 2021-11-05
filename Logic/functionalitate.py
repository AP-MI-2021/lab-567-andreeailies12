from Domain.vanzari import get_reducere, get_pret, schimbare_pret, get_titlu, schimbare_gen, get_gen
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


def min_pret(lista):
    """
    Detrmina minimul preturilor pentru fiecare gen
    :param lista: lista de vanzari
    :return: minimul de pret pentru fiecare gen
    """
    rezultat = {} # am creat un dictionar ; cheie:gen, valoare:pret
    for vanzare in lista:
        gen = get_gen(vanzare)
        pret = get_pret(vanzare)
        if gen in rezultat:
            if pret < rezultat[gen]: # if min< valoarea cheii gen --> atunci valoare cheii gen va lua valoarea min
                rezultat[gen] = pret
        else:
                rezultat[gen] = pret
    return rezultat

def ord_pret(lista):
    """

    :param lista:
    :return:
    """
    return sorted(lista, key = get_pret)

def nr_titluri(lista): # algoritmul este asemantor cu cel de min_pret
    """

    :param lista:
    :return:
    """
    numar = 1
    rezultat = {}#gen cheia,  nr titlu valoare
    for vanzare in lista:
        titlu = get_titlu(vanzare)
        gen = get_gen(vanzare)
        if gen in rezultat:
            if titlu != rezultat[gen]: # daca titlul nu se afla printre valorile existenta in dictionar
                numar = numar + 1 # se va adauga la numar / +1
                rezultat[gen] = numar
        else:
            rezultat[gen] = 1
    return rezultat






