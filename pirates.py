def fill_city_dict():
    dict = {}
    while True:
        command = input()
        if command == 'Sail':
            break
        command = command.split('||')
        city = command[0]
        population = int(command[1])
        gold = int(command[2])

        if city not in dict:
            dict[city] = {'population': 0, 'gold': 0}
        dict[city]['population'] += population
        dict[city]['gold'] += gold
    return dict


def plunder(dict: dict, town: str, people: int, gold: int):
    dict[town]['population'] -= people
    dict[town]['gold'] -= gold

    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

    if dict[town]['population'] <= 0 or dict[town]['gold'] <= 0:
        dict.pop(town)
        print(f"{town} has been wiped off the map!")
    return dict


def prosper(dict: dict, town: str, gold: int):
    if gold < 0:
        print(f"Gold added cannot be a negative number!")
    else:
        dict[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {dict[town]['gold']} gold.")
    return dict


def print_info(dict: dict):
    if not dict:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")
    else:
        print(f"Ahoy, Captain! There are {len(dict)} wealthy settlements to go to:")
        for town, info in dict.items():
            popul = info['population']
            gold = info['gold']
            print(f"{town} -> Population: {popul} citizens, Gold: {gold} kg")


if __name__ == '__main__':
    cities = fill_city_dict()

    while True:
        command = input()
        if command == 'End':
            break

        command = command.split('=>')
        if command[0] == 'Plunder':
            town = command[1]
            people = int(command[2])
            gold = int(command[3])
            cities = plunder(cities, town, people, gold)

        elif command[0] == 'Prosper':
            town = command[1]
            gold = int(command[2])
            cities = prosper(cities, town, gold)

    print_info(cities)
