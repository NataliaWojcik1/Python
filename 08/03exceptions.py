# 3▹ Stwórz listę 10 elementową (różne typy!).
# Pozwól użytkownikowi podać dowolny index. Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

items = [0, 'dog', 3.14, 10, True, [], {'key': 3}, (), 'mug', 8]

number = input("Podaj numer indeksu: ")
try:
    number = int(number)
    result = items[number] / 1
    print(result)
except (IndexError, TypeError, ZeroDivisionError) as e:
    print(e)
except ValueError as e:
    print('Incorrect index ->', e)