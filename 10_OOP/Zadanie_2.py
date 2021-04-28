class Storczyk:
    def __init__(self, kolor, pora, gatunki):
        self.kolor = kolor
        self.pora = pora
        self.gatunki = gatunki


chinski = Storczyk('czerwony', 'zima', 'jednorodny')#definicja obiektu
print(chinski.kolor, chinski.pora, chinski.gatunki)