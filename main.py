def factorial(n):
    if n == 1:
        return 1
    else:
        a = n
        print(f'{n} * fac({a})-1')
        return n * factorial(n-1)

print(factorial(4))
