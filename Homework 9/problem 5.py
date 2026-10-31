# Homework 9 - Problem 5
# Keyword and Twisted Path Cipher

def make_grid(message, rows, columns):
    while len(message) < rows * columns:
        message += "X"

    grid = []
    position = 0

    for row in range(rows):
        new_row = []
        for column in range(columns):
            new_row.append(message[position])
            position += 1
        grid.append(new_row)

    return grid


def make_path(rows, columns):
    path = []

    for row in range(rows):
        if row % 2 == 0:
            for column in range(columns):
                path.append((row, column))
        else:
            for column in range(columns - 1, -1, -1):
                path.append((row, column))

    return path


def encrypt(message, keyword):
    columns = len(keyword)
    rows = 5

    grid = make_grid(message, rows, columns)
    path = make_path(rows, columns)

    twisted = ""
    for row, column in path:
        twisted += grid[row][column]

    twisted_grid = make_grid(twisted, rows, columns)

    order = sorted(range(columns), key=lambda x: (keyword[x], x))

    encrypted = ""
    for column in order:
        for row in range(rows):
            encrypted += twisted_grid[row][column]

    return encrypted


def decrypt(message, keyword):
    columns = len(keyword)
    rows = 5

    order = sorted(range(columns), key=lambda x: (keyword[x], x))

    grid = []
    for row in range(rows):
        grid.append([""] * columns)

    position = 0

    for column in order:
        for row in range(rows):
            grid[row][column] = message[position]
            position += 1

    twisted = ""
    for row in grid:
        for letter in row:
            twisted += letter

    path = make_path(rows, columns)

    original_grid = []
    for row in range(rows):
        original_grid.append([""] * columns)

    for position in range(len(path)):
        row, column = path[position]
        original_grid[row][column] = twisted[position]

    decrypted = ""
    for row in original_grid:
        for letter in row:
            decrypted += letter

    return decrypted


message = input("Enter a message: ")
message = message.replace(" ", "").upper()

keyword = input("Enter a keyword: ").upper()

while len(keyword) == 0 or len(message) > 5 * len(keyword):
    print("Message must fit in a 5-row grid.")
    keyword = input("Enter a longer keyword: ").upper()

encrypted = encrypt(message, keyword)
decrypted = decrypt(encrypted, keyword)

print("\nOriginal Message:", message)
print("Keyword:", keyword)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
