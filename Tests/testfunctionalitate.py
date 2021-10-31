from Domain.vanzari import get_pret, get_gen
from Logic.CRUD import adauga_vanzare, get_by_id
from Logic.functionalitate import vanzare_discount, modificare_gen


def test_vanzare_discount():
    lista = []
    lista = adauga_vanzare("1", "Sange de zapada", "politist", 35, "gold", lista)
    lista = adauga_vanzare("2", "Enigma Otiliei", "bildugsroman", 30, "none", lista)
    lista = adauga_vanzare("3", "Micul print", "fantastic", 20, "silver", lista)

    vanzare_discount(lista)
    assert get_pret(get_by_id("1", lista)) == 31.5
    assert get_pret(get_by_id("2", lista)) == 30.0
    assert get_pret(get_by_id("3", lista)) == 19.0

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