# Homework 9 - Problem 2
# Polybius Checkerboard

checkerboard = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T"],
    ["U", "V", "W", "X", "Y/Z"]
]

def find_letter(board, letter):
    for row in range(5):
        for col in range(5):
            if letter in board[row][col]:
                return (row, col)
    return None

def encrypt(message, board):
    encrypted = ""

    for letter in message.upper():
        if letter == " ":
            continue

        position = find_letter(board, letter)

        if position is not None:
            encrypted += str(position[0])
            encrypted += str(position[1])
            encrypted += " "

    return encrypted.strip()

def decrypt(message, board):
    decrypted = ""
    numbers = message.split()

    for number in numbers:
        row = int(number[0])
        col = int(number[1])
        decrypted += board[row][col][0]

    return decrypted

message = input("Enter a message: ")

encrypted_message = encrypt(message, checkerboard)
decrypted_message = decrypt(encrypted_message, checkerboard)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
