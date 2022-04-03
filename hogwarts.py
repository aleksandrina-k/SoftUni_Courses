def abjuration(spell: str):
    spell = spell.upper()
    print(spell)
    return spell


def necromancy(spell: str):
    spell = spell.lower()
    print(spell)
    return spell


def illusion(spell: str, index, letter):
    if 0 <= index < len(spell):
        spell = spell[:index] + letter + spell[index + 1:]
        print('Done!')
    else:
        print('The spell was too weak.')
    return spell


def divination(spell: str, first, second):
    if first in spell:
        spell = spell.replace(first, second)
        print(spell)
    return spell


def alteration(spell: str, substring):
    if substring in spell:
        spell = spell.replace(substring, '')
        print(spell)
    return spell


if __name__ == '__main__':
    spell = input()

    while True:
        command = input().split(' ')
        if command[0] == 'Abracadabra':
            break

        if command[0] == 'Abjuration':
            spell = abjuration(spell)

        elif command[0] == 'Necromancy':
            spell = necromancy(spell)

        elif command[0] == 'Illusion':
            index = int(command[1])
            letter = command[2]
            spell = illusion(spell, index, letter)

        elif command[0] == 'Divination':
            first = command[1]
            second = command[2]
            spell = divination(spell, first, second)

        elif command[0] == 'Alteration':
            substring = command[1]
            spell = alteration(spell, substring)
        else:
            print('The spell did not work!')
