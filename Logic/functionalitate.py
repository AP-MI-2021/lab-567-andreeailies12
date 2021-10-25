from Domain.vanzari import get_reducere, get_pret, schimbare_pret


def vanzare_discount(lista):

    for vanzare in lista:
        if get_reducere(vanzare) == "silver":
            pret_nou = get_pret(vanzare) - 0.05 * get_pret(vanzare)
        elif get_reducere(vanzare) == "gold":
            pret_nou = get_pret(vanzare) - 0.1 * get_pret(vanzare)
        else:
            pret_nou = get_pret(vanzare)
        schimbare_pret(vanzare, pret_nou)

