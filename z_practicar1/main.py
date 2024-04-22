class Producto:
    contadorP = 0
    @classmethod
    def PK1(cls):
        cls.contadorP += 1
        return cls.contadorP
    def __init__(self, nombre, precio):
        self._id = Producto.PK1()
        self._nombre = nombre
        self._precio = precio
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        self._precio = precio
    def __str__(self):
        return f'ID[{self._id}] Producto[{self._nombre}] Precio[{self._precio}]'
if __name__ == '__main__':
    pp1 = Producto('Leche', 99)
    pp2 = Producto('Maiz', 66)
    pp3 = Producto('Manzana', 123)
    print(pp1)
    print(pp2)
    print(pp3)