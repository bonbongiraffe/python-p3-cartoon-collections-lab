def roll_call_dwarves(dwarves):
    counter = 1
    for dwarve in dwarves:
        print(f'{counter}. {dwarve}')
        counter += 1

def summon_captain_planet(calls):
    cp_calls = []
    for call in calls:
        cp_calls.append(f'{(call[0]).upper()}{call[1:]}!')
    return cp_calls


def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(items):
    for item in items:
        if item == "cheddar":
            return item
