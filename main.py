from Tests.testall import run_all_test
from UI.command_line_console import meniu
from UI.console import run_menu

def meniuu():
    print("1. Prima metoda de rezolvare al UI")
    print("2. A doua metoda de UI")
    print("3. Iesire")
def main():
    run_all_test()
    #run_menu([])

    while True:
        meniuu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            print(run_menu([]))
        elif optiune == "2":
            print(meniu())
        elif optiune == "3":
            break
        else:
            print("Optiune gresita! Reincercati: ")


main()