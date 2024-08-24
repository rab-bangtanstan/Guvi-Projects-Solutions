# correct pwd
correct_password = "password123"

while True:
    entered_password = input("Enter the password: ")

    if entered_password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Please try again.")
