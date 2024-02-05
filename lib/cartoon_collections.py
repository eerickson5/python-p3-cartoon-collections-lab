def roll_call_dwarves(dwarves):
    i = 1
    for dwarf in dwarves:
        print(f"{i}. {dwarf}")
        i += 1

def summon_captain_planet(planeteer_calls):
    return([f"{call.title()}!" for call in planeteer_calls])

def long_planeteer_calls(planeteer_calls):
    i = 0
    try:
        while len(planeteer_calls[i]) <= 4:
            i += 1
    except IndexError:
        return False
    return True

def find_the_cheese(foods):
    cheeses = ("gouda", "cheddar", "camembert")
    for food in foods:
        if food in cheeses:
            return food
    return None