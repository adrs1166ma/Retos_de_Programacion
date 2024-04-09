"""
Operadores de mi lenguaje
"""

# operando1 = a
# operando2 = b
# Respuesta = r

a = 5
b = 3

# Aritméticos
print(f'Suma: {a + b}')
print(f'Resta: {a - b}')
print(f'Multiplicacion: {a * b}')
print(f'Division: {a / b}')
print(f'Divicion (int - entero): {a // b}')
print(f'residuo: {a % b}')
print(f'exponente: {a ** b}')

# Comparación
print(f'La igualdad de a == b es: {a == b}')
print(f'La desigualdad de a == b es: {a != b}')
print(f'El mayor que de a == b es: {a > b}')
print(f'El menor que de a == b es: {a < b}')
print(f'El mayor igual de a == b es: {a >= b}')
print(f'El menor igual de a == b es: {a <= b}')

# lógicos
t = True
f = False
print(f'AND de True and False: {t and f} ')
print(f'OR de True and False: {t or f} ')
print(f'NOT de True: {not t} ')
print(f'NOT de False: {not f} ')

# asignación
numero = 10 # asignacion | numero = 10
print(numero)
numero += 1 # suma     | numero = numero + 1 | con reasignacion
print(numero)
numero -= 1 # resta    | numero = numero - 1 | con reasignacion
print(numero)
numero *= 1 # producto | numero = numero * 1 | con reasignacion
print(numero)
numero /= 1 # dividir  | numero = numero / 1 | con reasignacion
print(numero)
#raros
numero //= 1 # div(int)| numero = numero // 1 | con reasignacion
print(numero)
numero %= 1 # modulo   | numero = numero % 1  | con reasignacion
print(numero)
numero **= 1 #exponente| numero = numero ** 1 | con reasignacion
print(numero)

# Identidad
''' 1 '''
print(' | '.center(30,'-'))
print('PRIMER CASO')
print(f' Tomamos como refencia el ultimo valor imprimido')
print(f' de la variable " numero " que es = 0.0')
n1 = 0.0
print(f' creamos la variable " n1 " que tambien es = {n1} ')
print(' | '.center(30,'-'))
print(f' En Identidad, pasa lo siguiente: ')
print(f' numero es n1? | n is n1? : {numero is n1}')
print(f' numero no es n1? n no es n1?: {numero is not n1}')
''' 2 '''
print(' | '.center(30,'-'))
print('SEGUNDO CASO')
print(f'reasigando el mismo espacio de memoria a n1 con numero')
n1 = numero
print('n1 = numero')
print(f' n es n1? | n is n1? : {numero is n1}')
print(f' n no es n1? n no es n1?: {numero is not n1}')
''' 3 '''
print(' | '.center(30,'-'))
print('TERCER CASO')
print(f'a las 2 variables la igualamos a un mismo dato')
n = 2
n1 = 2
print(f' n es n1? | n is n1? : {n is n1}')
print(f' n no es n1? n no es n1?: {n is not n1}')
print(' | '.center(30,'-'))

# Pertenencia
print(" Comprobar si algo esta dentro de algo mas")
print(f' "o" in "Anderson" = {"u" in "Anderson"}  ')
print(f' "a" not in "Anderson" = {"a" not in "Anderson"}  ')

# bits
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 1010 # 1. 0101 # 2. 0010 = # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 1010 # 1010 00 = # 101000

"""
 Estructuras de control
"""
miCondicion = False

if miCondicion == True:
    print(' Mi condición es verdadera')
elif miCondicion == False:
    print('Mi condición es falsa')
else:
    print('Mi condición es reconocida')
# Iterativas
for i in range(0,11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1
# Manejo de excepciones
try:
    print(10 / 0)
except:
    print('Se ha producido un error')
finally:
    print("Ha finalizado el manejo de excepciones")

"""
 DIFICULTAD EXTRA
"""
for i in range(10,56):
    if i == 55:
        print(i)
    elif (i % 2 == 0) and (i != 16) and (i % 3 != 0):
        print(i)
print(f' Incluye el 10 y el 55'.center(30,'-'))
