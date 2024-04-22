from raton import *
from teclado import *
from monitor import *
class Computadora:
    contadorComputadoras = 0
    @classmethod
    def idComputadora(cls):
        cls.contadorComputadoras += 1
        return cls.contadorComputadoras
    def __init__(self, nombre, monitor, teclado, raton):
        self._idComputadora = Computadora.idComputadora()
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    def __str__(self):
        return f'''
        {self._nombre} : {self._idComputadora}
        Monitor : {self._monitor}
        Teclado : {self._teclado}
        Raton : {self._raton}  
        '''
if __name__ == '__main__':
    t1 = Teclado('HP', 'USB')
    r1 = Raton('HP', 'USB')
    m1 = Monitor('HP', '1500')
    c1 = Computadora('Linux',t1,r1,m1)
    print(c1)
    t2 = Teclado('HP', 'USB')
    r2 = Raton('HP', 'USB')
    m2 = Monitor('HP', '1500')
    c2 = Computadora('Linux',t2,r2,m2)
    print(c2)
