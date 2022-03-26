def fill_plants(n: int):
    result = {}
    for _ in range(n):
        command = input().split('<->')
        plant = command[0]
        rarity = int(command[1])
        if plant not in result:
            result[plant] = {'rarity': 0, 'rating': []}
        result[plant]['rarity'] = rarity

    return result


def rate(dict: dict, plant: str, rating: int):
    if plant not in dict:
        print('error')
    else:
        dict[plant]['rating'].append(rating)
    return dict


def update(dict: dict, plant: str, new_rarity: int):
    if plant not in dict:
        print('error')
    else:
        dict[plant]['rarity'] = new_rarity
    return dict


def reset(dict: dict, plant: str):
    if plant not in dict:
        print('error')
    else:
        dict[plant]['rating'] = []
    return dict


def print_info(dict: dict):
    print("Plants for the exhibition:")
    for plant, info in dict.items():
        if len(info['rating']) > 0:
            av_rating = sum(info['rating']) / len(info['rating'])
        else:
            av_rating = 0
        print(f"- {plant}; Rarity: {info['rarity']}; Rating: {av_rating:.2f}")


if __name__ == '__main__':
    n = int(input())
    plants = fill_plants(n)

    while True:
        line = input()
        if line == 'Exhibition':
            break

        line = line.split(': ')
        if line[0] == 'Rate':
            attrib = line[1].split(' - ')
            plant = attrib[0]
            rating = int(attrib[1])
            plants = rate(plants, plant, rating)

        elif line[0] == 'Update':
            attrib = line[1].split(' - ')
            plant = attrib[0]
            new_rarity = int(attrib[1])
            plants = update(plants, plant, new_rarity)

        elif line[0] == 'Reset':
            plant = line[1]
            plants = reset(plants, plant)

    print_info(plants)
