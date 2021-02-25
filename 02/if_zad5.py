# Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków. Poinformuj użytkownika,
# jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input('Wprowadz haslo: ')
# if len(password) < 8:
#     print('Haslo za krotkie')
#
# if password.islower():
#     print('Haslo musi zawierac jedna duza litere')
#
# if password.isalpha():
#     print('Haslo musi zawierac cyfry')
# elif password.isdigit():
#     print('Haslo musi zawierac litery')
# elif not password.isalnum():
#     print('Haslo nie moeze zawiera spacji ani znakow specjalnych')


lenght_correct = password >= 8
includes_letters_and_digits = not password.isdigit() and not password.isalpha() and password.isalnum()
at_list_one_capital_letter = not password.islower()

if not lenght_correct:
    print('Haslo za krotkie')

if not includes_letters_and_digits:
    print('Haslo musi zawierac cyfry i litery')

