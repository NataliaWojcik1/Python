# 4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

num_list = []

for elem in range(4):
    num = input('Podaj elementy do listy: ')
    num_list.append(num)

if num_list[1] == num_list[2]:
    print('Dwa srodkowe elementy są takie same')
else:
    print('Dwa srodkowe elementy nie sa takie same')