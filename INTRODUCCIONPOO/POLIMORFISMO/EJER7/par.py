
class Parada:
    def __init__(self, nombreP=""):
        self.nombreP = nombreP
        self.admins = [None] * 10
        self.autos = [[None for _ in range(3)] for _ in range(10)]
        self.adminIndex = 0
        self.autoIndex = 0

    def mostrar(self):
        print(f"Nombre de la parada: {self.nombreP}")
        print("Administradores:")
        for admin in self.admins:
            if admin is not None:
                print(admin)
        print("Autos:")
        for auto in self.autos:
            if auto[0] is not None:
                print(f"Modelo: {auto[0]}, Conductor: {auto[1]}, Placa: {auto[2]}")

    def adicionarAdmin(self, admin):
        if self.adminIndex < len(self.admins):
            self.admins[self.adminIndex] = admin
            self.adminIndex += 1
        else:
            print("No hay más espacio para administradores")

    def adicionarAuto(self, modelo, conductor, placa):
        if self.autoIndex < len(self.autos):
            self.autos[self.autoIndex][0] = modelo
            self.autos[self.autoIndex][1] = conductor
            self.autos[self.autoIndex][2] = placa
            self.autoIndex += 1
        else:
            print("No hay más espacio para autos")

def main():
    parada = Parada("Parada 1")
    parada.adicionarAdmin("Admin 1")
    parada.adicionarAuto("Toyota", "Juan", "ABC123")
    parada.mostrar()

if __name__ == "__main__":
    main()