# For loops - we know in advance the number of iterations
# While loops - we don't know the no. of iterations- depends on conditions

# For loop
for i in range (5):
    print(f"Iteration {i}")

# While loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

#Challenge - Write a program that prints the first 10 Fibonacci numbers using both a for loop and a while loop.

# For loop
def fibonacci_for_loop(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

print("Fibonacci numbers using for loop:")
print(fibonacci_for_loop(10))

# While loop
def fibonacci_while_loop(n):
    fib_sequence = [0, 1]
    i = 2
    while i < n:
        fib_sequence.append(fib_sequence[i-1] + fib_sequence [i-2])
        i += 1
    return fib_sequence

print("\nFibonacci numbers using while loop:")
print(fibonacci_while_loop(10))
        