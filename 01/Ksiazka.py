title = input('Podaj tytul ksiazki: ')
surname = input('Podaj nazwisko autora: ')
pages = input('Podaj liczbe stron: ')

print('Czy w tytule sa tylko litery:', title.isalpha())
print('Czy w nazwisku sa tylko litery: ', surname.isalpha())
print('Czy w liczbie stron są tylko liczby: ', pages.isnumeric())
title.capitalize()
surname.capitalize()

book = title + surname + pages
print(' '.join(book))
print(len(book))