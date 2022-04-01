import re


def calculate_coolness(text, threshold):
    pattern = r'([:|*]{2})([A-Z][a-z]{2,})\1'
    cools = []
    counter = 0

    matches = re.finditer(pattern, text)
    for match in matches:
        counter += 1
        current_coolness = sum(map(ord, list(match.group(2))))
        if current_coolness > threshold:
            cools.append(match.group())

    return cools, counter


def calculate_threshold(text):
    digit_pattern = r'\d'
    product = 1

    matches = re.finditer(digit_pattern, text)
    for match in matches:
        product *= int(match.group())
    return product


def print_info(threshold, cools, counter):
    print(f'Cool threshold: {threshold}')
    print(f"{counter} emojis found in the text. The cool ones are:")
    for cool in cools:
        print(cool)


if __name__ == '__main__':
    text = input()
    threshold = calculate_threshold(text)

    cools, counter = calculate_coolness(text, threshold)
    print_info(threshold, cools, counter)
