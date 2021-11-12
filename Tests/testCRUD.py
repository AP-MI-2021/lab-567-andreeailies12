from Domain.vanzari import get_id, get_titlu, get_gen, get_pret, get_reducere
from Logic.CRUD import adauga_vanzare, get_by_id, sterge_vanzare, modifica_vanzare


def test_adauga_vanzare():
    lista = []
    lista = adauga_vanzare("1", "Singur pe lume", "fictiune", 20, "none", lista)

    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
    assert get_titlu(lista[0]) == "Singur pe lume"
    assert get_gen(lista[0]) == "fictiune"
    assert get_pret(lista[0]) == 20
    assert get_reducere(get_by_id("1", lista)) == "none"


def test_sterge_vanzare():
    lista = []
    lista = adauga_vanzare("1", "Singur pe lume", "fictiune", 20, "none", lista)
    lista = adauga_vanzare("2", "Inainte sa te cunosc", "fictiune", 20, "none", lista)

    lista = sterge_vanzare("1", lista)
    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None

    try:
        lista = sterge_vanzare("3", lista)
        assert False
    except ValueError:
        assert len(lista) == 1  # am sters 1, ne a rams lista a doua.
        assert get_by_id("2", lista) is not None
    except Exception:
        assert False


def test_modifica_vanzare():
    lista = []
    lista = adauga_vanzare("1", "Singur pe lume", "fictiune", 20, "none", lista)
    lista = adauga_vanzare("2", "Inainte sa te cunosc", "fictiune", 20, "none", lista)
    lista = modifica_vanzare("1", "Sub aceeasi stea", "dragoste", 25, "silver", lista)

    vanzare_updatata = get_by_id("1", lista)
    assert get_id(vanzare_updatata) == "1"
    assert get_titlu(vanzare_updatata) == "Sub aceeasi stea"
    assert get_gen(vanzare_updatata) == "dragoste"
    assert get_pret(vanzare_updatata) == 25
    assert get_reducere(vanzare_updatata) == "silver"

    vanzare_neupdatata = get_by_id("2", lista)
    assert get_id(vanzare_neupdatata) == "2"
    assert get_titlu(vanzare_neupdatata) == "Inainte sa te cunosc"
    assert get_gen(vanzare_neupdatata) == "fictiune"
    assert get_pret(vanzare_neupdatata) == 20
    assert get_reducere(vanzare_neupdatata) == "none"

    lista = []
    lista = adauga_vanzare("1", "Singur pe lume", "fictiune", 20, "none", lista)
    lista = modifica_vanzare("1", "Sub aceeasi stea", "dragoste", 25, "silver", lista)

    vanzare_neupdatata = get_by_id("1", lista)
    assert get_id(vanzare_neupdatata) == "1"
    assert get_titlu(vanzare_neupdatata) == "Singur pe lume"
    assert get_gen(vanzare_neupdatata) == "fictiune"
    assert get_pret(vanzare_neupdatata) == 20
    assert get_reducere(vanzare_neupdatata) == "none"
