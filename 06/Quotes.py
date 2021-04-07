from random import choice

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


filename = "Cytaty.txt"
with open('Cytaty.txt', 'r') as fopen:
    lines = fopen.readlines()

quote = select_quote(lines)
show(quote)


print("Quote of the day is: ")
print('*' * 50, '\n')
print(quote)
print('*' * 50)
print("------------------")
show_first_5(lines)