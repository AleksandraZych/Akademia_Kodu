"""Zadanie
Stwórz skrypt, który ob służy błędnie podaną liczbę typu float Liczba może zostać podana przez metodę input()
lub jako zmienna."""

def zadanie1(round):
    #napis_wczytany = "2.,5" #2.5
    print(f"\n Runda {round} \nPodaj liczbę:")
    napis_wczytany = input()
    try:
        liczba = float(napis_wczytany)
        print(f"Liczbą jest {liczba}")
    except ValueError as e:
        print("Och nie, nie udało się sparsować liczby! Szczegóły poniżej:\n" + str(e))
    except Exception as e:
        print("Och nie, nie udało się sparsować liczby i nie wiemy dlaczego! Szczegóły poniżej:\n" + str(e))
    else:
        print("Udało się skonwertować twoją liczbę na float")
    finally:
        print("Dzięki za zabawę!")

for round in range(1,4):
    zadanie1(round)