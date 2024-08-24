# Function to convert Fahrenheit to Celsius
def temp_converter(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = temp_converter(fahrenheit)

print('The temperature in celsius:',celsius,'degrees')
