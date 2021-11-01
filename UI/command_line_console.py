from Domain.vanzari import to_string
from Logic.CRUD import adauga_vanzare, modifica_vanzare, sterge_vanzare


def show_all(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def meniu_help():
    print("Add, id, titlu, gen, pret, reducere -> Adauga vanzarea")
    print("Update, id, titlu, gen, pret, reducere -> Modifica vanzarea")
    print("Delete, id -> Sterge vanzarea")
    print("ShowAll -> Afiseaza vanzarea din lista")
    print("Stop -> Se opreste programul")


def menu(lista):
    while True:
        optiune = input()
        if optiune == 'Help':
            meniu_help()
        else:
            optiuni = optiune.split(';')
            if optiuni[0] == 'Stop':
                break
            else:
                for optiune in optiuni:
                    comenzi = optiune.split(',')
                    if comenzi[0] == 'Add':
                        try:
                            lista = adauga_vanzare(comenzi[1], comenzi[2], comenzi[3], float(comenzi[4]), comenzi[5], lista)
                        except ValueError as ve:
                            print('Eroare: ', ve)
                    elif comenzi[0] == 'ShowAll':
                        show_all(lista)
                    elif comenzi[0] == 'Update':
                        lista = modifica_vanzare(comenzi[1], comenzi[2], comenzi[3], float(comenzi[4]), comenzi[5], lista)
                    elif comenzi[0] == 'Delete':
                        lista = sterge_vanzare(comenzi[1], lista)
                    else:
                        print("Optiunea este gresita!")

