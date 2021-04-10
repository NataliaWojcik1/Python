# 5▹ W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
# Co jeśli użytkownik poda wartość 60 kg ? Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.


def calculate_BMI(mass, height):
    bmi = mass / (height ** 2)
    bmi_rounded = round(bmi, 2)

    if bmi_rounded < 18:
        return "underweight"
    elif 18 <= bmi_rounded < 25:
        return "normal"
    elif 25 <= bmi_rounded < 30:
        return "overweight"
    elif bmi_rounded >= 30:
        return "obesity"
    else:
        return "Something went wrong."




# try:
#     weight = float(input('Podaj wage w kg: '))
#     height = float(input('Podaj wzrost w m: '))
# except ValueError as e:
#     print('Incorrect value ->', e)