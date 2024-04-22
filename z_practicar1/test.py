from main import *
from main2 import *

pp1 = Producto('Leche', 99)
pp2 = Producto('Maiz', 66)
pp3 = Producto('Manzana', 123)
ps1 = [pp1, pp2]
orr1 = Orden(ps1)
orr1.agregar_producto(pp3)
print(orr1)
print(f'El total es: {orr1.calcular_total()}')

pp11 = Producto('Cereal', 10)
pp22 = Producto('Cerdo', 666)
pp33 = Producto('Manzana', 321)
ps2 = [pp11, pp22, pp33]
orr2 = Orden(ps2)
print(orr2)