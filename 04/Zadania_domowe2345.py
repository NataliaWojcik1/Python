# 2▹ Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).


# def minium_of(a,b,c):
#     if a < b and a <c:
#         print('A jest najmniejsze')
#     elif b < a and b <c:
#         print('B jest najmniejsze')
#     elif c < a and c <b:
#         print('C jest najmniejsze')
#
#
# minium_of(0,0,1)

# 3▹ Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

# def max_of(a,b,c):
# #     if a > b and a > c:
# #         print('A jest najwieksze')
# #     elif b > a and b > c:
# #         print('B jest najwieksze')
# #     elif c > a and c > b:
# #         print('C jest najwieksze')
#
# max_of(2, 3, 5)


# 4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

# def check_list(number, begin, end):
#     if begin < number < end:
#         print('Podana liczba znajduje sie w zakresie!')
#     else:
#         print('Podana liczba nie znajduje sie w zakresie!')
#
#
# number = 40
# start = int(input('Podaj poczatek zakresu '))
# end = int(input('Podaj koniec zakresu '))
# check_list(number, start, end)

# 5. Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

# import random
#
# def check_number(number):
#     counter = 0
#     while counter < 6:
#         guess = int(input(" Podaj liczbe: "))
#         if number < guess:
#             counter +=1
#             print("Podana liczba jest za duża")
#             print(counter)
#         elif number > guess:
#             counter +=1
#             print("Podana liczba jest za mała")
#             print(counter)
#         else:
#             print("Zgadłeś!")
#             break
#     print("Wykorzystałes wszystkie próby!")
#
# # number = random.randint(1, 100)
#
#
# check_number(random.randint(1, 100))

# secret_number = 5
#
# previous_guess = -100
#
# while True:
#     user_number = int(input('Give me, give me: '))
#     if user_number == user_number:
#         break
#
#     if abs(secret_number - user_number) < abs(previous_guess):
#         print('warm')
#         previous_guess = user_number
#     else:
#         print('Cold')
