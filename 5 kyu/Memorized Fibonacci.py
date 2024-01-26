term = [0 for i in range(100000)]

def fibonacci(n):
    if n <= 1:
        return n

    if term[n] != 0:
        return term[n]

    else:
        term[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return term[n]