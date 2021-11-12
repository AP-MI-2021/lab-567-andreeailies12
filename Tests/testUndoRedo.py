from Logic.CRUD import adauga_vanzare

def adaugare(id, titlu, gen, pret, reducere, lista):
    try:
        return adauga_vanzare(id, titlu, gen, pret, reducere, lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def test_undo_redo():
    lista =[] # 1. start program/ lista initiala goala
    undo_list = []
    redo_list = []

    rezultat = adaugare("1", "Singur pe lume", "fictiune", 20, "none", lista)
    undo_list.append(lista)
    lista = rezultat #2. add prima vanzare
#avem o vanzare in lista

    rezultat = adaugare("2", "Inainte sa te cunosc", "fictiune", 20, "none", lista)
    undo_list.append(lista)
    lista = rezultat #3. add a doua vanzare
#acum avem doua vanzari in lista

    rezultat = adaugare("3", "Micul print", "fictiune", 20, "silver", lista)
    undo_list.append(lista)
    lista = rezultat #4. add a treia vanzare

    assert len(lista) == 3
    assert lista == [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'},
                     {'id': '2', 'titlu': 'Inainte sa te cunosc', 'gen': 'fictiune','pret': 20, 'reducere': 'none'}
    , {'id': '3', 'titlu': 'Micul print', 'gen': 'fictiune', 'pret': 20, 'reducere': 'silver'}]
#avem 3 vanzari in lista

    redo_list.append(lista)  # redo se face la undo
    lista = undo_list.pop()
    assert len(lista) == 2
    assert undo_list == [[], [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'}]]
    assert lista == [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'},
                     {'id': '2', 'titlu': 'Inainte sa te cunosc', 'gen': 'fictiune','pret': 20, 'reducere': 'none'}]
#5. undo - scoate ultima vanzare

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert undo_list == [[]]
    assert lista == [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'}]
#6. undo - inca un undo scoate penultima vanzare adaugata

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert undo_list == []
    assert lista == []
#7. undo - inca un undo scoate si prima vanzare adaugata

    if len(undo_list) > 0:
        redo_list.append(lista)  # redo se face la undo
        lista = undo_list.pop()
    #else:
        #print("Nu se poate face undo.") - din UI. vedem ca lista nu mai are veun element, nu se poate face undo,ramane ca la 7
    assert len(lista) == 0
    assert undo_list == []
    assert lista == []
#8. undo - inca un undo nu face nimic

    rezultat = adaugare("1", "Singur pe lume", "fictiune", 20, "none", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()

    rezultat = adaugare("2", "Inainte sa te cunosc", "fictiune", 20, "none", lista)
    undo_list.append(lista)
    lista = rezultat

    rezultat = adaugare("3", "Micul print", "fictiune", 20, "silver", lista)
    undo_list.append(lista)
    lista = rezultat


    assert len(lista) == 3
    assert lista == [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'},
                     {'id': '2', 'titlu': 'Inainte sa te cunosc', 'gen': 'fictiune','pret': 20, 'reducere': 'none'}
    , {'id': '3', 'titlu': 'Micul print', 'gen': 'fictiune', 'pret': 20, 'reducere': 'silver'}]
#9. am adaugat cele 3 vanzari

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert len(lista) == 3
    assert len(redo_list) == 0 # nu am facut vreun undo ca sa pot face redo
#10. redo -redo nu face nimic

    redo_list.append(lista)
    lista = undo_list.pop()

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert lista == [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'}]
    assert undo_list == [[]]
#11. undo,undo - doua undo-uri scot ultimele 2 vanzari

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 2
    assert redo_list == [[{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'},
                     {'id': '2', 'titlu': 'Inainte sa te cunosc', 'gen': 'fictiune','pret': 20, 'reducere': 'none'}
    , {'id': '3', 'titlu': 'Micul print', 'gen': 'fictiune', 'pret': 20, 'reducere': 'silver'}]]
    assert undo_list == [[], [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'}]]
#12. redo - redo anuleaza ultimul undo, daca ultima operatie e undo

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 3
    assert redo_list == []
    assert undo_list == [[], [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'}],
                         [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'},
                          {'id': '2', 'titlu': 'Inainte sa te cunosc', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'}]]
#13.redo anuleaza si primul undo

    redo_list.append(lista)
    lista = undo_list.pop()

    redo_list.append(lista)
    lista = undo_list.pop()

    assert len(lista) == 1
    assert lista == [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'}]
    assert undo_list == [[]]
#14. undo, undo - doua undo-uri scot ultimele 2 vanzari

    rezultat = adaugare("4", "Tu", "dragoste", 30, "silver", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()
#15. add a patra vanzare

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert len(lista) == 2
    assert lista == [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'},
     {'id': '4', 'titlu': 'Tu', 'gen': 'dragoste', 'pret': 30, 'reducere': 'silver'}]
    assert redo_list == []
    assert undo_list == [[], [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'}]]
#16.redo - redo nu face nimic, deoarece ultima operatie nu este un undo

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert undo_list == [[]]
    assert redo_list == [[{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'},
     {'id': '4', 'titlu': 'Tu', 'gen': 'dragoste', 'pret': 30, 'reducere': 'silver'}]]
#17. undo - undo anuleaza adaugarea lui o4

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert undo_list == []
    assert redo_list ==[[{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'},
     {'id': '4', 'titlu': 'Tu', 'gen': 'dragoste', 'pret': 30, 'reducere': 'silver'}],
    [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'}]]
#18. undo - undo anuleaza adaugarea lui o1 - practic se continua sirul de undo de la pct 14, imi vin sterse amandoua

    undo_list.append(lista)
    lista = redo_list.pop()

    undo_list.append(lista)
    lista = redo_list.pop()

    assert len(lista) == 2
    assert lista == [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'},
                     {'id': '4', 'titlu': 'Tu', 'gen': 'dragoste', 'pret': 30, 'reducere': 'silver'}]
    assert redo_list == []
# redo, redo - se anuleaza ultimele 2 undo-uri

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
    assert lista == [{'id': '1', 'titlu': 'Singur pe lume', 'gen': 'fictiune', 'pret': 20, 'reducere': 'none'},
                     {'id': '4', 'titlu': 'Tu', 'gen': 'dragoste', 'pret': 30, 'reducere': 'silver'}]
    assert redo_list == []
#20. redo - redo nu face nimic

