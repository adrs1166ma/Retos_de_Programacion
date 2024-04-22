from Retos_de_Programacion.z_practicar2.computadora import Computadora
from Retos_de_Programacion.z_practicar2.monitor import Monitor
from Retos_de_Programacion.z_practicar2.orden import Orden
from Retos_de_Programacion.z_practicar2.raton import Raton
from Retos_de_Programacion.z_practicar2.teclado import Teclado

t1 = Teclado('HP', 'USB')
r1 = Raton('HP', 'USB')
m1 = Monitor('HP', '1500')
c1 = Computadora('Linux', t1, r1, m1)
preOr1 = [c1]
or1 = Orden(preOr1)
print(or1)

t2 = Teclado('HP', 'USB')
r2 = Raton('HP', 'USB')
m2 = Monitor('HP', '1500')
c2 = Computadora('Linux', t2, r2, m2)
preOr2 = [c2]
or2 = Orden(preOr2)
print(or2)