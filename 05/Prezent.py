# Stwórz listę pomysłów na prezent dla swoich bliskich. Kiedy nadarzy się okazja, aby dać im prezent
# (święta, urodziny, rocznicę), program losowo wybierze jeden (i być może miejsca, w których możesz go zdobyć).

import random

gift_list = ['torebka', 'zegarek', 'pasek', 'chusta', 'kolczyki']

occasion = ['swieta', 'urodziny', 'rocznica', 'imieniny']

place = ['sklep', 'targ', 'galeria']

print('W tym roku kupilam', random.choice(gift_list), 'z okazji', random.choice(occasion), 'w', random.choice(place))