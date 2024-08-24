# List to store the inputs
inputs = []

while True:
    user_input = input("Enter a value (type 'stop' to end): ")

    if user_input.lower() == 'stop':
        break
    else:

        inputs.append(user_input)

print("Entered values:", inputs)
