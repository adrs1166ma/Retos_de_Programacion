# Fucionces, un bloque de codigo para poder ser reutilizado
"""
 Funciones definidas por el usuario
"""

# Simple
def greet():
    print('Hola, Python!')
greet()
def return_greet():
    return 'Hola, Python!!'
a = return_greet()
print(a)
print(return_greet())

# Con un argumento
def arg_greet(name):
    print(f'Hola, {name}!!!')
arg_greet('Adrs')

# Con un argumentos
def args_greet(greet, name):
    print(f'{greet}, {name}!')
args_greet('Hi','Adrs')
args_greet(name='Adrs', greet='Hi')

# Con un argumento predeterminado
def default_arg_greet(name="Python"):
    print(f'Hola, {name}!')
default_arg_greet("adrs")
default_arg_greet()

# Con argumentos y return
def return_args_greet(greet, name):
    return f'{greet}, {name}!'
print(return_args_greet('Hi', 'Adrs'))

# Con retorno de varios valores
def multiple_return_greet():
    return "Hola", "Python"
print(multiple_return_greet()) #estructura
greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un numero variable de argumentos
def variable_arg_greet(*names):
    for i in names:
        print(f'Hola, {i}')
variable_arg_greet("jose", "maira", "juan", "mario")

# Con un numero variable de argumentos con palabra clave
def variable_key_arg_greet(**names):
    for param, name in names.items(): # funcion .items descompone los elementos en clave y valor
        print(f'Hola, {name} ({param})!')
variable_key_arg_greet(
    language="Python",
    name="Anderson",
    alias="Adrs",
    age="19"
    )

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Funcion interna : Hola, Python!")
    inner_function()
outer_function()

"""
Funciones del lenguaje (built-in)
"""

print(len("Anderson")) # cuenta y es entero
print(type(36)) # imprime el tipo
print("Anderosn".upper()) # pone en mayusculas

"""
Variables locales y globales
"""

global_var = "Python"
print(global_var)

def hello_python():
    local_var = "Hola"
    print(f'{local_var}, {global_var}!')
print(global_var)
hello_python()
# print(local_var) # no se puede acceder a la variable local de una funcion

"""
Extra
"""

def cadena(cadena1, cadena2):
    num = 0
    for i in range(1,101):
        if (i % 3 == 0) and (i % 5 == 0):
            print(f'[{i}] Texto concatenado: {cadena1} {cadena2}')
            # num += 1
        elif i % 3 == 0:
            print(f'[{i}] Cadena de texto del primer parametro: {cadena1}')
            # num += 1
        elif i % 5 == 0:
            print(f'[{i}] Cadena de texto del segundo parametro: {cadena2}')
            # num += 1
        else:
            print(f'[{i}] ')
            num += 1
    # print(f'Se han impreso {num} veces los textos')
    # print(f'Se han impreso {num} veces los numeros')
    return num
# cadena('hola', 'Adrs')
print(cadena('hola', 'Adrs'))

