from Domain.vanzari import get_pret, get_gen, get_id
from Logic.CRUD import adauga_vanzare, get_by_id
from Logic.functionalitate import vanzare_discount, modificare_gen, min_pret, ord_pret, nr_titluri


def test_vanzare_discount():
    lista = []
    lista = adauga_vanzare("1", "Sange de zapada", "politist", 35, "gold", lista)
    lista = adauga_vanzare("2", "Enigma Otiliei", "bildugsroman", 30, "none", lista)
    lista = adauga_vanzare("3", "Micul print", "fantastic", 20, "silver", lista)

    #vanzare_discount(lista)
    lista = vanzare_discount(lista)
    assert get_pret(lista[0]) == 31.5
    assert get_pret(lista[1]) == 30.0
    assert get_pret(lista[2]) == 19.0


def test_modificare_gen():
    lista = []
    lista = adauga_vanzare("1", "Sange de zapada", "politist", 35, "gold", lista)
    lista = adauga_vanzare("2", "Enigma Otiliei", "bildugsroman", 30, "none", lista)
    lista = adauga_vanzare("3", "Micul print", "fantastic", 20, "silver", lista)

    modificare_gen("Sange de zapada", "fictiune", lista)
    assert get_gen(get_by_id("1", lista)) == "fictiune"

    modificare_gen("Micul print", "drama", lista)
    assert get_gen(get_by_id("3", lista)) == "drama"

    modificare_gen("Enigma Otiliei", "dragoste", lista)
    assert get_gen(get_by_id("2", lista)) == "dragoste"


def test_min_pret():
    lista = []
    lista = adauga_vanzare("1", "Sange de zapada", "politist", 35, "gold", lista)
    lista = adauga_vanzare("2", "Enigma Otiliei", "bildugsroman", 30, "none", lista)
    lista = adauga_vanzare("3", "Micul print", "politist", 20, "silver", lista)

    rezultat = min_pret(lista)

    assert len(rezultat) == 2
    assert rezultat["politist"] == 20
    assert rezultat["bildugsroman"] == 30


def test_ord_cresc():
    lista = []
    lista = adauga_vanzare("1", "Sange de zapada", "politist", 35, "gold", lista)
    lista = adauga_vanzare("2", "Enigma Otiliei", "bildugsroman", 30, "none", lista)
    lista = adauga_vanzare("3", "Micul print", "fictiune", 20, "silver", lista)

    rezultat = ord_pret(lista)

    assert get_id(rezultat[0]) == "3"
    assert get_id(rezultat[1]) =="2"
    assert get_id(rezultat[3]) == "1"


def test_nr_titluri():
    lista = []
    lista = adauga_vanzare("1", "Sange de zapada", "politist", 35, "gold", lista)
    lista = adauga_vanzare("2", "Enigma Otiliei", "bildugsroman", 30, "none", lista)
    lista = adauga_vanzare("3", "Micul print", "politist", 20, "silver", lista)

    rezultat = nr_titluri(lista)

    assert rezultat["politist"] == 2
    assert rezultat["bildugsroman"] == 1








