class DispositivoEntrada:
    def __init__(self, tipoEntrada, marca):
        self.__tipoEntrada = tipoEntrada
        self.__marca = marca
    @property
    def tipoEntrada(self):
        return self.__tipoEntrada
    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self.__tipoEntrada = tipoEntrada
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    def __str__(self):
        return f'Tipo de Entrada[{self.__tipoEntrada}], Marca[{self.__marca}]'
if __name__ == '__main__':
    p = DispositivoEntrada('bluetooh', 'hp')
    p1 = DispositivoEntrada('bluetooh', 'hp')
    print(p)
    print(p1)