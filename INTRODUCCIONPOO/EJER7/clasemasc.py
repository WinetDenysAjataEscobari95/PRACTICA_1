class Mascota:
    def __init__(self, nombre, tipo, energia=100):
        self.nombre = nombre
        self.tipo = tipo
        self.energia = energia

    def alimentar(self):
        self.energia = min(100, self.energia + 20)
        print(f"{self.nombre} ha sido alimentado. Energía actual: {self.energia}")

    def jugar(self):
        self.energia = max(0, self.energia - 15)
        print(f"{self.nombre} ha jugado. Energía actual: {self.energia}")

def main():
    mascota1 = Mascota("Toby", "Perro")
    mascota2 = Mascota("Luke", "Gato")

    print(f"Energía inicial de {mascota1.nombre}: {mascota1.energia}")
    mascota1.alimentar()
    mascota1.jugar()

    print(f"\nEnergía inicial de {mascota2.nombre}: {mascota2.energia}")
    mascota2.alimentar()
    mascota2.jugar()
    mascota2.jugar()
    mascota2.jugar()
    mascota2.jugar()
    mascota2.jugar()
    mascota2.jugar()
    mascota2.jugar()

if __name__ == "__main__":
    main()

