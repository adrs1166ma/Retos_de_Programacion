"""
Ejercicio
"""


def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)


countdown(100)

"""
Extra
"""


def factorial(number: int) -> int:
    if number < 0:
        print("Los números negativos no son válidos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5))
print('')

def fibonacci(number: int) -> int:
    if number <= 0:
        print("La posición tiene que ser mayor que cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        a = number
        print(f'({number} - 1) + ({number} - 2)')
        print(f'{a - 1} + {a - 2}')
        print(''.center(10,'-'))
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(9))