# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
#
# Co wiemy o tych numerach tych kart?
#
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
#
# American Express card numbers start with 34 or 37 and have 15 digits.

# cards = [4,1,7,1,5,5,7,3,3,0,7,7,8,1,9,6]
#
# def card_number(card):
#     #for index in range(len(cards):
#     if cards[0] == 4 and len(cards) == 16 or len(cards) == 13:
#         print('visa')
#     elif cards[0] == 5 and cards[1] == 1 or cards[1] == 5
#
# card_number(cards)
#
#
# print(len(cards))

# def can_be_card_number(user_input):
#     if not len(user_input) in [13, 15, 16]:
#         return False
#     if not user_input.isdigit():
#         return False
#
#     return True
#
# def is_visa(card_number):
#     if len(user_input) in [13,14] and user_input[0] == '4':
#         return True
#     else:
#         return False

# def is_mastercard(card_number):
#     if 51 <= int(card_number[0:2]) <= 55 or 2222 <= int(card_number[0:4]) <= 2720 and len(card_number) == 16:
#         return True
#     else:
#         return False
#
# def is_america_express(card_number):
#     if card_number[0:2] in ['34', '37'] and len(card_number) == 15:
#         return True
#
#
# user_input = input('Give me a card number: ').replace(' ', '')
# # if not len(user_input) in [13, 15,16]
# #     print('This is not card number!')
# #
# # if not user_input.isdigit():
# #     print('This is not a card, laier')
# #
# # print(can_be_card_number(user_input))
#
# if can_be_card_number(user_input):
#
#     if is_visa(user_input):
#
#         print('Visa card')
#
#     elif is_mastercard(user_input):
#         print('Master card')
#
#     elif is_america_express(user_input):
#         print('America')
#
#     else:
#         print('To nie Karta Gnojku')
#
# else:
#     print('To nie jest numer karty')




