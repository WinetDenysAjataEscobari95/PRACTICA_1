class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedido = None

    def __del__(self):
        print(f"Cliente {self.nombre} eliminado")

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_pedido(self):
        return self.pedido

    def set_pedido(self, pedido):
        self.pedido = pedido

class Pedido:
    def __init__(self, productos, estado="Registrado"):
        self.productos = productos
        self.estado = estado

    def __del__(self):
        print(f"Pedido {self.productos} eliminado")

    def get_productos(self):
        return self.productos

    def set_productos(self, productos):
        self.productos = productos

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

def main():
    cliente1 = Cliente("Lady Gaga")
    pedido1 = Pedido(["Café Expresso", "Torta de Maracuya"])

    cliente1.set_pedido(pedido1)

    print(f"Nombre del cliente: {cliente1.get_nombre()}")
    print(f"Productos del pedido: {cliente1.get_pedido().get_productos()}")
    print(f"Estado del pedido: {cliente1.get_pedido().get_estado()}")

    cliente1.get_pedido().set_estado("Preparado")
    print(f"Estado del pedido actualizado: {cliente1.get_pedido().get_estado()}")

if __name__ == "__main__":
    main()
