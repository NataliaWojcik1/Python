# 2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
# 3▹ Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.
list_of_num = []
odd = []
print('Musisz podać 10 liczb, zaczynaj!')
for i in range(10):
    number = int(input('Podaj liczbe: '))
    list_of_num.append(number)

for elem in list_of_num:
    if elem % 2 != 0:
        odd.append(elem)
print(odd)

if list_of_num[0] == list_of_num[-1]:
    print('Pierwsza i ostatnia liczba jest taka sama!')
else:
    print('Pierwsza i ostania liczby są różne')