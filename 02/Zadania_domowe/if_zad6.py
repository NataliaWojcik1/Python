# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą
# przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.


number = int(input('Podaj liczbę od 1 do 100: '))

hide_number = 8

if number == hide_number:
    print('Gratulacje!')

else:
    print('pudło!')
