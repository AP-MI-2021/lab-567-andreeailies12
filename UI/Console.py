from Domain.vanzari import to_string
from Logic.CRUD import adauga_vanzare, sterge_vanzare, modifica_vanzare
from Logic.functionalitate import vanzare_discount, modificare_gen, min_pret, ord_pret, nr_titluri


def print_menu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicare discount tuturor vanzarilor. (5% pentru silver, 10% pentru gold)")
    print("5. Modificare gen in functie de titlul dat")
    print("6. Determinarea prețului minim pentru fiecare gen")
    print("7. Ordonarea vânzărilor crescător după preț")
    print("8. Afișarea numărului de titluri distincte pentru fiecare gen")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare vanzare")
    print("x. Iesire")


def ui_adauga_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Dati id ul: ")
        titlu = input("Dati titlul cartii: ")
        gen = input("Dati genul cartii: ")
        pret = float(input("Dati pretul cartii: "))
        reducere = input("Dati tipul de reducere(none, silver, gold): ")

        rezultat = adauga_vanzare(id, titlu, gen, pret, reducere, lista)

        undo_list.append(lista)  #doar dupa ce vedem ca nu exista vreo exceptie/ ca nu are ce sa crape, vom adauga la undo_list lista
        redo_list.clear()  #golesc lista cu clear
        return rezultat
    except ValueError as ve:
        print('Eroare! Detalii:', ve)
        return lista


def ui_sterge_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Dati id ul vanzarii/cartii de sters: ")
        rezultat = sterge_vanzare(id, lista)

        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modifica_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Dati id ul vanzarii de carte de modificat: ")
        titlu = input("Dati  noul titlu al cartii: ")
        gen = input("Dati noul gen al cartii: ")
        pret = float(input('Dati noul pret al cartii: '))
        reducere = input("Dati noul tip de reducere(none,silver, gold): ")
        rezultat = modifica_vanzare(id, titlu, gen, pret, reducere, lista)

        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def show_all(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def console_modificare_gen(lista):
    try:
        titlu = input("Titlu cartii careia doriti sa ii modificati genul: ")
        gen_nou = input("Noul gen:")
        modificare_gen(titlu, gen_nou, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def console_min_pret(lista):
    rezultat = min_pret(lista)
    for gen in rezultat:
        print("Genul {} are minimul de pret {}".format(gen, rezultat[gen]))


def console_ord_pret(lista):
    show_all(ord_pret(lista))


def console_nr_titluri(lista):
    rezultat = nr_titluri(lista)
    for gen in rezultat:
        print("Genul {} are numarul de titluri diferite egal cu {}".format(gen, rezultat[gen]))


def ui_vanzare_discount(lista, undo_list, redo_list):
    undo_list.append(lista)
    redo_list.clear()
    return vanzare_discount(lista)


def run_menu(lista):
    undo_list = [] # retinem lista de istoricuri ,lista de liste
    redo_list = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = ui_adauga_vanzare(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_sterge_vanzare(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modifica_vanzare(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = ui_vanzare_discount(lista, undo_list, redo_list)
        elif optiune == "5":
            console_modificare_gen(lista)
        elif optiune == "6":
            console_min_pret(lista)
        elif optiune == "7":
            console_ord_pret(lista)
        elif optiune == "8":
            console_nr_titluri(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)  # redo se face la undo
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo.")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo.")

        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
