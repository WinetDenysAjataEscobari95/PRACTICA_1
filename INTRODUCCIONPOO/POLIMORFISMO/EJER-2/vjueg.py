
class Videojuego:
    def __init__(self, nombre, plataforma, cantidad_jugadores=1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidad_jugadores = cantidad_jugadores

    @classmethod
    def con_plataforma(cls, nombre, plataforma):
        return cls(nombre, plataforma)

    def agregar_jugador(self):
        self.cantidad_jugadores += 1
        print(f"Se agregó un jugador a {self.nombre}. Cantidad de jugadores actual: {self.cantidad_jugadores}")

    def agregar_jugadores(self, cantidad):
        self.cantidad_jugadores += cantidad
        print(f"Se agregaron {cantidad} jugadores a {self.nombre}. Cantidad de jugadores actual: {self.cantidad_jugadores}")

def main():
    # Instanciar 2 videojuegos
    juego1 = Videojuego("FIFA", "PS4", 4)
    juego2 = Videojuego.con_plataforma("Call of Duty", "Xbox")

    # Agregar jugadores
    juego1.agregar_jugador()
    juego2.agregar_jugadores(int(input("Ingrese la cantidad de jugadores a agregar: ")))

    # Mostrar información
    print(f"Nombre: {juego1.nombre}, Plataforma: {juego1.plataforma}, Cantidad de jugadores: {juego1.cantidad_jugadores}")
    print(f"Nombre: {juego2.nombre}, Plataforma: {juego2.plataforma}, Cantidad de jugadores: {juego2.cantidad_jugadores}")

if __name__ == "__main__":
    main()