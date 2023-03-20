# Zadanie 3
import random
import getpass

opcje = ["p", "k", "n"]

print("Dostępne tryby:\n1. gra z komputerem\n2. dwóch graczy")
tryb = input("Wybierz tryb: ")
ilosc_rund = input("Podaj ilość rund: ")
wyniki = list(range(0, int(ilosc_rund)))

while tryb not in {"1", "2"}:
    print("Podaj poprawny numer!")
    tryb = input("Wybierz tryb: ")

if tryb == "1":
    gracz = input("Nazwa gracza: ")
    suma_gracz = 0
    suma_komputer = 0

    for i in range(int(ilosc_rund)):
        wybor = input("Podaj swój wybór (p - papier, k - kamień, n - nożyce): ")
        while wybor not in opcje:
            print("Spróbuj ponownie")
            wybor = input("Podaj swój wybór (p - papier, k - kamień, n - nożyce): ")

        komputer = opcje[random.randint(0, 2)]

        print(gracz, ":", wybor)
        print("Komputer: ", komputer)

        if wybor == komputer:
            wyniki[i] = "remis"
            print("Remis")
        else:
            if opcje.index(wybor) - opcje.index(komputer) in {-1, 2}:
                wyniki[i] = gracz
                suma_gracz += 1
                print("Runde wygrywa ", gracz)
            else:
                wyniki[i] = "komputer"
                suma_komputer += 1
                print("Runde wygrywa komputer")

    print("**********WYNIKI**********")
    for i in range(len(wyniki)):
        print("Runda", i+1, ":", wyniki[i])

    if suma_gracz == suma_komputer:
        print("Remis")
    else:
        print("Wygrywa ", end="")
        if suma_gracz > suma_komputer:
            print(gracz)
        else:
            print("komputer")


elif tryb == "2":
    gracz1 = input("Nazwa gracza 1: ")
    gracz2 = input("Nazwa gracza 2: ")
    suma_g1 = 0
    suma_g2 = 0

    for i in range(int(ilosc_rund)):
        g1 = getpass.getpass(gracz1 + ", podaj swój wybór (p - papier, k - kamień, n - nożyce): ")
        while g1 not in opcje:
            print("Spróbuj ponownie")
            g1 = getpass.getpass(gracz1 + ", podaj swój wybór (p - papier, k - kamień, n - nożyce): ")

        g2 = getpass.getpass(gracz2 + ", podaj swój wybór (p - papier, k - kamień, n - nożyce): ")
        while g2 not in opcje:
            print("Spróbuj ponownie")
            g2 = getpass.getpass(gracz2 + ", podaj swój wybór (p - papier, k - kamień, n - nożyce): ")

        print(gracz1, ":", g1)
        print(gracz2, ":", g2)

        if g1 == g2:
            wyniki[i] = "remis"
            print("Remis")
        else:
            if opcje.index(g1) - opcje.index(g2) in {-1, 2}:
                wyniki[i] = gracz1
                suma_g1 += 1
                print("Runde wygrywa ", gracz1)
            else:
                wyniki[i] = gracz2
                suma_g2 += 1
                print("Runde wygrywa ", gracz2)

    print("**********WYNIKI**********")
    for i in range(len(wyniki)):
        print("Runda", i + 1, ":", wyniki[i])

    if suma_g1 == suma_g2:
        print("Remis")
    else:
        print("Wygrywa ", end="")
        if suma_g1 > suma_g2:
            print(gracz1)
        else:
            print(gracz2)
