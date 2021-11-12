from Logic.CRUD import adauga_vanzare
from Tests.testall import run_all_test
from UI.command_line_console import meniu
from UI.console import run_menu


def meniuu():
    print("1. Prima metoda de rezolvare al UI")
    print("2. A doua metoda de UI")
    print("3. Iesire")


def main():
    run_all_test()
    #run_m1enu([])

    while True:
        meniuu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = []
            lista = adauga_vanzare("1", "Sange de zapada", "politist", 35, "gold", lista)
            lista = adauga_vanzare("2", "Enigma Otiliei", "bildugsroman", 30, "none", lista)
            print(run_menu(lista))
        elif optiune == "2":
            lista = []
            lista = adauga_vanzare("1", "Sange de zapada", "politist", 35, "gold", lista)
            lista = adauga_vanzare("2", "Enigma Otiliei", "bildugsroman", 30, "none", lista)
            print(meniu(lista))
        elif optiune == "3":
            break
        else:
            print("Optiune gresita! Reincercati: ")



main()
