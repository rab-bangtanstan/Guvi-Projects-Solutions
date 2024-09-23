def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Input: weight in kilograms and height in meters
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Display the BMI result
print("Your BMI is:", bmi)

# Determine BMI category
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
