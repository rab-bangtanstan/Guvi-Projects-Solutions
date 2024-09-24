num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
operator = input("Enter operator:")


if operator == '+':
    print("Addition of ", num1,"and", num2 , "is", num1+num2)
elif operator == '-':
    print("Subtraction of ", num1,"and", num2 , "is", num1-num2)
elif operator == '*':
    print("Multiplication of ", num1,"and", num2 , "is", num1*num2)
elif operator == '/':
    print("Division of ", num1,"and", num2 , "is", num1/num2)
elif operator == '//':
    print("Floor Division of ", num1,"and", num2 , "is", num1//num2)
elif operator == '**':
    print("Exponentiation of ", num1,"and", num2 , "is", num1**num2)
elif operator == '%':
    print("Modulus of ", num1,"and", num2 , "is", num1%num2)
else:
    print("Invalid operator")
