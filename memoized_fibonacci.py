def fibonacci(n, memo={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n not in memo:
        fib_n = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        memo[n] = fib_n
    return memo[n]
