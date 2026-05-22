def calculate_factorial(number):
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    return factorial

num = 5

print("Factorial of", num, "is", calculate_factorial(num))