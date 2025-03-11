def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]

    return fibonacci

fib = caching_fibonacci()