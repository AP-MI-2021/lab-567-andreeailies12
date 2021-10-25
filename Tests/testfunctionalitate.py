from Domain.vanzari import get_pret
from Logic.CRUD import adauga_vanzare, get_by_id
from Logic.functionalitate import vanzare_discount


def test_vanzare_discount():
    lista = []
    lista = adauga_vanzare("1", "Sange de zapada", "politist", 35, "gold", lista)
    lista = adauga_vanzare("2", "Enigma Otliliei", "bildugsroman", 30, "none", lista)
    lista = adauga_vanzare("3", "Micul print", "fantastic", 20, "silver", lista)

    vanzare_discount(lista)
    assert get_pret(get_by_id("1", lista)) == 31.5
    assert get_pret(get_by_id("2", lista)) == 30.0
    assert get_pret(get_by_id("3", lista)) == 19.0