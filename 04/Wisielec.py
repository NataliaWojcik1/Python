# 10▹ Stwórz grę wisielec “bez wisielca”.
# Komputer losuje wyraz z dostępnej w programie listy wyrazów.
# Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
# Użykownik podaje literę.
# Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
# “Trafione!” oraz napis ze znanymi literami.
# W przeciwnym wpadku pokaż komunikat:
# “Nie trafione, spróbuj jeszcze raz!”.
# Możesz ograniczyć liczbę prób do np. 10.

def check_letter(user_letter, computer_choice,word):
    if user_letter in computer_choice:
        print('Trafione!')
        for index in range(len(word)):
            if user_letter == computer_choice[index]:
                word[index] = user_letter
        return (' '.join(word))
    elif user_letter not in computer_choice:
        print('Nie trafione, spróbuj jeszcze raz!')
        return (' '.join(word))


words = ['pomidor', 'marchewka', 'pietruszka', 'burak', 'ziemniak']
import random

computer_word = random.choice(words)
print('Haslo posiada:', len(computer_word), 'liter')

guess_word = '-' * len(computer_word)
print(guess_word.replace('', ' '))

guess_word = list(guess_word)

for chance in range (0, 11):
    user_guess = input('Podaj litere: ')
    print(check_letter(user_guess, computer_word, guess_word))

print('Koniec gry!')



