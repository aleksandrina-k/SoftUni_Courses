import re

if __name__ == '__main__':
    pattern = r'(=|/)([A-Z][a-zA-Z]{2,})\1'

    line = input()

    countries = [c.group(2) for c in re.finditer(pattern, line)]
    points = sum([len(c) for c in countries])

    print("Destinations: " + ', '.join(countries))
    print("Travel Points: " + str(points))
