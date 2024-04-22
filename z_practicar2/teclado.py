from d_e import *
class Teclado(DispositivoEntrada):
    contadorTeclados = 0
    @classmethod
    def idTeclado(cls):
        cls.contadorTeclados += 1
        return cls.contadorTeclados
    def __init__(self, tipoEntrada, marca):
        DispositivoEntrada.__init__(self, tipoEntrada, marca)
        self._idTeclado = Teclado.idTeclado()
    def __str__(self):
        return f'Teclado[{self._idTeclado}]: {DispositivoEntrada.__str__(self)}'
if __name__ == '__main__':
    t1 = Teclado('Blue', 'W')
    t2 = Teclado('Blue', 'W')
    print(t1)
    print(t2)