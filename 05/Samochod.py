git add# Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
#
# Program zacznie ze stworzonym słownikiem o trzech kluczach:
# marka (str)
#
# model (str)
#
# rocznik (int)
#
# Wypisze ten słownik na ekran (bez żadnego formatowania)
#
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
# “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
#
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:
# “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
#
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.


def show_vintage(age):
    if age > 25:
        print(f'Gratuluje, Twój samochód {car["brand"]} moze byc zarejstrowany)
    else:
        print('Niestety nie')

car = {'marka' : 'Wolswagen' , 'model' : 'Polo', 'rocznik' : 2009}


print(dict)

if 2021 - car['year'] > 25:
    print(f'Gratuluje, Twój samochód {car["brand"]} moze byc zarejstrowany)
else:
    print('Niestety nie')
