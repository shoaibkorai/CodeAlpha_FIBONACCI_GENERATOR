#method to generate fibonacci sequence  by taking one arguement as (n) and generate Fibonacci numbers  til the length of the sequence reaches n.
def fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[:n]



#usage 
fib_numbers = fibonacci(100)
print(fib_numbers)
