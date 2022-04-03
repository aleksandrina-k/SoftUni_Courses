import re

if __name__ == '__main__':
    pattern = r'^([$|%])([A-Z][a-z]{2,})\1: \[([\d]+)\]\|\[([\d]+)\]\|\[([\d]+)\]\|$'
    n = int(input())
    for _ in range(n):
        message = input()

        match = re.search(pattern, message)

        if match:
            tag = match.group(2)
            decrypted_message = chr(int(match.group(3))) + \
                                chr(int(match.group(4))) + \
                                chr(int(match.group(5)))

            print(f'{tag}: {decrypted_message}')
        else:
            print('Valid message not found!')
