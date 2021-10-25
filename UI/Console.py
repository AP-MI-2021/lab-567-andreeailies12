from Domain.vanzari import to_string
from Logic.CRUD import adauga_vanzare, sterge_vanzare, modifica_vanzare
from Logic.functionalitate import vanzare_discount


def print_menu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicare discount tuturor vanzarilor. (5% pentru silver, 10% pentru gold)")
    print("a. Afisare vanzare")
    print("x. Iesire")


def ui_adauga_vanzare(lista):
    id = input("Dati id ul: ")
    titlu = input("Dati titlul cartii: ")
    gen = input("Dati genul cartii: ")
    pret = float(input('Dati pretul cartii: '))
    reducere = input ("Dati tipul de reducere(none, silver, gold): ")
    return adauga_vanzare(id, titlu, gen, pret, reducere, lista)


def ui_sterge_vanzare(lista):
    id = input("Dati id ul vanzarii/cartii de sters: ")
    return sterge_vanzare(id, lista)


def ui_modifica_vanzare(lista):
    id = input("Dati id ul vanzarii de carte de modificat: ")
    titlu = input("Dati  noul titlu al cartii: ")
    gen = input("Dati noul gen al cartii: ")
    pret = float(input('Dati noul pret al cartii: '))
    reducere = input("Dati noul tip de reducere(none,silver, gold: ")
    return modifica_vanzare(id, titlu, gen, pret, reducere, lista)


def show_all(lista):
    for vanzare in lista:
        print(to_string(vanzare))



def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = ui_adauga_vanzare(lista)
        elif optiune == "2":
            lista = ui_sterge_vanzare(lista)
        elif optiune == "3":
            lista = ui_modifica_vanzare(lista)
        elif optiune == "4":
            vanzare_discount(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")