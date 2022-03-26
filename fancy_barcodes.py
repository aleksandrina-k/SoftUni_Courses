import re

if __name__ == '__main__':
    pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'

    n = int(input())
    for _ in range(n):
        barcode = input()
        match = re.search(pattern, barcode)
        if match:
            group = [l for l in match.group(1) if l.isdigit()]
            if group == []:
                group = '00'
            else:
                group = ''.join(group)

            print('Product group: ' + str(group))
        else:
            print('Invalid barcode')
