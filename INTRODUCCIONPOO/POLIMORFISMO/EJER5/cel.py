class Celular:
    def __init__(self, nroTel, dueño, espacio, ram, nroApp):
        self.nroTel = nroTel
        self.dueño = dueño
        self.espacio = espacio
        self.ram = ram
        self.nroApp = nroApp

    def __str__(self):
        return f"Número de teléfono: {self.nroTel}, Dueño: {self.dueño}, Espacio: {self.espacio} GB, RAM: {self.ram} GB, Número de aplicaciones: {self.nroApp}"

    def __iadd__(self, other):
        self.nroApp += 10
        return self

    def __isub__(self, other):
        self.espacio -= 5
        if self.espacio < 0:
            self.espacio = 0
        return self

def main():
    celular = Celular("123456789", "Juan", 128, 8, 10)
    print("Antes de los operadores:")
    print(celular)

    celular += 1
    celular -= 1
    print("\nDespués de los operadores:")
    print(celular)

if __name__ == "__main__":
    main()
