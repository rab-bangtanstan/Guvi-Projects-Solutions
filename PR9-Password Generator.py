import random
import string

# Function to generate password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_list = []
    
    # Generate each character and add it to the list
    for i in range(length):
        random_char = random.choice(characters)
        password_list.append(random_char)
    
    # Combine the list into a string (password)
    password = ""
    for char in password_list:
        password += char
    
    return password

# Input: Desired password length
length = int(input("Enter the length of the password: "))

# Generate and display the password
print("Generated Password:", generate_password(length))
