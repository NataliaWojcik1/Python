# Rozwiń kod funkcja_bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności
# od wyniku: niedowaga / waga normalna / nadwaga / otyłość.
masa = int(input("Podaj swoja mase w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))

bmi_1 = masa / ((wzrost)**2)
bmi = round(bmi_1, 2)

print('Twoje BMI wynosi:', bmi)
if bmi < 18.49:
    print('Niedowaga')
elif 18.50 < bmi < 24.99:
    print('Prawidłowa waga')
elif 25 < bmi < 29.99:
    print('Nadwaga')
elif bmi > 30:
    print('Otyłość!')



