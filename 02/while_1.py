# cookies = 5
# while cookies > 0:
#     print('Zjedz ciastko')
#     cookies = cookies - 1
#     print('Zostało jeszcze ', cookies)
#     print('---------------------------')
#
# print('\nNo nie, znowu trzeba kupić ciastka!')

# 1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.


temp_F = 0
while temp_F < 201:
    temp_C = 5/9 * (temp_F - 32)
    print('Temperatura w F = ', temp_F, 'na C to:', round(temp_C, 2))
    temp_F = temp_F + 20




