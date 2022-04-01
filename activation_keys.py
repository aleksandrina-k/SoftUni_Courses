def contains(act_key, substr):
    if substr in act_key:
        print(f"{act_key} contains {substr}")
    else:
        print(f"Substring not found!")


def flip(act_key, case, start, end):
    if case == 'Upper':
        act_key = act_key[:start] \
                  + act_key[start:end].upper() \
                  + act_key[end:]
    else:
        act_key = act_key[:start] \
                  + act_key[start:end].lower() \
                  + act_key[end:]
    print(act_key)
    return act_key


def slice(act_key, start, end):
    act_key = act_key[:start] + act_key[end:]
    print(act_key)
    return act_key


if __name__ == '__main__':
    activation_key = input()

    while True:
        command = input().split('>>>')
        if command[0] == 'Generate':
            break

        elif command[0] == 'Contains':
            substring = command[1]
            contains(activation_key, substring)

        elif command[0] == 'Flip':
            case = command[1]
            start_index = int(command[2])
            end_index = int(command[3])
            activation_key = flip(activation_key, case, start_index, end_index)

        elif command[0] == 'Slice':
            start_index = int(command[1])
            end_index = int(command[2])
            activation_key = slice(activation_key, start_index, end_index)

    print(f"Your activation key is: {activation_key}")