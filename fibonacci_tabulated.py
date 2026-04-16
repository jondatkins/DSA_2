def fibonacci(n):
    fib_table = [None] * (n + 1)
    if n == 0:
        fib_table[0] = 0
    else:
        fib_table[0] = 0
        fib_table[1] = 1
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table[n]
