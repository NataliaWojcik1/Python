# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

number_1 = int(input('Podaj pierwszą liczbę calkowta: '))
number_2 = int(input('Podaj druga liczbe calkowitą: '))

total = number_1 + number_2

if total > 100:
    print(total)
else:
    print('Koniec')
