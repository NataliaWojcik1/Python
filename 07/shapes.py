# def circle(r):
#     circle_field = 3.14 * r**2
#     return circle_field
#
#
# def rectangle(a, b):
#     rectangle_field = a * b
#     return rectangle_field
#
#
# def triangle(a, h):
#     triangle_field = 0.5 * a * h
#     return triangle_field
#
# print('modul - wartosc zmiennej __name__:', __name__)

# n =int(input("give me number of rows and columns N: "))
#
# tab = [ ['-'] * n ] * n
#
#
#
# for row in tab:
#     print (' '.join(row))

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""


poem = poem.lower()

poem = poem.replace(',', '')


poem = poem.split()



poem_dict = {}
for word in poem:
    if word in poem_dict:
        poem_dict[word] += 1
    else:
        poem_dict[word] = 1


for key, value in poem_dict.items():
     print(key, ':', value)