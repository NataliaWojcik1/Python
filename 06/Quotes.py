from random import choice
import random


def select_quote(quotes):
    quote = choice(quotes)
    quote = quote.center(50)
    return quote


def show(quote):
    quote = quote.strip().split('-')
    print(quote)


def show_first_5(quotes):
    for q in quotes[0:5]:
        print(q.strip())


def show_three_random(quotes):
    counter = 0
    if counter < 3:
        counter += 1
        que = random.choice(quotes)
        print(que)


filename = "Cytaty.txt"
with open('Cytaty.txt', 'r') as fopen:
    lines = fopen.readlines()

# quote = select_quote(lines)
# show(quote)

# print("Quote of the day is: ")
# print('*' * 50, '\n')
# print(quote)
# print('*' * 50)
# print("------------------")
# show_first_5(lines)
print(show_three_random(lines))
