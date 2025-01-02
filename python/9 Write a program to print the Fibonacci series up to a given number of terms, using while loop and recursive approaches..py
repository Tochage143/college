def fibonacci_while(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

terms = int(input("Enter the number of terms for Fibonacci series (using while loop): "))
fibonacci_while(terms)

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci_recursive(n - 1)
        series.append(series[-1] + series[-2])
        return series

terms = int(input("Enter the number of terms for Fibonacci series (using recursion): "))
result = fibonacci_recursive(terms)
print(" ".join(map(str, result)))
