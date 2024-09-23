
def prime_or_not(num1):
    result = "It is a prime number"

    if (num1 <= 0):
        result = "It is not a prime number"
        return result
    else:
        for i in range(2 ,num1):
            if num1 % i == 0:
                result = "It is not a prime number"
                return result

    return result




num = int(input("Enter a number:"))

print(prime_or_not(num))
