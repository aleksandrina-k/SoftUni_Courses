def fill_pieces(n: int):
    pieces = {}
    for _ in range(n):
        piece, composer, key = input().split('|')
        pieces[piece] = {'composer': composer, 'key': key}
    return pieces


def print_all(pieces: dict):
    for piece, info in pieces.items():
        print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")


def add(pieces: dict, piece, composer, key):
    if piece in pieces:
        print(f"{piece} is already in the collection!")
    else:
        pieces[piece] = {'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    return pieces


def remove(pieces: dict, piece):
    if piece in pieces:
        pieces.pop(piece)
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces


def change_key(pieces: dict, piece, new_key):
    if piece in pieces:
        pieces[piece]['key'] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces


if __name__ == '__main__':
    n = int(input())
    pieces = fill_pieces(n)

    while True:
        line = input().split('|')
        if line[0] == 'Stop':
            break
        elif line[0] == 'Add':
            piece = line[1]
            composer = line[2]
            key = line[3]
            pieces = add(pieces, piece, composer, key)

        elif line[0] == 'Remove':
            piece = line[1]
            pieces = remove(pieces, piece)

        elif line[0] == 'ChangeKey':
            piece = line[1]
            new_key = line[2]
            pieces = change_key(pieces, piece, new_key)

    print_all(pieces)
