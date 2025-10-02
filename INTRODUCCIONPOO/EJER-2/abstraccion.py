class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.recaudado = 0

    def subir_pasajeros(self, cantidad):
        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
            print(f"Subieron {cantidad} pasajeros. Total de pasajeros: {self.pasajeros}")
        else:
            print("No hay suficientes asientos disponibles.")

    def cobrar_pasaje(self, cantidad):
        self.recaudado += cantidad * 1.50
        print(f"Se cobraron {cantidad} pasajes. Total recaudado: Bs. {self.recaudado:.2f}")

    def asientos_disponibles(self):
        return self.capacidad - self.pasajeros

    def mostrar_info(self):
        print(f"Pasajeros: {self.pasajeros}")
        print(f"Asientos disponibles: {self.asientos_disponibles()}")
        print(f"Total recaudado: Bs. {self.recaudado:.2f}")

def main():
    # Crear instancia del bus
    mi_bus = Bus(50)

    # Subir pasajeros
    mi_bus.subir_pasajeros(20)

    # Cobrar pasaje
    mi_bus.cobrar_pasaje(20)

    # Mostrar información
    mi_bus.mostrar_info()

    # Mostrar asientos disponibles
    print(f"Asientos disponibles: {mi_bus.asientos_disponibles()}")

if __name__ == "__main__":
    main()