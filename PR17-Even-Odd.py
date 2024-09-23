# Function to separate even and odd numbers
def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers

# Input: List of numbers
input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Separate even and odd numbers
evens, odds = separate_even_odd(input_numbers)

# Display the results
print("Even numbers:", evens)
print("Odd numbers:", odds)
