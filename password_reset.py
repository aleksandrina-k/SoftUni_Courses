import re

if __name__ == '__main__':
    password = input()

    while True:
        command = input()
        if command == 'Done':
            break

        command = command.split(' ')
        if command[0] == 'TakeOdd':
            password = ''.join([l for i, l in enumerate(password) if i % 2 == 1])
            print(password)

        elif command[0] == 'Cut':
            index = int(command[1])
            length = int(command[2])
            substring = password[index: index + length]
            password = re.sub(substring, '', password, 1)
            print(password)

        elif command[0] == 'Substitute':
            substring = command[1]
            substitute = command[2]
            if substring in password:
                password = password.replace(substring, substitute)
                print(password)
            else:
                print('Nothing to replace!')

    print(f"Your password is: {password}")
