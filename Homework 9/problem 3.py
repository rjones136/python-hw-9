# Homework 9 - Problem 3
# Key Word Transposition Cipher

def encrypt(message, keyword):
    message = message.upper().replace(" ", "")
    keyword = keyword.upper()

    columns = len(keyword)

    while len(message) % columns != 0:
        message += "X"

    rows = len(message) // columns

    grid = []
    position = 0

    for row in range(rows):
        line = []
        for col in range(columns):
            line.append(message[position])
            position += 1
        grid.append(line)

    order = sorted(range(columns), key=lambda i: (keyword[i], i))

    encrypted = ""

    for col in order:
        for row in range(rows):
            encrypted += grid[row][col]
        encrypted += " "

    return encrypted.strip()


def decrypt(message, keyword):
    message = message.replace(" ", "")
    keyword = keyword.upper()

    columns = len(keyword)
    rows = len(message) // columns

    grid = []

    for row in range(rows):
        grid.append([""] * columns)

    order = sorted(range(columns), key=lambda i: (keyword[i], i))

    position = 0

    for col in order:
        for row in range(rows):
            grid[row][col] = message[position]
            position += 1

    decrypted = ""

    for row in range(rows):
        for col in range(columns):
            decrypted += grid[row][col]

    return decrypted


message = input("Enter a message: ")
keyword = input("Enter a keyword: ")

if keyword == "":
    print("Keyword cannot be empty.")
else:
    encrypted = encrypt(message, keyword)
    decrypted = decrypt(encrypted, keyword)

    print("Original Message:", message)
    print("Encrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)
