class Persona:
    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci

    def mostrarDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"CI: {self.ci}")


class Cliente(Persona):
    def __init__(self, nombre, apellido, ci, nro_compra, id_cliente):
        super().__init__(nombre, apellido, ci)
        self.nro_compra = nro_compra
        self.id_cliente = id_cliente

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Nro de compra: {self.nro_compra}")
        print(f"ID de cliente: {self.id_cliente}")


class Jefe(Persona):
    def __init__(self, nombre, apellido, ci, sucursal, tipo):
        super().__init__(nombre, apellido, ci)
        self.sucursal = sucursal
        self.tipo = tipo

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Sucursal: {self.sucursal}")
        print(f"Tipo: {self.tipo}")


# ----------- MAIN (opcional) ------------
if __name__ == "__main__":
    print("=== Datos del Cliente ===")
    c1 = Cliente("Lisa", "Simpson", "7896543", "C123", "CL01")
    c1.mostrarDatos()

    print("\n=== Datos del Jefe ===")
    j1 = Jefe("Ned", "Flanders", "4563219", "Central", "General")
    j1.mostrarDatos()
