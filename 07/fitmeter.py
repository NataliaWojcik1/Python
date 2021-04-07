import bmi

def open_advice(filename):
    filename = filename + ".txt"
    with open(filename) as file:
        advice = file.read()
    return advice

if __name__ == "__main__":
    m = 56
    h = 1.6
    result = bmi.calculate_bmi(m, h)
    print(result)
    print(open_advice(result))