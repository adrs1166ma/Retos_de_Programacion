"""
Estructuras para el extra USAR MATCH y CASE por defencto case _: y el BREACK
"""
# o Colecciones
# sirven para organizar datos

# Listas []
my_list: list = ["Adrs", "Berta", "Carlos", "Dario"]
print(my_list) # imprimir lista
print('acceso normal'.center(30,'-'))
print(my_list[0])  # Elemento 0
print(my_list[1])  # Elemento 1
print(my_list[2])  # Elemento 2
print(my_list[3])  # Elemento 3

print(' '); print(' ')

print('acceso inverso'.center(30,'-'))
print(my_list[-1]) # Elemento ultimo
print(my_list[-2]) # Elemento penultimo
print(my_list[-3]) # Elemento antes del pen
print(my_list[-4]) # Elemento antes de la anterior

print(' '); print(' ')

print('Imprimir un rango'.center(30,'-'))
print(' ')
print('sin incluir el indice 2')
print(my_list[0:2])
print(' ')
print('Ir del inicio de la lista al índice (sin incluirlo)')
print(my_list[:3])
print(' ')
print('Ir del índice indicado hasta el final')
print(my_list[1:])
print(' ')
print('Cambiar valor'.center(30,'-'))
print(my_list)
my_list[1] = "Cuervillo"
print(my_list)
print(' ')
print('Iterar una lista'.center(30,'-'))
print(my_list)
for lista in my_list:
    print(lista)
else:
    print('No existen mas nombres en la lista')

print(' '); print(' ')

print(''.center(30,'-'))
print('preguntar el largo de una lista')
print(my_list)
print(len(my_list))
print(' ')
print('agregar un elemento o insercion'.center(30,'-'))
print(my_list)
my_list.append("Castor")  # Inserción
print(my_list)
print(' ')
print('insertar un elemento en un índice en específico'.center(30,'-'))
print(my_list)
my_list.insert(1, 'Octavio')
print(my_list)
print(' ')
print('Ordenar')
my_list.sort()  # Ordenación
print(my_list)
print(' ')
print(type(my_list)) # tipo
print(' ')
print('remover elemento')
print(my_list)
my_list.remove("Dario")  # Eliminación
print(my_list)
print(' ')
print('remover el último valor agregado')
print(my_list)
my_list.pop()
print(my_list)
print(' ')
print('eliminar un indice')
print(my_list)
del my_list[0]
print(my_list)
print(' ')
print('limpiar un indice'.center(30,'-'))
print(my_list)
my_list.clear()
print(my_list)

print(' '); print(' ')

print('borrar la lista por COMPLETO'.center(30,'-'))
del my_list
try:
    print(my_list)
except:
    print('Se ha producido un error')
finally:
    print("Ha finalizado el manejo de excepciones")


# Tuplas () - inmutable
my_tuple: tuple = ("Brais", "Moure", "@mouredev", "36")
print('Acceso - acceder a un elemento'.center(30,'-'))
print(my_tuple[0])  # Acceso
print(my_tuple[1])  # Acceso
print(my_tuple[2])  # Acceso
print('Acceso inverso'.center(30,'-'))
print(my_tuple[-1])
print(my_tuple[-2])
print(my_tuple[-3])

print(' '); print(' ')

print('Imprimir un rango'.center(30,'-'))
print(' ')
print('sin incluir el indice 2')
print(my_tuple[0:1])

print(' ')

print('Iterar una tupla'.center(30,'-'))
print(my_tuple)
for tupla in my_tuple:
    print(tupla, end=' ')
else:
    print('No existen mas nombres en la tupla')

print(' '); print(' ')

print('ordenacion')
print(my_tuple)
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)
print(' ')
print('tipo')
print(type(my_tuple))
print(' ')

print(' '); print(' ')

print('cambiar valor de una tupla'.center(30,'-'))
print(my_tuple)
# frutas[0] = 'Pera'
tupla_lista = list(my_tuple)
tupla_lista[0] = 'Pera'
my_tuple = tuple(tupla_lista)
print('\n',my_tuple)

print(' '); print(' ')

print('eliminar la tupla'.center(30,'-'))
del my_tuple
try:
    print(my_tuple)
except:
    print('no se encontro la tupla')
finally:
    print('Ha finalizado el manejo de excepciones')



# # Sets {} - no se guardan duplicados - hashset - no se ordena
my_set: set = {"Brais", "Moure", "@mouredev", "36"}
print(my_set)
print("largo")
print(len(my_set))
print(' ')
print('revisar si un elemento está presente')
print('Moure' in my_set)
print(' ')
print('agregar un elemento')
print(my_set)
my_set.add("mouredev@gmail.com")  # Inserción
# my_set.add("mouredev@gmail.com") # no se pueden agregar 2 iguales
print(my_set)

print(' '); print(' ')

print('eliminar elemento posiblemente arrojando un error')
my_set.remove("Moure")  # Eliminación
print(my_set)
print(' ')
print('eliminar sin arrojar error')
print(my_set)
my_set.discard('36')
print(my_set)

print(' '); print(' ')

print('no se puede ordenar')
# my_set = set(sorted(my_set))  # No se puede ordenar
# print(my_set)
print(' ')
print('tipo')
print(type(my_set))
print(' ')
print('limpiar set')
my_set.clear()
print(my_set)
print(' ')
print('eliminar set')
del my_set
try:
    print(my_set)
except:
    print('no se encontro "set" ')
finally:
    print('finalizo el intento')



# Diccionario { : }, (key, value), es acceso y ordenado diferente
my_dict: dict = {
    "name": "Brais",
    "surname": "Moure",
    "alias": "@mouredev",
    "age": "36"
}
# imprimir y largo aca es lo mismo


print('acceder a un elemento (key)')
print(my_dict["name"])  # Acceso
print(' ')
print('otra forma de recuperar un elemento')
print(my_dict.get('age'))

print(' '), print('')

print('modificando elementos o agregar y actualizar')
print(my_dict)
my_dict["email"] = "mouredev@gmail.com"  # Inserción y modificacion
print(my_dict)
print(' ')

print(' '), print('')

print('recorrer los elementos')
for termino, valor in my_dict.items():
    print(termino, valor)

for termino in my_dict.keys():
    print(termino)

for valor in my_dict.values():
    print(valor)

print(''), print('')

print('ordenar')
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Ordenación .items
print(my_dict)
print('')
print('comprobar existencia de algún elemento')
print('age' in my_dict)
print('')
print('remover un elemento')
print(my_dict)
my_dict.pop('age')
print(my_dict)
# clear para limpiar y del para eliminar


"""
EXTRA
"""
# IMPLEMENTAR
#busqueda
#insercion
#actualizacion
#eliminacion
# de contactos

# key = nomber , value = numero de telefono

# que operacion desea realizar

# deben ser enteros  y no mas de 9 digitos

#finalizar el programa

contactos: dict = {'':''}

print('welcome to contacts'.center(30,'-'))
opcion = 0
while opcion != 5:
    opcion = int(input('Que operacion desea realizar? '
                       '\n1. Buscar'
                       '\n2. Agregar'
                       '\n3. Actualizar y Mostrar'
                       '\n4. Eliminar'
                       '\n5. Finalizar'
                       ''
                       '\nOpcion : '))
    if opcion == 1:
        nombre = input('Ingrese el nombre que desea buscar: ')
        try:
            for nam, num in contactos.items():
                if nombre == nam:
                    print(f'Nombre: [{nam}] \nNumero: [{num}]')
        except:
            print('El nombre no existe')
        finally:
            print('')

    elif opcion == 2:
        nombre = input('para agregar ingrese el nombre: ')
        numero = int(input('para agregar ingrese el numero: '))
        if numero < 1000000000:
            contactos[nombre] = numero # agrega
            print('Contacto agregado')
            for nam, num in contactos.items(): # busca e imprime lo agregado
                if nam == nombre:
                    print(f'Nombre: [{nam}] \nNumero: [{num}]')
        else:
            print('el numero excede el limite de digitos')

    elif opcion == 3:
        for nam, num in contactos.items():
            print(f'Nombre: [{nam}] \nNumero: [{num}]')
            print('')

    elif opcion == 4:
        print('eliminar por nombre ')
        nombre = input('Coloca el nombre a elimnar')
        contactos.pop(nombre)
        print('Se elimino el contacto')

print('A finalizado el programa')

# .isdigit, len > 0 and len(phone)<=11

