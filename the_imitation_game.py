def insert(message, index: int, value: str):
    m_list = list(message)
    m_list.insert(index, value)
    return ''.join(m_list)


if __name__ == '__main__':
    message = input()

    while True:
        line = input()
        if line == 'Decode':
            break

        line = line.split('|')
        if line[0] == 'Move':
            n = int(line[1])
            message = message[n:] + message[:n]
        elif line[0] == 'Insert':
            index = int(line[1])
            value = line[2]
            message = insert(message, index, value)
        elif line[0] == 'ChangeAll':
            substring = line[1]
            replacement = line[2]
            message = message.replace(substring, replacement)

    print(f"The decrypted message is: {message}")
