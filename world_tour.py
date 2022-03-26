def is_valid_index(index: int, stops: str):
    if 0 <= index < len(stops):
        return True
    return False


if __name__ == '__main__':
    stops = input()

    while True:
        command = input()
        if command == 'Travel':
            break

        command = command.split(':')
        if command[0] == 'Add Stop':
            index = int(command[1])
            new_stop = command[2]
            if is_valid_index(index, stops):
                stops = stops[:index] + new_stop + stops[index:]

        elif command[0] == 'Remove Stop':
            start = int(command[1])
            end = int(command[2])
            if is_valid_index(start, stops) and is_valid_index(end,stops):
                stops = stops[:start] + stops[end+1:]

        elif command[0] == 'Switch':
            old = command[1]
            new = command[2]
            if old in stops:
                stops = stops.replace(old, new)
        print(stops)

    print(f'Ready for world tour! Planned stops: {stops}')