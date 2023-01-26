def factorial(n):
    num = 1

    for i in range(1, n+1):
        num *= i

    return num

print(factorial(3))

def factorial_self(n):
    if n == 1:
        return 1
    else:
        return n * factorial_self(n-1)

print(factorial_self(3))