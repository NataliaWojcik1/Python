import exceptions05


def get_weight():
    while True:
        try:
            weight = int(input('Podaj wage w kg:'))
        except (ValueError, TypeError):
            print('To nie jest prawidłowa wartosc! Sprobuj jeszcze raz')
            continue

        if weight > 30:
            break
        else:
            print('Twoja masa jest za niska! Podaj prawdziwa wage!')
    return weight


def get_height():
    while True:
        try:
            height = float(input('Podaj wzrost w metrach:'))
        except (ValueError, TypeError):
            print('To nie jest prawidłowa wartosc! Sprobuj jeszcze raz')
            continue

        if height > 1.5 < 2.3:
            break
        else:
            print('Twoj wzrost jest za niski! Podaj prawdziwa wage!')
    return height


def open_advice(filename):
    filename = filename + ".txt"
    # ... try except

    try:
        with open(filename) as file:
            advice = file.read()
    except FileNotFoundError:
        advice = 'Nie znaleziono pliku'

    return advice


if __name__ == "__main__":
    m = get_weight()
    h = get_height()
    result = exceptions05.calculate_BMI(m, h)
    print(result)
    print(open_advice(result))
