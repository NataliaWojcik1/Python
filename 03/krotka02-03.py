# 2▹ Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.
# 3▹ Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby. Jeśli liczba znajduje się na krotce wyswietl jej indeks.

numbers = (3, 5, 6, 2, 10)

guess = input('Podaj jakas liczbe calkowita: ')

if guess is numbers:
    index = numbers.index(guess)
    print('Liczba znajduje sie na indeksie: ', index)
else:
    print('Nie ma liczby w zbiorze')