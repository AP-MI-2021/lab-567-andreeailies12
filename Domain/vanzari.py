def creeaza_vanzare(id, titlu, gen, pret, reducere):
    """
    Creeaza o lista ce reprezinta o vanzare.
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param reducere: string
    :return: un lista ce contine o vanzare.
    """
    return [id, titlu, gen, pret, reducere]


def get_id(vanzare): # ne ajuta ca atunci cand gresim sa ne apara exact gresela, functia.
    """
    Getter pentru id ul  cartii
    :param vanzare: lista ce contine o vanzare
    :return: id ul vanzarii
    """
    return vanzare[0] #--> id. imi returneaza valoarea


def get_titlu(vanzare):
    """
    Getter pentru titlul cartii
    :param vanzare: lista ce contine o vanzare
    :return: titlul cartii de vanzare
    """
    return vanzare[1]


def get_gen(vanzare):
    """
    Getter pentru genul cartii
    :param vanzare: lista ce contine o vanzare
    :return: genul cartii de vanzare
    """
    return vanzare[2]


def get_pret(vanzare):
    """
    Getter pentru pretul cartii
    :param vanzare: lista ce contine o vanzare
    :return: pretul cartii de vanzare
    """
    return vanzare[3]


def get_reducere(vanzare):
    """
    Getter pentru reducerea cartii
    :param vanzare: lista ce contine o vanzare
    :return: tipul de reducere a cartii de vanzare
    """
    return vanzare[4]

def schimbare_pret(vanzare, pret_nou):
    """
    Modifica pretul unei vanzari
    :param vanzare: pret initial
    :param pret_nou: noul pret
    """
    vanzare[3] = pret_nou


def to_string(vanzare):
    return "id: {}, titlu: {}, gen: {}, pret: {}, reducere: {}".format(
        get_id(vanzare),
        get_titlu(vanzare),
        get_gen(vanzare),
        get_pret(vanzare),
        get_reducere(vanzare)
    )