import random

# List out all the possible numbers, letters, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '(', ')', '*', '+']

print("Welcome to the password generator")

# Get user input for desired length of password characters 
print("How many letters would you like?")
letterLength = int(input())

print("How many numbers would you like?")
numberLength = int(input())

print("How many symbols would you like?")
symbolLength = int(input())

# Make password a list so we can shuffle it 
password = []

# Get random characters for password and append to password list 
for randomLetter in range(1, letterLength + 1):
    password.append(random.choice(letters))

for randomNumber in range(1, numberLength + 1):
    password.append(random.choice(numbers))

for randomSymbol in range(1, symbolLength):
    password.append(random.choice(symbols))

# Shuffle password characters around
random.shuffle(password)

# Convert password from list to string
finalPassword = ""
for character in password:
    finalPassword += character

print(f"Your password is: {finalPassword}")