from Domain.vanzari import get_reducere, get_pret, get_titlu, schimbare_gen, get_gen, creeaza_vanzare, \
    get_id
from Logic.CRUD import get_by_titlu


def vanzare_discount(lista):
    """
    Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold.
    :param lista: lista
    :return: lista noua cu dicount urile aplicate
    """
    lista_noua = []
    for vanzare in lista:
        if get_reducere(vanzare) == "silver":
            noua_vanzare =creeaza_vanzare(get_id(vanzare),
        get_titlu(vanzare),
        get_gen(vanzare),
        get_pret(vanzare) - 0.05 * get_pret(vanzare),
        get_reducere(vanzare),
    )
            lista_noua.append(noua_vanzare)

        elif get_reducere(vanzare) == "gold":
            noua_vanzare = creeaza_vanzare(get_id(vanzare),
        get_titlu(vanzare),
        get_gen(vanzare),
        get_pret(vanzare) - 0.1 * get_pret(vanzare),
        get_reducere(vanzare),
    )
            lista_noua.append(noua_vanzare)
        else:
            lista_noua.append(vanzare)
    return lista_noua


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
    Ordonarea vânzărilor crescător după preț
    :param lista:
    :return: vanzari ordonate dupa pret
    """
    return sorted(lista, key = get_pret)

def nr_titluri(lista): # algoritmul este asemantor cu cel de min_pret
    """
     Afișarea numărului de titluri distincte pentru fiecare gen
    :param lista:
    :return: numarul de titluri diferite pentru fiecare gen
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






