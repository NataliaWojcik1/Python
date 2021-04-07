# Napisz program, który wyświetli kolejne wyniki
# dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).

number = int(input('Podaj liczbę od 1 do 8: '))
score = 1
if number <= 8:
    for i in range(1, number+1):
        score = score * i
        if i == number:
            print(' Silnia z', number, 'rowna się', score)
else:
    print('Podana liczba jest za duza')
