import re

if __name__ == '__main__':
    pattern = r'([\|#])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
    total_calories = 0
    string_info = ''
    food_info = input()

    matches = re.finditer(pattern, food_info)
    for match in matches:
        total_calories += int(match.group(4))
        string_info += f'Item: {match.group(2)}, Best before: {match.group(3)}, Nutrition: {match.group(4)}\n'

    print(f'You have food to last you for: {total_calories//2000} days!')
    print(string_info)