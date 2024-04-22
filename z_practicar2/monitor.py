class Monitor:
    contadorMonitores = 0
    @classmethod
    def idMonitor(cls):
        cls.contadorMonitores += 1
        return cls.contadorMonitores
    def __init__(self, marca, tamaño):
        self._idMonitor = Monitor.idMonitor()
        self._marca = marca
        self._tamaño = tamaño
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    @property
    def tamaño(self):
        return self._tamaño
    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño
    def __str__(self):
        return f'Monitor[{self._idMonitor}]: Marca[{self._marca}], Tamaño[{self._tamaño}]'

if __name__ == '__main__':
    m1 = Monitor('apple', '1200')
    print(m1)
