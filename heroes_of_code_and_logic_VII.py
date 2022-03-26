heroes = {}
n = int(input())
for _ in range(n):
    line = input().split(' ')
    hero = line[0]
    hit_points = int(line[1])
    mana_points = int(line[2])

    heroes[hero] = {'hit': hit_points, 'mana': mana_points}

while True:
    command = input()
    if command == 'End':
        break

    command = command.split(' - ')
    if command[0] == 'CastSpell':
        name = command[1]
        mana_needed = int(command[2])
        spell = command[3]
        if heroes[name]['mana'] >= mana_needed:
            heroes[name]['mana'] -= mana_needed
            print(f"{name} has successfully cast {spell} and now has {heroes[name]['mana']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")

    elif command[0] == 'TakeDamage':
        name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes[name]['hit'] -= damage
        if heroes[name]['hit'] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['hit']} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            heroes.pop(name)

    elif command[0] == 'Recharge':
        name = command[1]
        amount = int(command[2])
        if heroes[name]['mana'] + amount >= 200:
            amount = 200 - heroes[name]['mana']
            heroes[name]['mana'] = 200
        else:
            heroes[name]['mana'] += amount
        print(f"{name} recharged for {amount} MP!")

    elif command[0] == 'Heal':
        name = command[1]
        amount = int(command[2])
        if heroes[name]['hit'] + amount >= 100:
            amount = 100 - heroes[name]['hit']
            heroes[name]['hit'] = 100
        else:
            heroes[name]['hit'] += amount
        print(f"{name} healed for {amount} HP!")

for hero, points in heroes.items():
    print(hero)
    print(f"  HP: {points['hit']}")
    print(f"  MP: {points['mana']}")
