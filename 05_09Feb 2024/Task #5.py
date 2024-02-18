# fibonacci series
def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_series = fib_series[-1] + fib_series[-2]
        fib_series.append(next_series)
    return fib_series


num = 10
result = fibonacci(num)
print(f"Fibonacci series up to {num} numbers: {result}")
