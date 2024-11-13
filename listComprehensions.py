#Create a list of squares from 0 - 9 using list comprehension
squares = [x**2 for x in range(10)]
print(squares)

#Create a list of even numbers from another list using list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7]
evens = [num for num in numbers if num % 2 == 0]
print(evens)

#Challenge - Create a list of all the odd numbers from 1 to 100 using list comprehension
odd_numbers = [num for num in range(1, 101) if num % 2 != 0]
print(odd_numbers)

# Challenge - Create a list of all the prime numbers from 1 to 100 using list comprehension.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Create a list of prime numbers from 1 to 100 using list comprehension
prime_numbers = [num for num in range(1, 101) if is_prime(num)]

# Print the resulting list
print(prime_numbers)