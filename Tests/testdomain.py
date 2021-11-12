from Domain.vanzari import get_id, get_titlu, get_gen, get_pret, get_reducere, creeaza_vanzare


def test_vanzare():
    vanzare = creeaza_vanzare("1", "Singur pe lume", "fictiune", 20, "none")

    assert get_id(vanzare) == "1"
    assert get_titlu(vanzare) == "Singur pe lume"
    assert get_gen(vanzare) == "fictiune"
    assert get_pret(vanzare) == 20
    assert get_reducere(vanzare) == "none"
