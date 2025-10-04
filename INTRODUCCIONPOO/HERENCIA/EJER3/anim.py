class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def desplazarse(self):
        pass

class Leon(Animal):
    def desplazarse(self):
        print(f"{self.nombre} el león está caminando")

class Pinguino(Animal):
    def desplazarse(self):
        print(f"{self.nombre} el pingüino está nadando")

class Canguro(Animal):
    def desplazarse(self):
        print(f"{self.nombre} el canguro está saltando")

def main():
    animales = [
        Leon("Simba", 5),
        Pinguino("Pablo", 3),
        Canguro("Kiki", 2),
        Leon("Mufasa", 10),
        Pinguino("Penny", 1),
        Canguro("Skippy", 4)
    ]

    for animal in animales:
        animal.desplazarse()

if __name__ == "__main__":
    main()