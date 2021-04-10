# 6▹ Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.

import random

options = ['kamien', 'papier', 'nozyce']


def gameplay(user, computer):
    if user == computer:
        return 'Remis!'
    elif user == 'papier' and computer == 'kamien':
        return 'Wygrałeś!'
    elif user == 'kamien' and computer == 'nozyce':
        return 'Wygrałeś!'
    elif user == 'nozyce' and computer == 'papier':
        return 'WYgrales'
    else:
        return 'Wygrał komputer'


while True:
    user_sign = input('Wybierz kamien, papier lub nozyce: ')
    computer_sign = random.choice(options)
    print(computer_sign)
    print(gameplay(user_sign, computer_sign))
    break
