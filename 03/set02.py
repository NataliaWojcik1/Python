# To jest 3!! Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
# a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.


animal=('jez', 'kot', 'pies', 'lis')
food=('pizza', 'kanapka','ciacho', 'sliwka')

list1 = list(animal[::2])
print(list1)
list2 = list(food[1::2])
print(list2)

set_all = set(list1 + list2)
print(set_all)