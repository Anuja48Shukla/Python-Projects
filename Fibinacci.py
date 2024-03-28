def fib(n):
    series = []
    a, b = 0, 1
    while len(series) < n:
    #while a < n:
        series.append(a)
        a, b = b, a + b

    return series


print("Enter the number:\n")
number=input()
fib_series = fib(number)
print("Fibonacci Series:")
print(fib_series)
