def creeaza_vanzare(id, titlu, gen, pret, reducere):
    """
    Creeaza un dictionar ce reprezinta o vanzare.
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param reducere: string
    :return: un dictionar ce contine o vanzare.
    """
    return {  # la liste folosim [], la dictionar folosim {}
        "id": id,  # cheie: valoare
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "reducere": reducere

    }


def get_id(vanzare): # ne ajuta ca atunci cand gresim sa ne apara exact gresela, functia.
    """
    Getter pentru id ul  cartii
    :param vanzare: dictionar ce contine o vanzare
    :return: id ul vanzarii
    """
    return vanzare["id"] #--> id. imi returneaza valoarea


def get_titlu(vanzare):
    """
    Getter pentru titlul cartii
    :param vanzare: dictionar ce contine o vanzare
    :return: titlul cartii de vanzare
    """
    return vanzare["titlu"]


def get_gen(vanzare):
    """
    Getter pentru genul cartii
    :param vanzare: dictionar ce contine o vanzare
    :return: genul cartii de vanzare
    """
    return vanzare["gen"]


def get_pret(vanzare):
    """
    Getter pentru pretul cartii
    :param vanzare: dictionar ce contine o vanzare
    :return: pretul cartii de vanzare
    """
    return vanzare["pret"]


def get_reducere(vanzare):
    """
    Getter pentru reducerea cartii
    :param vanzare: dictionar ce contine o vanzare
    :return: tipul de reducere a cartii de vanzare
    """
    return vanzare["reducere"]

def schimbare_pret(vanzare, pret_nou):
    """
    Modifica pretul unei vanzari
    :param vanzare: pret initial
    :param pret_nou: noul pret
    """
    vanzare["pret"] = pret_nou


def to_string(vanzare):
    return "id: {}, titlu: {}, gen: {}, pret: {}, reducere: {}".format(
        get_id(vanzare),
        get_titlu(vanzare),
        get_gen(vanzare),
        get_pret(vanzare),
        get_reducere(vanzare)
    )
