from Retos_de_Programacion.z_practicar2.computadora import Computadora
from Retos_de_Programacion.z_practicar2.monitor import Monitor
from Retos_de_Programacion.z_practicar2.raton import Raton
from Retos_de_Programacion.z_practicar2.teclado import Teclado


class Orden:
    contadorOrdenes = 0
    @classmethod
    def idOrden(cls):
        cls.contadorOrdenes += 1
        return cls.contadorOrdenes
    def __init__(self, computadoras):
        self._idOrden = Orden.idOrden()
        self._computadoras = list(computadoras)
    @property
    def computadoras(self):
        return self._computadoras
    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras
    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)
    def __str__(self):
        computadora_str = ''
        for computadora in self._computadoras:
            computadora_str += computadora.__str__() + ' Gracias por su compra CONCHA TUU MARE!! '.center(50,'-')
        return f'''Orden[{self._idOrden}]
                Computadoras: {computadora_str}
                '''
if __name__ == '__main__':
    t1 = Teclado('HP', 'USB')
    r1 = Raton('HP', 'USB')
    m1 = Monitor('HP', '1500')
    c1 = Computadora('Linux',t1,r1,m1)
    preOr1 = [c1]
    or1 = Orden(preOr1)
    print(or1)

    t2 = Teclado('HP', 'USB')
    r2 = Raton('HP', 'USB')
    m2 = Monitor('HP', '1500')
    c2 = Computadora('Linux',t2,r2,m2)
    preOr2 = [c2]
    or2 = Orden(preOr2)
    print(or2)
