def creeaza_vanzare(id, titlu, gen, pret, reducere):
    """
    Creeaza o dictionar ce reprezinta o vanzare.
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param reducere: string
    :return: un lista ce contine o vanzare.
    """
    return {  # la liste folosim [], la dictionar folosim {}
        "id": id,  # cheie: valoare
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "reducere": reducere

    }
    # return [ id,....]


def get_id(vanzare): # ne ajuta ca atunci cand gresim sa ne apara exact gresela, functia.
    """
    Getter pentru id ul  cartii
    :param vanzare: dictionar ce contine o vanzare
    :return: id ul vanzarii
    """
    #return vanzare[0] #--> id. imi returneaza valoarea
    return vanzare["id"]


def get_titlu(vanzare):
    """
    Getter pentru titlul cartii
    :param vanzare: dictionar ce contine o vanzare
    :return: titlul cartii de vanzare
    """
    #return vanzare[1]
    return vanzare["titlu"]


def get_gen(vanzare):
    """
    Getter pentru genul cartii
    :param vanzare: dictionar ce contine o vanzare
    :return: genul cartii de vanzare
    """
    #return vanzare[2]
    return vanzare["gen"]


def get_pret(vanzare):
    """
    Getter pentru pretul cartii
    :param vanzare: dictionar ce contine o vanzare
    :return: pretul cartii de vanzare
    """
    #return vanzare[3]
    return vanzare["pret"]


def get_reducere(vanzare):
    """
    Getter pentru reducerea cartii
    :param vanzare: dictionar ce contine o vanzare
    :return: tipul de reducere a cartii de vanzare
    """
    #return vanzare[4]
    return vanzare["reducere"]


def schimbare_gen(vanzare, gen_nou):
    """
    Modifica genul unei carti
    :param vanzare: vanzarea careia o sa i se modifice genul
    :param gen_nou: noul gen
    """
    vanzare["gen"] = gen_nou


def to_string(vanzare):
    return "id: {}, titlu: {}, gen: {}, pret: {}, reducere: {}".format(
        get_id(vanzare),
        get_titlu(vanzare),
        get_gen(vanzare),
        get_pret(vanzare),
        get_reducere(vanzare)
    )
