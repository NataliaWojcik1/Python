# dish = 'gzik'
# if dish == 'pyzy':
#     reg = 'Wielko'
# print(reg)

# zad 1. Poproś użytkownika o podanie liczby.
# Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

number = int(input('Podaj liczbe calkowita: '))

if number % 3 == 0:
    print('Twoja liczba jest podzielna przez 3')
else:
    print('Nie jest podzielna')