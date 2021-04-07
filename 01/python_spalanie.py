# # Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny. Załóżmy, że spalanie na 100km wynosi 6,4 l,
# # trasa to 120km, litr benzyny kosztuje 5,04 zł.
#
# milage_per_100 = 6.4
# distnace = 120
# cost = 5.04
#
# total = distnace/100 * milage_per_100 * cost
#
# print('koszt wyprawy to: ',total)

# txt = '9865'
#-----------
# print(txt.isnumeric())

# txt = 'Blala'
# -------------
# print(txt.center(10,'+'))
# print(len(txt))
#---------
# txt ='Blalala****'
#
# print(txt.rstrip('*'))

#--------

# txt = 'BLaaaa'
#
# print(txt.isupper())

#---------

# txt = 'Banananana'
# print(txt.count('na'))

#Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.


# txt = 'abrakadabra'
#
# middle = len(txt)//2
# element = txt[middle]
# prev = txt[middle-1]
# next = txt[middle+1]
#
# print(prev+element+ next)

quote = 'Honesty is the first chapter in the book of wisdom.'
#
# print(len(quote))
# print(quote[-2:-7:2])
# print(quote[-1])
#print(quote[25:51:3])
# Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

txt = input('Podaj zdanie: ')

txt = txt.replace(" ", "")
txt = txt.lower()

txt_2 = txt[::-1]



print('Is palindrom: ',txt == txt_2)

