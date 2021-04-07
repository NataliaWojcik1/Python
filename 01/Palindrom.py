# Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie.
# Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

sentence = input('Podaj zdanie: ')
sentence = sentence.replace(' ', '')
sentence = sentence.lower()

sentence_2 = sentence[::-1]

print('Czy zdanie jest palindromem: ', sentence == sentence_2)