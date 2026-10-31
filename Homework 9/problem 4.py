# Homework 9 - Problem 4
# Twisted Path Cipher with Keyword

def create_grid(message):
    grid = []
    position = 0

    for row in range(5):
        line = []
        for column in range(6):
            line.append(message[position])
            position += 1
        grid.append(line)

    return grid


def create_path():
    path = []

    # Each tuple is a row and column location
    # Follow a twisting path through the grid
    for row in range(5):
        if row % 2 == 0:
            for column in range(6):
                path.append((row, column))
        else:
            for column in range(5, -1, -1):
                path.append((row, column))

    return path


def column_order(keyword):
    order = []

    for column in range(6):
        order.append(column)

    # Put columns in keyword alphabetical order
    for i in range(6):
        for j in range(i + 1, 6):
            if keyword[order[i]] > keyword[order[j]]:
                order[i], order[j] = order[j], order[i]

    return order


def encrypt(message, keyword):
    while len(message) < 30:
        message += "X"

    grid = create_grid(message)
    path = create_path()
    order = column_order(keyword)

    encrypted = ""

    # Follow the twisted path using keyword columns
    for row, column in path:
        encrypted += grid[row][order[column]]

    return encrypted


def decrypt(message, keyword):
    grid = []

    for row in range(5):
        grid.append([""] * 6)

    path = create_path()
    order = column_order(keyword)

    position = 0

    # Reverse the encryption process
    for row, column in path:
        grid[row][order[column]] = message[position]
        position += 1

    decrypted = ""

    for row in range(5):
        for column in range(6):
            decrypted += grid[row][column]

    return decrypted


# Main program
message = input("Enter a message: ").upper()
message = message.replace(" ", "")

keyword = input("Enter a keyword: ").upper()

while len(keyword) != 6 or not keyword.isalpha():
    keyword = input("Enter a 6-letter keyword: ").upper()

while len(message) > 30 or len(message) == 0:
    message = input("Enter a message of 1 to 30 letters: ").upper()
    message = message.replace(" ", "")

encrypted_message = encrypt(message, keyword)
decrypted_message = decrypt(encrypted_message, keyword)

print("\nOriginal Message:", message)
print("Keyword:", keyword)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
