# def function_name(parameters):
#     code block to execute
#     return result ~ optional return statement


def greet(name):
    return f"Hello, {name}!"

print(greet(input("Enter your name: ")))

#Challenge - Write a function called factorial that takes an integer as input and returns its factorial.

def factorial (n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
try:    
    user_input = int(input("Enter a number which you need to get a factorial: "))

    print(factorial(user_input))
except ValueError as e:
    print("Invalid input:", e)
