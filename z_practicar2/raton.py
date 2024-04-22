from d_e import *
class Raton(DispositivoEntrada):
    contadorRatones = 0
    @classmethod
    def idRaton(cls):
        cls.contadorRatones += 1
        return cls.contadorRatones
    def __init__(self, tipoEntrada, marca):
        DispositivoEntrada.__init__(self, tipoEntrada, marca)
        self._idRaton = Raton.idRaton()
    def __str__(self):
        return f'Raton[{self._idRaton}]: {DispositivoEntrada.__str__(self)}'
if __name__ == '__main__':
    r1 = Raton('Blue', 'HP')
    r2 = Raton('Blue', 'HP')
    print(r1)
    print(r2)