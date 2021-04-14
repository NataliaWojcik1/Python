def party_planner(cookies,people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError as e:
        print('people cannot ebe zero')


    return num_each, leftovers


print(party_planner(20,5))