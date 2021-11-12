from Logic.CRUD import modifica_vanzare, adauga_vanzare, sterge_vanzare
from UI.console import show_all

def adaugare(id, titlu, gen, pret, reducere, lista):
    try:
        return adauga_vanzare(id, titlu, gen, pret, reducere, lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def modificare(id, titlu, gen, pret, reducere, lista):
    try:
        return modifica_vanzare(id, titlu, gen, pret, reducere, lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def stergere(id, lista):
    try:
        return sterge_vanzare(id, lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista

def ajutor():
    print("Meniul comenzilor:")
    print("add - id, titlu, gen, pret, reducere(none, silver, gold) - adauga vanzare")
    print("update - id, titlu, gen, pret, reducere(none, silver, gold) - modifica vanzare")
    print("showAll - afisarea tuturor vanzarilor")
    print("delete - id - sterge vanzarea")
    print("stop - oprirea programului")


def meniu(lista):
    ajutor()
    while True:
        print("help - arata meniul")
        comanda = input("Dati comanda: ")
        if comanda == "help":
            print("Meniul comenzilor:")
            print("add - id, titlu, gen, pret, reducere(none, silver, gold) - adauga vanzare")
            print("update - id, titlu, gen, pret, reducere(none, silver, gold) - modifica vanzare")
            print("showAll - afisarea tuturor vanzarilor")
            print("delete - id - sterge vanzarea")
            print("stop - oprirea programului")
        elif comanda == "stop":
            break
        else:
            toate_opt = comanda.split(";")
            for i in range(len(toate_opt)):
                opt = toate_opt[i].split(",")
                if opt[0] == "add":
                    id = opt[1]
                    titlu = opt[2]
                    gen = opt[3]
                    pret = float(opt[4])
                    reducere = opt[5]
                    lista = adaugare(id, titlu, gen, pret, reducere, lista)
                elif opt[0] == "delete":
                    id = opt[1]
                    lista = stergere(id, lista)
                elif opt[0] == "update":
                    id = opt[1]
                    titlu = opt[2]
                    gen = opt[3]
                    pret = float(opt[4])
                    reducere = opt[5]
                    lista = modificare(id, titlu, gen, pret, reducere, lista)
                elif opt[0] == "showAll":
                    show_all(lista)
                else:
                    print("nu exista comanda")

