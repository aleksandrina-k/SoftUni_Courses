def add(zoo: dict, animal: str, needed_food: int, area: str):
    if area not in zoo:
        zoo[area] = {}

    if animal not in zoo[area]:
        zoo[area][animal] = 0
    zoo[area][animal] += needed_food

    return zoo


def feed(zoo: dict, animal: str, food):
    for area, animals in zoo.items():
        if animal in animals:
            animals[animal] -= food
            if animals[animal] <= 0:
                animals.pop(animal)
                print(f'{animal} was successfully fed')
    return zoo


def print_info(zoo: dict):
    print('Animals:')
    for animals in zoo.values():
        for animal, needed_food in animals.items():
            print(f"{animal} -> {needed_food}g")

    print('Areas with hungry animals:')
    for area, animals in zoo.items():
        length = len(zoo[area])
        if length > 0:
            print(f'{area}: {length}')


if __name__ == '__main__':
    zoo = {}

    while True:
        command = input()
        if command == 'EndDay':
            break
        command = command.split(': ')
        params = command[1].split('-')
        if command[0] == 'Add':
            animal = params[0]
            needed_food = int(params[1])
            area = params[2]
            zoo = add(zoo, animal, needed_food, area)

        elif command[0] == 'Feed':
            animal = params[0]
            food = int(params[1])
            zoo = feed(zoo, animal, food)

    print_info(zoo)