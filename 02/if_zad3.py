# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

rate_1 = int(input('Podaj pierwsza opinie: '))
rate_2 = int(input('Podaj druga opinie: '))
rate_3 = int(input('Podaj trzecia opinie: '))

ocena = (rate_1 + rate_2 + rate_3)/3

if ocena >= 7:
    print('Bardzo dobry')
elif 5 < ocena < 7:
    print('Przeciętna')
elif ocena < 4:
    print('Nie warta uwagi')