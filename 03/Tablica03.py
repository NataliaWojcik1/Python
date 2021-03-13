# 3▹ Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

# numbers = [3,4,3,9,3]
#
# if numbers[0] == numbers[-1]:
#     print('Takie same')
# else:
#     print('Rozne')

# numbers = input('Podaj liczby po przecinku: ')
# numbers = numbers.split(',')
# print(numbers)
#
# print('Czy pierwsza i ostatnia liczba sa takie same: ' , numbers[0] == numbers[-1])


counter = int(input('Ile liczb chesz podać?'))

list_of_num = []

for i in range(counter):
    num = float(input("Podaj liczbe: "))
    list_of_num.append(num)

if list_of_num[0] == list_of_num[-1]:
    print('Pierwsza i ostatnia takasa sama')
else:
    print('Nie sa takie same')