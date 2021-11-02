from Domain.vanzari import to_string
from Logic.CRUD import modifica_vanzare, adauga_vanzare, sterge_vanzare


def adaugare(id, titlu, gen, pret, reducere, lista):
    try:
        return adauga_vanzare(id, titlu, gen, pret, reducere, lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista

def modificare(id, titlu, gen, pret, reducere, lista):
    try:
        return modifica_vanzare(id, titlu, gen, pret, reducere,lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista

def stergere(id, lista):
    try:
        return sterge_vanzare(id, lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def show_all(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def ajutor():
    print("Meniul comenzilor:")
    print("add, id, titlu, gen, pret, reducere(none, silver, gold) - adauga vanzare")
    print("update, id, titlu, gen, pret, reducere(none, silver, gold) - modifica vanzare")
    print("showAll - afisarea tuturor vanzarilor")
    print("delete, id - sterge vanzarea")
    print("stop - oprirea programului")
    print("Introduceti comanda: ")


def meniu():
    lista = []
    lista = adauga_vanzare("1", "Sange de zapada", "politist", 35, "gold", lista)
    lista = adauga_vanzare("2", "Enigma Otiliei", "bildugsroman", 30, "none", lista)
    functioneaza = True

    while functioneaza is True:
        ajutor()
        alegere = input()
        if alegere == "help":
            ajutor()
        else:
            comanda_lista = alegere.split(";")
            optiune = comanda_lista[0]
            for comanda in comanda_lista[1:]:
                opt = comanda.split(",")

            if optiune == "add":
                lista = adaugare(opt[0], opt[1], opt[2], float(opt[3]), opt[4], lista)
            elif optiune == "update":
                lista = modificare(opt[0], opt[1], opt[2], float(opt[3]), opt[4], lista)
            elif optiune == "delete":
                lista = stergere(opt[0], lista)
            elif optiune == "showAll":
                show_all(lista)
            elif optiune == "stop":
                functioneaza = False
            else:
                print("Comanda gresita! Incercati din nou!")

meniu()