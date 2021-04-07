# 1. Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
# i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

# txt = 'abrakadabra'
#
# middle = len(txt)//2
# element = txt[middle]
# prev = txt[middle-1]
# next = txt[middle+1]
#
# print(prev+element+ next)

# 2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy,
# utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = 'chmura'
s2 = 'slonce'

middle = len(s1)//2
prev = s1[:middle]
next = s1[middle:]
s3 = prev+s2+next

print(s3)