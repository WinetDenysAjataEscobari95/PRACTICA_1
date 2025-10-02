
class Producto:
    # a) Define la clase y los atributos
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # b) Agrega un método vender(cantidad: Int) que reste del stock
    def vender(self, cantidad):
        if cantidad > self.stock:
            print("No hay suficiente stock para vender.")
        else:
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

    # c) Agrega un método reabastecer(cantidad: Int) que sume al stock
    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Se reabastecieron {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

def main():
    producto = Producto("Camisa", 20.0, 100)
    producto.vender(20)
    producto.reabastecer(50)

if __name__ == "__main__":
    main()