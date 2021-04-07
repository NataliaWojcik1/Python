# 1▹ Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.
# pi * r * r

# def circle_area(radius):
#     return 3.14 * radius **2
#
# print(circle_area(4))

# 2▹ Napisać funkcję, która sprawdza czy liczba jest parzysta.

# 3▹ Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

def sum_list(arr):
    sum_items = 0

    for item in arr:
        sum_items += item

    return sum_items

# main part

result = sum_list([1, 2,3,1])
print(result)

# wszystko do zadania 6