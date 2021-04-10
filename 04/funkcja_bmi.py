# 1▹ Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą
# bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
# (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

def count_bmi(mass, height):
    bmi = mass / ((height) ** 2)
    bmi_round = round(bmi, 2)
    return bmi_round


def count_range(result):
    if result <= 18.49:
        return 'Niedowaga'
    elif 18.5 <= result <= 24.99:
        return 'Waga prawidlowa'
    elif 25 <= result <= 29.99:
        return 'Nadwaga'
    elif result >= 30:
        return 'Otylosc'
    else:
        return 'Podano nieprawidlowe wartosci'


masa = int(input("Podaj swoja mase w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))
bmi_exact = count_bmi(masa, wzrost)
bmi_range = count_range(bmi_exact)

print('Twoje BMI wynosi:', bmi_exact, 'i mieści sie w zakresie:', bmi_range)
