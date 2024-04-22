from main import *
class Orden:
    contadorO = 0
    @classmethod
    def PK2(cls):
        cls.contadorO += 1
        return cls.contadorO
    def __init__(self, productos):
        self._id2 = Orden.PK2()
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
            return total


    def __str__(self):

        p_srt = ''
        for producto in self._productos:
            p_srt += producto.__str__() + ' | '
        return f'Orden[{self._id2}] \nPRODUCTOS: {p_srt}'




if __name__ == '__main__':
    pp1 = Producto('Leche', 99)
    pp2 = Producto('Maiz', 66)
    pp3 = Producto('Manzana', 123)
    ps1 = [pp1, pp2, pp3]
    orr1 = Orden(ps1)
    print(orr1)

    pp11 = Producto('Cereal', 10)
    pp22 = Producto('Cerdo', 666)
    pp33 = Producto('Manzana', 321)
    ps2 = [pp11, pp22, pp33]
    orr2 = Orden(ps2)
    print(orr2)