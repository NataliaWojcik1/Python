# Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
# i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

txt = 'abrakadabra'

middle = len(txt)//2
element = txt[middle]
prev = txt[middle-1]
next = txt[middle+1]

print(prev+element+ next)