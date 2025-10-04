class Vehiculo:
    def __init__(self, conductor, placa, id):
        self.conductor = conductor
        self.placa = placa
        self.id = id

    def mostrarDatos(self):
        print(f"Conductor: {self.conductor}")
        print(f"Placa: {self.placa}")
        print(f"ID: {self.id}")

    def cambiarConductor(self, nuevo):
        self.conductor = nuevo
        print(f"El nuevo conductor es {self.conductor}")

    def desplazarse(self):
        print("El vehículo se está desplazando.")


class Bus(Vehiculo):
    def __init__(self, conductor, placa, id, capacidad, sindicato):
        super().__init__(conductor, placa, id)
        self.capacidad = capacidad
        self.sindicato = sindicato

    def desplazarse(self):
        print(f"El bus {self.placa} está transportando pasajeros.")


class Auto(Vehiculo):
    def __init__(self, conductor, placa, id, caballosFuerza, descapotable):
        super().__init__(conductor, placa, id)
        self.caballosFuerza = caballosFuerza
        self.descapotable = descapotable

    def desplazarse(self):
        print(f"El auto {self.placa} está rodando por la carretera.")


class Moto(Vehiculo):
    def __init__(self, conductor, placa, id, cilindrada, casco):
        super().__init__(conductor, placa, id)
        self.cilindrada = cilindrada
        self.casco = casco

    def desplazarse(self):
        print(f"La moto {self.placa} está circulando entre los autos.")


if __name__ == "__main__":
    bus1 = Bus("Mark", "BUS-456", 1, 40, "Sindicato A")
    auto1 = Auto("Sana", "AUTO-123", 2, 120, True)
    moto1 = Moto("Youngjae", "MOTO-789", 3, 250, True)

    print("=== Vehículos registrados ===")
    bus1.mostrarDatos()
    auto1.mostrarDatos()
    moto1.mostrarDatos()

    print("\n=== Desplazamientos ===")
    bus1.desplazarse()
    auto1.desplazarse()
    moto1.desplazarse()

    print("\n=== Cambio de conductor ===")
    bus1.cambiarConductor("Jinyoung")
