# #  wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
# #
# poem = """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""
# # Zadbaj o sposób wyświetlania np.:
# #
# # szybko : 5
# #
# # zbudź : 1
#
# poem = poem.lower()
# poem = poem.replace(',', '')
# poem = poem.split()
#
# print(poem)
#
# poem_dict = {}
#
# for word in poem:
#     if word in poem_dict:
#         poem_dict[word] +=1
#     else:
#         poem_dict[word] = 1
#
# print(poem_dict)
#
# for key, value in poem_dict.items():
#     print(key, ':', value)


# names = ["Agnieszka", "Anna"]
#
# for name in names:
#     name = name.lower().replace(" ", "_")
#
# print(names)


# for i in (range(1,20,2)):
#     print(i)
 d = {'jablka' : 1, 'banany' : 2, 'gruszka' : 3}
 while d:
     print(d.popitem(), end='')
print('koniec')